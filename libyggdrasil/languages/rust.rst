.. _hal_rust:

Rust Project
============

.. important::

    Rust is not supported by libyggdrasil, however development is still possible. Instead, the cortex-m and stm32f7-hal crate will be used for development.

To start developing, make sure you have the Yggdrasil toolchain, Rust and VSCode with the Rust and Cortex Debug extension installed.

Setup
-----

Installing the Toolchain
^^^^^^^^^^^^^^^^^^^^^^^^

Refer to the :ref:`Toolchain <yggdrasil_toolchain>` page.

Installing Rust
^^^^^^^^^^^^^^^

| Download and install `Rustup <https://rustup.rs/>`_.
| Once installed, run ``rustup target add thumbv7em-none-eabihf`` to install the Rust toolchain for ARMv7.

Installing VSCode
^^^^^^^^^^^^^^^^^

| Download and install `VSCode <https://code.visualstudio.com/>`_.
| Once installed, open the extensions panel and install the ``Rust`` and ``Cortex-Debug`` extensions.

Clone the repository
^^^^^^^^^^^^^^^^^^^^

.. code-block:: sh
    
    git clone https://gitlab.ti.bfh.ch/yggdrasil/midgard/midgard_rust_template --recurse-submodules


Usage
-----

To get started, clone the latest `Midgard Rust Template <https://gitlab.ti.bfh.ch/yggdrasil/midgard/midgard-rust-template>`_ from GitLab. 

| To compile the project, simply open the ``Run and Debug`` panel, select ``Debug Template`` or one of the ``Debug Example <XYZ>`` entries from the list and click on the Run button.
| Alternatively, you can also use ``cargo build`` to compile the template or ``cargo build --example=<example_name>`` to compile an example. 