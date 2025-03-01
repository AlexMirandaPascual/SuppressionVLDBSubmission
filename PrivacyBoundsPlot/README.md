# Code to Generate the Plots on the Privacy Parameters of Theorem 4.3

**This folder contains the code to generate the plots for our bound of the Theorem 4.3**

For the submission at VLDB 2025 of

*On the Adverse Effect of Suppression in Differential Privacy*
by Àlex Miranda-Pascual, Javier Parra-Arnau and Thorsten Strufe

## Overview 

The code generates the plots for our paper.

The code is written in Python 3.8.20.

## Installation

Requirements can be installed with the following:
```bash
pip install -r requirements.txt
```

## How to run

The result is obtained by running  `privacyboundsplot.py`.

## Output

The plots returned are: 

* `plots_eps_suppression_[epsilon].pdf` for `epsilon=0,0.25,0.5,0.75,1,2`. It consist the plot of epsilon^S with respect to m and M for the chosen value of `epsilon`. Used in Figure 1 of the submission paper. 
* `plot_simplied_areas.pdf`. It is the plot that shows the areas where the expression simplifies. It is shown in Figure 74 of the long version of the submission paper.

## Results for Paper and Time to Run

The time to run is as couple seconds. 