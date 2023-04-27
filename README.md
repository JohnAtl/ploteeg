# ploteeg
    Plot an eeg file using the mne toolbox.


    Plot an eeg file using the mne toolbox.

    Treats .eeg files as Nihon Kohden, rather than as an errant .vhdr, which is mne's default behavior.
    Loads .fif files as is. Other files are loaded with the 'encoding="latin1"' argument to
    support extended character sets.

``` bash


usage: ploteeg [-h] [-s SCALE] [-t START] [-d DURATION] [-b BGCOLOR] [-l LOWPASS] [-u HIGHPASS] [-o] [-f SAVENAME] [-x WIDTH] [-y HEIGHT] filename

positional arguments:
  filename              filename to plot

options:
  -h, --help            show this help message and exit
  -s SCALE, --scale SCALE
                        scale size in uV
  -t START, --start START
                        starting time in seconds
  -d DURATION, --duration DURATION
                        duration shown in seconds
  -b BGCOLOR, --bgcolor BGCOLOR
                        background color
  -l LOWPASS, --lowpass LOWPASS
  -u HIGHPASS, --highpass HIGHPASS
  -o, --save            save a screenshot as filename_start.png, and exit
  -f SAVENAME, --savename SAVENAME
                        filename to save the screenshot as
  -x WIDTH, --width WIDTH
                        size of the plot in inches (inches, I know)
  -y HEIGHT, --height HEIGHT
                        size of the plot in inches

```

    
    https://github.com/JohnAtl/ploteeg
    
