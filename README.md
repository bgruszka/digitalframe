# digitalframe

# Edit file /boot/config.txt (https://www.waveshare.com/wiki/5inch_HDMI_LCD_(B)_(Firmware_Rev_2.1)_User_Manual)
```
max_usb_current=1
hdmi_group=2
hdmi_mode=87
hdmi_cvt 800 480 60 6 0 0 0
hdmi_drive=1
```

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
