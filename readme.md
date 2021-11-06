Montone Library can be used to used to check the min from a list a by checking whether the given list is monotonic decreasing
and montononic increasing

Installation:

pip install /path/to/dist/monotone-0.1-py3-none-any.whl

Usage:

for getting the minimum by checking whether the first fue elements are monotonic decreasing and after that monotonic increasing

from montone import monotone

list  = [-2, -1, 1, 2, 3]
minimun = monotone.monotone_min(list)

For checking whether the list is montonic increasing or decreasing
use 
monotonic_increasing(list)
monotonic_decreasing(list)