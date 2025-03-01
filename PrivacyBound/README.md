# Experiment on the Correctness of Theorem 4.3

**This folder contains the code to check empirically the bound of the Theorem 4.3**

For the submission at VLDB 2025 of

*On the Adverse Effect of Suppression in Differential Privacy*
by Àlex Miranda-Pascual, Javier Parra-Arnau and Thorsten Strufe

## Overview 

The code generates checks and computes the difference between the empirical value and theoretical value for multiple epsilon, m and M values. The algorithm returns CSV files with the difference. 

The code is written in Python 3.8.20.

## Installation

Requirements can be installed with the following:
```bash
pip install -r requirements.txt
```

## How to run

The result is obtained by running the specific python script:

* `FinalMaximumFunctionEps0.py`: Check and generates the CSV file containing the theoretical and empirical result and its difference of the function explained in Remark B.17 (in long version of paper) for epsilon = `0` and all `(m,M)` with granularity `0.01`.
* `FinalMaximumFunctionRange1.py`: Check and generates the CSV file containing the theoretical and empirical result and its difference of the function explained in Remark B.17 (in long version of paper) for all epsilon between `0.01` and `1.99` (step=`0.01`) and all `(m,M)` with granularity `0.01`.
* `FinalMaximumFunctionRange2.py`: Check and generates the CSV file containing the theoretical and empirical result and its difference of the function explained in Remark B.17 (in long version of paper) for all epsilon between `2` and `9.9` (step=`0.1`) and all `(m,M)` with granularity `0.01`.
* `FinalMaximumFunctionRange3.py`: Check and generates the CSV file containing the theoretical and empirical result and its difference for all epsilon between `10` and `100` (step=`1`) and all `(m,M)` with granularity `0.01` (see Remark B.17 in long version of paper).
* `FinalMaximumInverse.py`: Check and generates the CSV file containing the theoretical and empirical result and its difference of the function explained in Remark B.19 (in long version of paper) for all epsilon previously listed and `(m,M)` with granularity `0.01`.  

## Output

The first four python script each output a CSV file (`output_epsilon0`, `output_range1`, `output_range2` and `output_range3`) containing the empirical (`DiffEvol`) and hypothesized theoretical values (`HypValue`), and its difference (`Difference`=`HypValue`-`DiffEvol`). The script also outputs error messages in the terminal when:
* If the empirical maximum is obtained in a degenerate case, which we do hypothesize. 
* The difference between `HypValue` and `DiffEvol` is too large. 
* `DiffEvol` is larger than `HypValue` (up to some floating error), since we do not expect it to do either.
Our last iteration does not output many errors. It also prints the largest and smallest values of `Difference` (taking sign into consideration). 

`FinalMaximumInverse.py` outputs on the terminal if an error is reached:
* The difference between `HypValue` and `DiffEvol` is too large. 
* `DiffEvol` is larger than `HypValue` (up to some floating error), since we do not expect it to do either.
Our last iteration does not output many errors. It also prints the largest and smallest values of `Difference` (taking sign into consideration). 
* The term `L4`, which we consider to be superfluous, is actually not superfluous.
Our last iteration does not output many errors. It also prints the largest and smallest values of `Difference` (taking sign into consideration). 
Our last iteration does not output many errors. It also prints the largest and smallest values of `Difference` (taking sign into consideration). 

## Results for Paper and Time to Run

Due to the amount of computations, the time to run for all algorithms is around a day. `FinalMaximumFunctionRange1.py`,  `FinalMaximumFunctionRange2.py`, and  `FinalMaximumFunctionRange3.py` are parallelized with 64 cores. 