:orphan:

.. default-role:: math

Mathematics
===========

This package implements Latin Hypercube Sampling (LHS) for pytest. LHS is a statisical method for generating samples from multi-dimensional sample spaces.
LHS works as follows:

#. Divide the range of each variable into N equally sized intervals.
#. Select M samples (which are N-tuples, where the `i` th value is sampled from the `i` th variable), by randomly choosing a strata for each variable and randomly sampling within it, ensuring such that for any two samples, the `i` th value of the first sample is not sampled from the same strata as the `i` th value of the second sample. 

This is called Latin Hypercube Sampling because the samples are arranged in a Latin Hypercube, a higher dimensional generalisation of a Latin square -
a square grid where each row and each column contains exactly one sample. The benefit of LHS is that, while it generates samples that are "less random" than 
random sampling, it ensures that the samples are more evenly distributed throughout the sample space - since M strata in each variable are represented.
.. less random is a funny idea

Application to testing
======================
LHS is typically used within the design of computer experiments, for example with Monte Carlo simulation, often with continuous variables. In this package, the goal
is instead to use For unit testing, this
is often not the case, where parameter spaces are already discrete. Therefore, the first step is unnecessary, provided there are N possible parameter values for
each parameter. This condition will be softened later. We also do not need to sample within the second step, as each strata now only contains a single value.

 For this use case, it makes sense to take N samples instead of 