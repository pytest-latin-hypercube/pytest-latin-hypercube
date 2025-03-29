

.. default-role:: math

Mathematics
===========
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

A *Latin hypercube* is a generalisation of a Latin square to grid of an arbitrary number of dimensions, where each axis contains exactly one sample. Within the context of statistical sampling each dimension is drawn from a continuous distribution. Each dimension is then divided into `N` equally sized groups, which forms the hypercube. `N` sample strata are then selected, such that the Latin property is satisfied. Finally, samples are drawn from each of the selected strata, either randomly or deterministically, for example by taking the midpoints (?? Verify this). This sampling strategy is known as Latin Hypercube Sampling (LHS).

There are many benefits of using a LHS approach, but within this project there are two which are the most important. Firstly, LHS allows better coverage than a completely random sampling strategy. This is incredibly important in contexts where every sample is expensive, such as in the context of software testing. Secondly, as the dimension of our space increases, the number of samples necessary to "completely cover" the space grows exponentially (?? better wording). For example, if we chose to sample from some set `S^K`, and we chose to subdivide each axis `S` into `N` values, then we would have `N^K`strata. With a Latin Hypercube Sampling strategy, we would only sample `N` times, regardless of the dimension `K`. Latin Hypercube Sampling therefore allows the exploration of high dimensional spaces without excessively sampling. (?? Definitely worth expanding here)

In order to apply the concept of Latin Hypercube Sampling to parametrised software testing, two generalisations are helpful. Firstly, software testing requires the functions tested to have a finite number of parameters and every test run checks a function given a specific realisation of these parameters. Since there exist a finite number of test runs, (?? Need to use specific language when referring to the test run, the test itself, and each individual element of each test) the parameter space to be sampled over is discrete, as opposed to continuous. The benefit of this is that there is no need to divide the space into strata and sample them, as the natural choice is to now include every discrete value into its own strata (?? fix language above to call this substrata I think). 
