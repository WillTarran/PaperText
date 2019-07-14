# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.1.7
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ## A notebook with Papermill parameterisation

# + {"tags": ["parameters"]}
# parameter
d_mean = 0.0
d_std = 1.0
n_bins = 10
# -

from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

# Here's a nice plot of some results

d = norm.rvs(loc=d_mean, scale=d_std, size=1000)
plt.hist(d, bins=n_bins)
