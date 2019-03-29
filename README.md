# bfx_201903

To run this project for yourself, clone the repo from github.

Required:
- Command line tools:
    - `tree`
- conda env `bfx_201903` (containing all python / R dependencies)
    - This can be cloned in entirety using `./conda_requirements.txt` (if on linux)
        - `conda create --name bfx_201903 --file conda_requirements.txt`
    - Or constructed approximately (on unix-a-like)
        - `conda env create --name bfx_201903 --file conda_environment.yaml`
    - To activate:
        - `conda activate bfx_201903`

Warning:
- `stackr` will be installed from github during the run of `code_tools.Rmd`

Run:
- Open this R project in `rstudio`
    - `rstudio bfx_201903.RProj &`
- Open the `code_tools.Rmd` file within `rstudio`
- `knit` the document to generate the html presentation
- THIS WILL FAIL the first time you run it
    - it should fail when `rosa_testable` is imported
    - I think this is because the `python`/`reticulate` interpreter is started
    before the package is installed by `bash`/`pip`
- It should knit properly the second time you run it

Sphinx:
- The code in the section on Sphinx documentation is not run during compilation
of the presentation
- To run this, just open the repo in the command line, under the `bfx_201903`
environment, and run the mentioned commands; eg
    - `(cd rosa_cli && make docs)`

Note:
- the code is actually incorrect....
    - it works ok for a permutation of the first N natural numbers (the
      requirements for the rosalind challenge)
    - but it fails on some sequences that contain duplicated elements
    - and, although it doesn't aim to deal with non-positive numbers, it
      doesn't throw an exception for this unexpected input
