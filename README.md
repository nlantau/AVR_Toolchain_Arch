# AVC Toolchain Arch

A bit more complicated than I expected it to be.
The `Pololu USB AVR Programmer v2.1`'s drivers already exists within the Linux kernel, but the .tar-ball from their site
provided with `pavr2cmd` and `pavr2gui`. At first, the `TTL port` and `Programming port` stated `(Unknown)`. As a last
restort, I rebooted the computer and finally Arch dedicated a **port** to it.


## How to view serial data from FTDI
```sh
tail -f /dev/ttyUSB0
```

## How to view data from DSO138mini oscilloscope
Run my Python script
```sh
./collect_and_plot.py
```

## How to setup permissions in Linux (for Arduino)
* Add user to group `uucp`

```sh
usermod -aG uucp <user>
```

* Add rule in `/etc/udev/rules.d/`

```sh
SUBSYSTEMS="usb", ATTRS{idVendor}=="xxxx", ATTRS{idProduct}=="yyyy", SYMLINK+="ttyUSB%n"
# Get idVendor and idProduct from `lsusb`

```

* Reload udev rules

```sh
udevadm config -R # Could differ depending on OS
```

* Reboot
