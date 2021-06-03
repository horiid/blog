---
layout : post
---
## Introduction
Hi, I recently revived my good ol' gear ThinkPad X220 and tuned it to the completely "free" computer using Coreboot BIOS & Linux. I wrote down the guide here, so if you are interested, why not give it a try? It's pretty fun & exciting!

---
## Coreboot Requirements
All you have to do is flash the BIOS chip(ROM) on the motherboard with Raspberry Pi. Yes, to do that, you need some tools and anatomize your laptop.

### Laptop Computer
I recommend ThinkPad series since you can find a few documents associated with reviving them with Coreboot on the internet.

### Raspberry Pi 
To flash a chip, you need a raspi to run a command called "flashrom" for flashing ROM. Model 3B+ or later is recommended.
And don't forget a keyboard.

### IC Test Clip
If you're trying with ThinkPad X220, Use a SOIC 8-pin IC test clip. You can find it easily on the internet.

### Female-Female Jumpers
Connect those wires to the clip and raspi GPIO.

## Setting up the Raspberry Pi
Launch raspberry pi, and then do the followings:

### Update packages index
~~~
sudo apt update
~~~
### Install flashrom
~~~
sudo apt install flashrom
~~~
### Install dependencies
~~~
sudo apt install build-essential git libftdi1 libftdi-dev libusb-dev \
libpci-dev m4 bison flex libncurses5-dev libncurses5 pciutils \
usbutils libpci-dev libusb-dev zlib1g-dev libusb-1.0 gnat-4.9
~~~
### Clone Coreboot repo
~~~
clone --recurse-submodules https://review.coreboot.org/coreboot.git ~/coreboot
~~~
### Build ifdtool
~~~
cd ~/coreboot/util/ifdtool
make & sudo make install
~~~

### Clone me_cleaner (Optional but highly recommended)
~~~
git clone https://github.com/corna/me_cleaner ~/me_cleaner
~~~

### Rasberry Pi Pinout
It depends on which ROM you're trying to flash, so search the pinout for your computer accordingly on the web.

## Flashrom
### Set alias
Note that quotes after equal(=) is "back quote",  which makes shell to interpret string in the quoted section as a command.
~~~ 
alias fr=`sudo flashrom -p linux_spi:dev=/dev/spidev0.0,spispeed=1024`
~~~

### Identify ROM chip
"fr" is alias for the command set in the previous phase.
~~~
# Identify all chips
fr
~~~

### Read ROM for backup and checking connection
Reading ROM a few time(2~4 times) is recommended to ensure connection is fine.
~~~
fr -c "your chip name" -r backup01.bin
fr -c "your chip name" -r backup02.bin
fr -c "your chip name" -r backup03.bin
fr -c "your chip name" -r backup04.bin
~~~

### Compare checksums
If checksums are not the same, it means connection is not secure. Make sure the clip is stable. If they are the same, store backup01.bin at a safe location. One or more backups would be better since __the computer may not be able to boot after flashing.__
~~~
md5sum backup01.bin backup02.bin backup03.bin backup04.bin
~~~

### Run me_cleaner
Run me_cleaner to modify an Intel ME firmware image to reduce its ability to interact with the system.
~~~
~/me_cleaner/me_cleaner.py -S backup01.bin
~~~

### Extract blobs with ifdtool 
~~~
ifdtool -x backup01.bin
~~~

### Copy and move blobs
The path for blobs depends on your computer. In this time, it's lenovo X220.
~~~
mkdir -p ~/coreboot/3rdparty/blobs/mainboard/lenovo/x220
cd $_ 
cp path/to/blobs/flashregion_0_flashdescriptor.bin descriptor.bin
cp path/to/blobs/flashregion_2_intel_me.bin me.bin
cp path/to/blobs/flashregion_3_gbe.bin gbe.bin
~~~

## Configure & build Coreboot
### Configuration
SeaBIOS may need a VGABIOS firmware, so follow the guide [here](https://www.coreboot.org/VGA_support) to extract it just in case (Optional).

Run "make menuconfig" to launch coreboot configuration menu.
~~~
make menuconfig

# Coreboot configuration
General
    [*]Compress ramstage with LZMA
    [*] Include coreboot .config file into the ROM image
    [*] Allow use of binary-only repository

Mainboard
    Mainboard vendor (Select your hardware vendor)
    Mainboard model (Select your model)

Chipset
    [*] Enable VMX for virtualization
    [*] Add Intel descriptor.bin file
    [*] Add Intel ME/TXE firmware
    [*] Add gigabit ethernet firmware

# If using VGABIOS
Devices
    [*] Graphics initialization (Run VGA Option ROMs)
    [*] Add a VGA BIOS image
    [*] Add a Video Bios Table (VBT) binary to CBFS

Generic Drivers
    [*] PS/2 keyboard init

Console
    [*] Show POST codes on the debug console

Payload
    Add a payload (SeaBIOS) --->
    SeaBIOS version (master) --->
    [*] Hardware init during option ROM execution
~~~

### Build Coreboot
~~~
make
~~~
If you are running it on Raspberry Pi, then run below instead:
~~~
make crossgcc-i386 CPUS=4
make iasl
make
~~~

## Write Coreboot to the chip
Let's write coreboot to the chip. Make up your mind.
~~~
cd ~/coreboot/build
fr -c "your chip name" -w coreboot.rom
~~~
Be noted that the last step of the command will verify the chip and if it's successful, the final line would be like this:
~~~
Verifying flash... VERIFIED.
~~~

* If suceessful, shutdown the Raspberry Pi before removing the test clip.
* If failed, make sure coneection is fine and flash again.
* If still failed, revise config, rebuild coreboot and flash again.
* If still failed and you get too worried, give up and flash backup0X.bin. This is why we prepared backups.


---
## Install Linux
In this section, I'm going to introduce how to download/install Linux to your computer. In this time we are creating LiveUSB, which enables to launch OS from USB. It also makes it easy to install OS to actual device.

*Aside from Coreboot procedure, you can do this section independently if you simply want to install Linux to your computer.*
### Creating LiveUSB
Download [UNetbootin](https://unetbootin.github.io). It loads distributions either by downloading ISO image for you, but you can independently download/select ISO images. 
### Boot LiveUSB and install Linux
Boot the PC and press ESC key (if coreboot payload is SeaBIOS) before BIOS starts loading the OS that is already in the system. You will see install configuration menu of Linux, then choose your preferences and good to go.