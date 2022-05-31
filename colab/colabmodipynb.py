#!/usr/bin/env python

# Modify a scico Jupyter notebook example to enable running it on Google
# Colab. Usage is
#  python colabmodipynb.py <src-path> <dst-path>

import json
import sys


def first_code_cell(path):
    """Get the first code cell in a Jupyter notebook."""
    with open(path, "r", encoding='utf-8') as fp:
        d = json.load(fp)

    match = False
    for idx, cell in enumerate(d["cells"]):
        if cell["cell_type"] == "code":
            match = True
            break

    if match:
        return cell["source"]
    else:
        return []


def extra_dependencies(path):
    """Get a list of extra dependencies for a Jupyter notebook."""

    cell = first_code_cell(path)

    depend = []
    for line in cell:
        if "xdesign" in line:
            depend.append("xdesign")
        if "import ray" in line:
            depend.append("ray")
        if "scico.ray" in line:
            depend.append("hyperopt")
            depend.append("ray[tune]")
        if "radon_astra" in line:
            depend.append("astra-toolbox")
        if "colour_demosaicing" in line:
            depend.append("colour_demosaicing")

    return sorted(list(set(depend)))


def prepend_first_code_cell(srcpth, dstpth, prepend):
    """Prepend a list of strings to the first code cell in a Jupyter notebook.
    """
    with open(srcpth, "r", encoding='utf-8') as fp:
        d = json.load(fp)

    match = False
    for idx, cell in enumerate(d["cells"]):
        if cell["cell_type"] == "code":
            match = True
            break

    if match:
        cell["source"] = prepend + cell["source"]

    with open(dstpth, "w", encoding='utf-8') as fp:
        json.dump(d, fp, indent=1, ensure_ascii=False)



srcpth = sys.argv[1]
dstpth = sys.argv[2]

prepend = [
    '# This scico project Jupyter notebook has been automatically modified\n',
    '# to install the dependencies required for running it on Google Colab.\n',
    '# If you encounter any problems in running it, please open an issue at\n',
    '#   https://github.com/lanl/scico-data/issues\n',
    '\n',
    '!pip install git+https://github.com/lanl/scico\n',
]

extradep = extra_dependencies(srcpth)
if extradep:
    prepend.append('!pip install ' + ' '.join(extradep) + '\n')

prepend.append('\n')

prepend_first_code_cell(srcpth, dstpth, prepend)
