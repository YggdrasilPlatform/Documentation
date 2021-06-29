u-boot
======

.. seealso::
    * `Asgard u-boot Repository <https://gitlab.ti.bfh.ch/yggdrasil/asgard/asgard_u-boot>`_

The Asgard u-boot port is currently based on **v2021.04** of the mainline u-boot repository.

Building
^^^^^^^^

.. code-block:: shell

    $ export CROSS_COMPILER=arm-none-linux-gnueabihf-
    $ make ARCH=arm CROSS_COMPILE=${CROSS_COMPILER} asgard_defconfig
    $ make ARCH=arm CROSS_COMPILE=${CROSS_COMPILER} DEVICE_TREE=stm32mp157c-dk2 all -j$((`nproc`+1))
