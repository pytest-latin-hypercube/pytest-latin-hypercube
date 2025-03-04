

.. default-role:: math

Mathematics
===========
In the context of statiscal sampling, a Latin square is an `N` by `N` grid containing `N` sample positions such that each row and each column contains exactly one sample.
An example of a 4 by 4 Latin square is here:

.. list-table::
    :widths: 30, 30, 30, 30
    :header-rows: 0

    * - 
      - 
      - X
      - 
    * - X
      - 
      - 
      - 
    * -
      -
      -
      - X
    * -
      - X
      -
      -

A Latin hypercube is a generalisation of a Latin square to an arbitrary number of dimensions.

This package implements Latin Hypercube Sampling (LHS) for pytest. LHS is a statisical method for generating samples from multi-dimensional sample spaces.
LHS works as follows:

#. Divide the range of each variable into N equally sized intervals.
#. Select M samples (which are N-tuples, where the `i` th value is sampled from the `i` th variable), by randomly choosing a strata for each variable and random