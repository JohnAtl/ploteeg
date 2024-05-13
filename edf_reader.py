import os
import re
import tempfile
from typing import Union

import edfio
import mne

from .config import ConfigKey, get_singleton_config
from .file_types import EEGFileName
from .fix_channels import standardize_channel_name, standardize_channel_name_order

config = get_singleton_config()


def _get_default_channels_re():
    channels = config[ConfigKey.SLEEP_MONTAGE] + config[ConfigKey.PHYSIOLOGY_MONTAGE]
    channels_re = "|".join([f"\\b{s}\\b" for s in channels])
    return channels_re


def read_edf(edf_filename: Union[str, EEGFileName], picks_re=None) -> mne.io.Raw:
    if picks_re is None:
        channels_re = _get_default_channels_re()
    else:
        channels_re = picks_re

    edf = edfio.read_edf(str(edf_filename))
    for signal in edf.signals:
        st_chan_name = standardize_channel_name(signal.label)
        if re.search(channels_re, st_chan_name):
            signal.label = st_chan_name
        else:
            try:
                edf.drop_signals(signal.label)
            except ValueError:
                pass  # just a duplicate signal
            except Exception:
                raise

    _, temp_filename = tempfile.mkstemp()
    temp_filename += ".edf"
    edf.write(temp_filename)
    new_edf = mne.io.read_raw(temp_filename, encoding="latin1", preload=True)
    channels_in_order = standardize_channel_name_order(new_edf.ch_names)
    new_edf.reorder_channels(channels_in_order)
    os.remove(temp_filename)
    return new_edf
