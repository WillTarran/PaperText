import papermill as pm
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.exporters import export, HTMLExporter
import yaml
from os import path
from sys import argv
from subprocess import run

in_file = argv[1]
param_file = argv[2]

f_path, f_name = path.split(in_file)
f_root, f_ext = path.splitext(f_name)
nb_out = path.join(f_path, f_root + '_processed.ipynb')
html_out = path.join(f_path, f_root + '_processed.html')

if (f_ext == '.py' and not path.exists(path.join(f_path, f_root + '.ipynb'))):
    jupytext_call = ['jupytext', '--to', 'notebook', in_file]
    run(jupytext_call)

in_file = path.join(f_path, f_root + '.ipynb')

with open(param_file, 'r') as f:
    p = yaml.safe_load(f)

# inject params
nb = pm.execute_notebook(in_file, nb_out, parameters=p)
pp = ExecutePreprocessor()
pp.preprocess(nb, resources={'metadata': {'path': './'}})
html, resources = export(HTMLExporter, nb)
with open(html_out, 'w') as f:
    f.write(html)

print(f'html written to {html_out}')
