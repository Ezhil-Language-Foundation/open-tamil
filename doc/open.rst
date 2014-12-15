.. _test:


Documentation of **test** source code
***********************************************

The test package contains the following modules.

* `Daily Progress`_
* `Monthly Progress`_
* `Seasonly Progress`_
* `Statistical Scores`_
* `More`_

Daily Progress
==============

The daily progress of `test`_ are listed below.


Anomaly
-------
    Have to update the code. Will do it soon.


Monthly Progress
================

The monthly progress of `test`_ are listed below.

* `Month Mean`_
* `Month Anomaly`_
* `Month Fcst Sys Error`_

These monthly progress will be automated.


.. compute_month_mean:

Month Mean
-----------

The word *Mean* means average of the data. The average will be taken over the month time axis is called month mean.

The below script *compute_month_mean.py* should explain more how we are implementing monthly mean and generating the nc files.




Month Anomaly
--------------

Hello This is math test. Remove me ! :math:`a^2 + b^2 a\_b = c^2`.

.. math::

   (a + b)^2 = a^2 + 2ab + b^2

   (a - b)^2 = a^2 - 2ab a\_b + b^2

Anomaly means the difference between the model analysis and climatology.

Monthly Anomaly : Take the difference between the model analysis data of the particular month and the climatology data of the corresponding month.

Anomaly = Analysis - Climatology

The below script *compute_month_anomaly.py* should explain more how we are implementing monthly anomaly and generating the nc files.





More
====

More utilities will be added and optimized in near future.

