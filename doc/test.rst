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


.. automodule:: compute_month_mean
   :members:


.. compute_month_anomaly:

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

.. automodule:: compute_month_anomaly
   :members:


.. compute_month_fcst_sys_error:

Month Fcst Sys Error
----------------------

Forecast Systematic Error means the difference between the model forecast hour data and model analysis.

This also called as *Fcst Sys Err*.


Month Fcst Sys Error : Take the difference between the model forecast hour data of the particular month and the model analysis data of the same month.

Fcst Sys Err = Model Fcst Hour Data - Model Analysis

The below script *compute_month_fcst_sys_error.py* should explain more how we are implementing monthly fcst sys err and generating the nc files.

.. automodule:: compute_month_fcst_sys_error
   :members:


Seasonly Progress
=================

The seasonly progress of `test`_ are listed below.

* `Season Mean`_
* `Collect Season Fcst Rainfall`_
* `Region Statistical Score`_
* `Season Statistical Score Spatial Distribution`_

These season progress will be automated with respect to the given season as input in the configure.txt.

The word *season* means the consecutive months.

For eg: JJAS contains June, July, August, September.


.. compute_season_mean:

Season Mean
------------

The word *Mean* means average of the data. The average will be taken over the season time axis is called season mean.

The below script *compute_season_mean.py* should explain more how we are implementing seasonly mean and generating the nc files.


.. automodule:: compute_season_mean
   :members:


.. collect_season_fcst_rainfall:

Collect Season Fcst Rainfall
----------------------------

This script *collect_season_fcst_rainfall.py* should collect the whole season forecast hourly rainfall with respect to the hours of season.
Finally it should create the nc files for every fcst hours that contains the fcst rainfall with needed time axis to compute the further process.


.. automodule:: collect_season_fcst_rainfall
   :members:


.. compute_region_statistical_score:


Region Statistical Score
------------------------

The below script *compute_region_statistical_score.py* should compute the various statistical scores regional wise and make the nc files.

Here regions are 'Central India', 'Peninsular India', etc. That is region name/variable defines the latitude and longitude range.


.. automodule:: compute_region_statistical_score
   :members:


.. compute_season_stati_score_spatial_distribution:


Season Statistical Score Spatial Distribution
---------------------------------------------

The below script *compute_season_stati_score_spatial_distribution.py* should compute the various statistical scores w.r.t each & every lat, lon
location of particular region.

.. automodule:: compute_season_stati_score_spatial_distribution
   :members:



test Plots
===============

The test plots of `test`_ are listed below.

* `Winds Plots`_
* `Iso Plots`_
* `Statistical Score Bar Plots`_
* `Statistical Score Spatial Distribution Plots`_


.. generate_winds_plots:

Winds Plots
-----------

Generate the vector plots using U and V component of the wind data.
The below script *generate_winds_plots.py* should generates the wind plots and save it as either png or jpg or svg in the suitable directory for month and season wise.

.. automodule:: generate_winds_plots
   :members:


.. generate_iso_plots:

Iso Plots
---------

Generate the iso plots for the iso variables which are all set in the 'vars.txt' file.


The below script *generate_iso_plots* should generates the following kind of plots.

* iso line
* iso fill
* iso fill line

Finally save the generated iso plots as either png or jpg or svg in the suitable directory for month and season wise.

.. automodule:: generate_iso_plots
   :members:



.. generate_statistical_score_bars:

Statistical Score Bar Plots
---------------------------

The script *generate_statistical_score_bars.py* should generate the bar plots w.r.t the statistical scores for different region & fcst hours.
Finally save the generated bar plots as either png or jpg or svg in the suitable directory for season wise.

.. automodule:: generate_statistical_score_bars
   :members:


.. generate_stati_score_spatial_distribution_plots:

Statistical Score Spatial Distribution Plots
--------------------------------------------

The script *generate_stati_score_spatial_distribution_plots.py* should generate the iso fill plots w.r.t the statistical scores for different fcst hours.
Finally save the generated iso fill plots as either png or jpg or svg in the suitable directory for season wise.


.. automodule:: generate_stati_score_spatial_distribution_plots
   :members:




Statistical Scores
==================

Contigency Table & Related Statistical Scores
---------------------------------------------

The module *ctgfunction.py* should helps to calculate the contigency table and its related statistical scores.

For eg : Threat Score, Bias Score, Proabability of detection and more.

.. automodule:: ctgfunction
   :members:


More
====

More utilities will be added and optimized in near future.

