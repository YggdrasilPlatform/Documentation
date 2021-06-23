.. _cmsis_dsp:

CMSIS DSP Library
=================

Built into libyggdrasil is the CMSIS DSP library. It gives access to highly optimized digital signal processing functions such as:

* Basic math functions
* Fast math functions
* Complex math functions
* Filtering functions
* Matrix functions
* Transform functions
* Motor control functions
* Statistical functions
* Support functions
* Interpolation functions
* Support Vector Machine functions (SVM)
* Bayes classifier functions
* Distance functions

|

.. seealso::
    | **CMSIS DSP Library Documentation**
    | Doxygen documentation
    | `>>> <https://www.keil.com/pack/doc/CMSIS/DSP/html/index.html>`_

Usage
-----

To make libyggdrasil include the cmsis dsp library, the following define needs to be added before the libyggdrasil include:

.. code-block:: cpp

    #define YGGDRASIL_USE_CMSIS_DSP
    #include <yggdrasil.h>
