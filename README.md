# Portfolio optimisation with multi-objective genetic algorithms

This **repository** includes all the files and scripts to reproduce the project of investment portfolio optimisation.

### Requisites

- `R` is required for reproducing the analysis. Further documentation [here](https://www.r-project.org).
  - The `eaf` library is needed to produce the algorithms' comparison plots. More information [here](https://mlopez-ibanez.github.io/eaf/).
- `Python` is required for reproducing the analysis. Further documentation [here](https://www.python.org/).
  - The `pandas` package is required for data manipulation and to get real time data.
  - The `datetime` package is used for selecting time frames when downloading real market data.
  - The `numpy` package is required for mathematical formulations.
  - The `pymoo` package is required. This is the package used specifically for modeling and solving the applied genetic algorithms.
  - The `scipy` package is used for performing statistical tests.
  - The `lzma` package is required for formatting the results correctly for the `eaf` library.

## Real market data

The financial data used as input for the two algorithms has been sourced from [Yahoo Finance](https://finance.yahoo.com/).

The `stocks_info.py` inside `code` folder contains the method utilized to download real market data of $20$ stocks considered important inside the UK.

The `stocks_info.py` file performs the following:

- Using the `datetime` package, the stocks data was delimited between $5$ October $2019$ and $5$ October $2022$.
  
- The risk free rate was setted to $0.00$. The returns were annualized and the sharpe ratio was computed as a percentage delta and the volatility based on $250$ trading days.
  
- Finally the formatted data is exported to `stocks_info.csv` inside `data`.
  

Both `alg1.py` and `alg2.py` source to the `stocks_info.csv` dataset as the source of market information employed as input.

## Reproducibility

In order to reproduce the analysis, it is necessary to follow the subsecuent steps:

1. Run both algorithms
2. Run the analysis and creation of plots

### Run both algorithms

As this work icompare two portfolio optimisation algorithms with different settings, the user should run both algorithms. The order in which they are performed is unimportant.

**Algorithm 1**
Algorithm contained inside `alg1` folder within `code`. `alg1` contains two files:

- `alg1.py`: stores the complete implementation of the genetic algorithm and exportation of results.
- `algorithm_1_results_formating.py`: formats the first algorithm's results.

For *running* and *saving* the findings of the **first algorithm** first excecute `alg1.py` for running the genetic algorithm and exporting results. Then, run `algorithm_1_results_formatin.py`, for generating an exported dataset of the results saved inside the `alg1` folder within `results`.

**Algorithm 2**

Algorithm contained inside `alg2` folder within `code`. `alg2` contains two files:

- `alg2.py`: stores the complete implementation of the genetic algorithm and exportation of results.
- `algorithm_2_results_formating.py`: formats the second algorithm's results.

For *running* and *saving* the findings of the **second algorithm** first excecute `alg2.py` for running the genetic algorithm and exporting results. Then, run `algorithm_2_results_formatin.py`, for generating an exported dataset of the results saved inside the `alg2` folder within `results`.

### Run the analysis and creation of plots

Results from both algorithms are stored inside `results` folder, divided correspondingly into two subfolders: `alg1` and `alg2`.
For comparing the GA's open the `analysis` folder inside `code`, there will be three files:

- `algs_boxplots.R`: creates a box plot comparing the objective values of the two GA's. Exports `boxplot.pdf` to `figures` folder.
- `algorithm_comparison_figures.R`: creates a `eaf` plot for each of the two algorithms and a `eaf` comparison plot between both algorithms. Exports `A1.pdf`, `A2.pdf` and `A1_vs_A2.´df` to `figures` folder.
- `analysis_test.py`: performs a Mann-Whitney U Test between the two algorithms' results. Exports `mann_whitney_tests.txt` to `results`.

## Report

Report available as `report.pdf` inside `report` folder. To replicate it please download and unzip `report.zip`, then compile it using `LaTex`. Due to `report.pdf`'s high resolution plots, there is a high probability of user issues when opening the file. For this reason, a compressed version can be found [here](https://drive.google.com/file/d/1lL_af-fXmmXB5kK0krifOHRDak6agRuN/view?usp=sharing).
