# Discovering Clusters of Users

A narrative workflow for collecting Tweets associated with a particular topic, and using some of the associated data to discover groups of similar users.

## Installation

We have provided both a `clustering_requirements.txt` file and a conda environment file for Anaconda users.

If you use anaconda, you can create an environment as such:

```
conda env create -f clustering_users_conda_env.yml
source activate clustering_users_example
```

Otherwise, use you favorite Python >=3.5 virtual environment and install via pip:

```
pip install -r requirements.txt
```

You can start a Jupyter notebook from within the virtual environment and load the notebook `clustering-users.ipynb`. If you use Anaconda environments frequently, you can use the nbconda extension which will detect your conda environments and allow you to switch python kernels within a notebook.
