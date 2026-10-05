# Neural EEG Interface

A software engineering residency project at INFANT Research Centre, UCC. The aim
is to build a web interface for neonatal EEG preprocessing and quantitative
feature extraction using the existing
[NEURAL Python feature set](https://github.com/BrianMur92/NEURAL_py_EEG_feature_set).

## Current status

This repository currently contains the development dependency configuration and
three initial pytest tests. A clean Python 3.14.7 environment was installed and
passed `pip check` and all three tests on Windows on 5 October 2026.

Earlier work investigated compatibility against a Python 3.11 reference
environment. The application integration and web interface are still to be built.

## Development setup

Install **Python 3.14.7** and **Git**, then clone this repository. From its root
directory, run these commands in Windows PowerShell:

```powershell
py -3.14 --version
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -m pytest
```

The version check should report Python 3.14.7. Use a new environment directory if
`.venv` already contains an existing environment, and adjust the paths accordingly.
Installation requires network access to package sources and the upstream NEURAL
repository. Expected check results are `No broken requirements found.` and
`3 passed`.

`requirements.txt` pins the direct runtime dependencies, including NEURAL at
commit `78c94258e4a3e6504e469f418443c78926e1a6be`.
`requirements-dev.txt` also installs pytest. Transitive dependencies are not fully
locked. pandas 2.3.3 is retained because a pandas 3 compatibility issue was found
in the tested NEURAL preprocessing path.

## Tests

- `tests/test_imports.py` checks that the main dependencies and NEURAL modules
  import successfully.
- `tests/test_preprocessing.py` uses synthetic two-channel signals to check
  256-to-64 Hz downsampling, output dimensions and preserved channel names/order.

These are initial smoke and structural regression tests. They do not cover the
complete EEG processing workflow or establish scientific validity.

## Research data

Keep real EEG recordings, participant information, credentials and confidential
research material outside version control. Use synthetic data for repository
tests. The repository includes ignore rules for common data and environment files;
those rules do not remove files already tracked by Git.

## Next steps

Agree the first supported processing workflow with the research team, build the
NEURAL integration, and develop the interface with researcher feedback.
