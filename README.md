# digitalframe

# Install (https://lb.raspberrypi.org/forums/viewtopic.php?t=78805&start=25#p1343999)
```
sudo apt-get install xserver-xorg-input-evdev xinput-calibrator -y
sudo mv /usr/share/X11/xorg.conf.d/10-evdev.conf /usr/share/X11/xorg.conf.d/45-evdev.conf
```

# Edit file /usr/share/X11/xorg.conf.d/99-calibration.conf
```
Section "InputClass"
    Identifier "calibration"
    MatchProduct "WaveShare WS170120"
    Option "Calibration" "229 3907 225 3951"
    Option "SwapAxes" "0"
EndSection
```
