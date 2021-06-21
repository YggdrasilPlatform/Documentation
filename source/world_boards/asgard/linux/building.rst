Building Linux from Scratch
===========================

.. seealso::
    * :ref:`Yggdrasil Toolchain <yggdrasil_toolchain>`
    * `Asgard SDCard Builder <https://gitlab.ti.bfh.ch/yggdrasil/asgard/asgard_sdcard_builder>`_

Setup
-----

To get started, make sure you got a recent Linux installation as well as the Yggdrasil Toolchain correctly installed.

On Ubuntu, the following additional packages are required for compilation. On other Distros their name may differ, however compiling is always possible.

* lzop
* cpio
* u-boot-tools
* pv
* build-essential
* libssl-dev
* flex
* bison
* git

Compiling
---------

Clone the latest Asgard SDCard Builder from GitLab and enter the ``Linux`` folder. In there, run the following commands.

.. code-block:: shell

    ./get.sh
    $ export CROSS_COMPILER=arm-none-linux-gnueabihf-
    $ ./build.sh

This will automatically clone and compile u-boot and the Linux Kernel. It also downloads a minimal Ubuntu rootfs into ``rootfs.tar.gz``. If desired, this can simply be replaced with a custom one after running ``./get.sh``.

Flashing
--------

Plug in your SD Card and find out what device it got assigned to.

.. warning::

    The SD Card will **never** be ``/dev/sda``. This is the hard drive from which your Linux installation runs. Passing it to the flash script will destroy your installation!

Once that's done, run the following command to flash u-boot, Linux and the rootfs onto the SD Card.

.. code-block:: shell

    $ sudo ./flash.sh /dev/<sdcard_device>