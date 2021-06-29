GNU / Linux
===========

.. seealso::
    * `Asgard Linux Repository <https://gitlab.ti.bfh.ch/yggdrasil/asgard/asgard_linux>`_

The Asgard Linux Kernel port is currently based on **5.10.40+** of the mainline repository combined with RobertCNelson's `ARMv7 patches for STM32MP1 <https://github.com/RobertCNelson/armv7-lpae-multiplatform/tree/v5.10.x>`_

.. seealso::
    | **Build Linux**
    | Building Linux from scratch and creating a sd card
    | :ref:`>>> <LinuxBuilding>`

.. seealso::
    | **GPIO Access**
    | Accessing GPIOs through sysfs
    | :ref:`>>> <LinuxGPIOAccess>`


Building
^^^^^^^^

.. code-block:: shell

    $ export CROSS_COMPILER=arm-none-linux-gnueabihf-
    $ make ARCH=arm CROSS_COMPILE=${CROSS_COMPILER} distclean
    $ make ARCH=arm CROSS_COMPILE=${CROSS_COMPILER} asgard_defconfig
    $ make ARCH=arm CROSS_COMPILE=${CROSS_COMPILER} uImage vmlinux dtbs LOADADDR=0xC2000040 -j$((`nproc`+1))
    $ make ARCH=arm CROSS_COMPILE=${CROSS_COMPILER} modules



.. toctree::
    :maxdepth: 1
    :caption: Contents:
    :hidden:

    building
    gpio_calculation