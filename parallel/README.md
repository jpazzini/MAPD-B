## Threading and Parallel processing module

This module will be run in class to demonstrate and discuss basics of multithreading and parallel processing in Python.

The `threading` and `multiprocessing` standard Python modules will be used.

To illustrate the effect of Python Global Interpreter Lock (GIL) and its changes, a recent (`>= 3.10`) and possibly also an older (`<=3.9`) Python versions should be used.

The impact of threading and multiprocessing on the CPU resources will be monitored using `htop` (cross-platform interactive process viewer availabe by default in Ubuntu).

The `taskset` Unix command can be used to set the affinity of a task to a given CPU or range of CPUs, to pin threads or processes to one or more CPU cores.

### Pre-requisites

1. Clone this repo (or fetch the latest updates) 
2. Have a working environment with a Python3 interpreter (also `docker`, `venv`, `conda`, etc can be used)
