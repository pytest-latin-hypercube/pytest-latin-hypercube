

.. default-role:: math

===========
Mathematics
===========

Latin Hypercube Sampling
------------------------

In the context of statistical sampling, a Latin square is an `N` by `N` grid containing `N` sample positions such that each row and each column contains exactly one sample.
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

A *Latin hypercube* is a generalisation of a Latin square to grid of an arbitrary number of dimensions, where each axis contains exactly one sample. This property, that every axis contains a single sample, is called the Latin property. Within the context of statistical sampling it is assumed that each dimension is drawn from a continuous distribution. Each dimension is then divided into `N` equally sized groups, which forms the hypercube. `N` sample strata are then selected, such that the Latin property is satisfied. Finally, samples are drawn from each of the selected strata randomly. This sampling strategy is known as Latin Hypercube Sampling (LHS).

Benefits of Latin Hypercube Sampling
------------------------------------------------

There are many benefits of using a Latin hypercube sampling approach, but within this project there are two which are the most important. Firstly, Latin hypercube sampling is a *space-filling design*, a design that seeks to uniformly fill a bounded region :cite:p:`lin2015latin`. For each dimension, the number of observations `N` is equal to the number of strata that the dimension is divided into - and every strata is sampled exactly once. This clearly allows better coverage than a completely random sampling strategy, which is not guaranteed to sample any given strata of a given dimension. This is incredibly important in contexts where every sample is expensive, such as in the context of software testing, where every sample corresponds to a test run. This is because in contexts where every sample is expensive, the samples should be chosen to maximise the information gained from each sample. Practically, this means that samples should be chosen to cover as much of the space as possible, and to avoid clustering of samples.

Secondly, as the dimension of our space increases, the number of samples necessary to "completely cover" the space grows exponentially (?? better wording). For example, if we chose to sample from some set `S^K`, and we chose to subdivide each axis `S` into `N` values, then we would have `N^K` strata. With a Latin Hypercube Sampling strategy, we would only sample `N` times, regardless of the dimension `K`. Latin Hypercube Sampling therefore allows the exploration of high dimensional spaces without excessively sampling. (?? Definitely worth expanding here)

Generalisation to Software Testing
------------------------------------------------

In order to apply the concept of Latin Hypercube Sampling to parametrised software testing, two generalisations are helpful. Firstly, software testing requires the functions tested to have a finite number of parameters and every test run checks a function given a specific realisation of these parameters. Since there exist a finite number of test runs, (?? Need to use specific language when referring to the test run, the test itself, and each individual element of each test) the parameter space to be sampled over is discrete, as opposed to continuous. The benefit of this is that there is no need to divide the space into strata and sample them, as the natural choice is to now include every discrete value into its own strata (?? fix language above to call this substrata I think). 


.. bibliography::