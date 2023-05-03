# ploteeg
    Plot an eeg file using the mne toolbox.

    Treats .eeg files as Nihon Kohden, rather than as an errant .vhdr, which is mne's default behavior.
    Loads .fif files as is. Other files are loaded with the 'encoding="latin1"' argument to
    support extended character sets.

``` text


usage: ploteeg [-h] [-s SCALE] [-t START] [-d DURATION] [-e EPOCHS] [-b BGCOLOR] [-l LOWPASS] [-u HIGHPASS] [-o] [-f SAVENAME] [-x WIDTH] [-y HEIGHT] [-p PICK] filename

    Plot an eeg file using the mne toolbox.

    Files ending in _epo.fif, .set, .mat, and .sqd are treated as epoched data.
    Files ending in .eeg are treated as Nihon Kohden data.
    Files that end in .fif are treated as continuous data.
    Other file extensions will try to be loaded with the default mne behavior, 
    with the addition of the 'encoding="latin1"' argument to
    support extended character sets.
    

positional arguments:
  filename              filename to plot

options:
  -h, --help            show this help message and exit
  -s SCALE, --scale SCALE
                        scale size in uV, or 'auto'
  -t START, --start START
                        starting time in seconds (for continuous data)
  -d DURATION, --duration DURATION
                        duration to show in seconds (for continuous data)
  -e EPOCHS, --epochs EPOCHS
                        number of epochs to display (for epoched data)
  -b BGCOLOR, --bgcolor BGCOLOR
                        background color (for continuous data)
  -l LOWPASS, --lowpass LOWPASS
  -u HIGHPASS, --highpass HIGHPASS
  -o, --save            save a screenshot as filename_start.png, and exit
  -f SAVENAME, --savename SAVENAME
                        filename to save the screenshot as
  -x WIDTH, --width WIDTH
                        size of the plot in inches (inches, I know)
  -y HEIGHT, --height HEIGHT
                        size of the plot in inches
  -p PICK, --pick PICK  channel name filter, e.g. FP matches FP1, FP2, etc. channels


```

    
    https://github.com/JohnAtl/ploteeg
    
