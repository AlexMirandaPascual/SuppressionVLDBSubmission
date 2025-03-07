# Experiments on Suppression

For the submission at VLDB 2025 of

*On the Adverse Effect of Suppression in Differential Privacy*
by Àlex Miranda-Pascual, Javier Parra-Arnau and Thorsten Strufe

## Overview 

Each folder contains an independent experiment. These are:

* `NoisyAverage` contains our experiment on the mean computation with NoisyAverage.
* `ReportNoisyMax` contains our experiment on the mode computation with report noisy max and the exponential mechanism. 
* `Clustering` contains our experiment on clustering.
* `PrivacyBound` contains the code that checks whether the empirical result we obtain match our theorized values for Theorem 4.3.
* `PrivacyBoundPlots` contains the code that generates Figures 1 and 74 of our submission. 

Each folder has a respective README file that explains the details of each experiment. 

We also include the long version of our submission here for the process of submission.

All code is written in Python 3.8.20.