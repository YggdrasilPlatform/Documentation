.. _yggdrasil_toolchain:

Yggdrasil Toolchain
===================

For developing applications for **Midgard using Rust** or for **Asgard under Linux** using VSCode instead of the STM32CubeIDE, a custom toolchain setup is required.
When developing on Midgard or Asgard's coprocessor, it's possible to use the custom toolchain, however it's much easier to just use the STM32CubeIDE instead.

Setup
-----

Download the latest release of the `Toolchain <https://gitlab.ti.bfh.ch/yggdrasil/toolchain/-/releases>`_. for your operating system from GitLab.

Windows
^^^^^^^

Unpack the toolchain zip to `C:/Dev`.

.. note::

    This path is important mainly for Linux development as the meson cross-compile configuration script will point to the wrong location. If you prefer to install the toolchain in a different location, you must adjust the config file named ``asgard`` in the ``yggdrasil/asgard`` folder accordingly.

For VSCode and the environment to pick up the toolchain, it must be added to the ``PATH`` environment variable. 
Search for ``Edit the system environement variables`` in the search box, click on ``Environement Variables...`` and add ``C:/Dev/yggdrasil/midgard/bin`` and ``C:/Dev/yggdrasil/asgard/bin`` to the PATH variable under **System variables**.

Linux
^^^^^

Unpack the toolchain zip to `/opt`.

.. note::

    This path is important mainly for Linux development as the meson cross-compile configuration script will point to the wrong location. If you prefer to install the toolchain in a different location, you must adjust the config file named ``asgard`` in the ``yggdrasil/asgard`` folder accordingly.

For VSCode and the environment to pick up the toolchain, it must be added to the ``PATH`` environment variable. 
Open your ``~/.bashrc``, ``~/.zshrc`` or similar shell config file and at the bottom add ``export PATH=/opt/yggdrasil/midgard/bin:/opt/yggdrasil/asgard/bin:$PATH``.
Restart the terminal or ``source`` the config file for the changes to be applied.