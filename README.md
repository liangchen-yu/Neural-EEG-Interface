# Neural-EEG-Interface

An early-stage software engineering residency project at INFANT Research Centre,
UCC. The aim is to make neonatal quantitative EEG preprocessing and feature
extraction accessible through a researcher-facing web application using
[NEURAL](https://github.com/BrianMur92/NEURAL_py_EEG_feature_set), an external
research dependency. This application repository is separate from upstream NEURAL.

Development focuses on the pinned NEURAL Python implementation. Changes to its
scientific behaviour require careful consideration. The older MATLAB qEEG
implementation remains historical and algorithm reference material.
`downsample_open_eeg` is a separate dataset-preparation utility; its CSV/XZ workflow
is not currently an application requirement.

## Project status

- **Completed:** a reproducible Python 3.11.6 reference environment, initial pytest
  tests, Python 3.14 compatibility investigations, and a clean Python 3.14.7
  environment installation and test run on Windows on 5 October 2026.
- **In progress:** defining the supported processing workflow and its inputs and
  outputs with the research team.
- **Planned:** application-owned NEURAL integration, structured results, and a web
  interface/backend. No frontend, backend, or API is implemented here yet.
- **Known limitations:** IBI/burst features require an external detector.
  Scientific equivalence with MATLAB and clinical validity have not been
  established. The application is not production-ready.

## Development setup — Windows PowerShell

The default development configuration uses **Python 3.14.7**.
`requirements.txt` pins the direct runtime dependencies;
`requirements-dev.txt` includes them and adds pytest. NEURAL is pinned to commit
`78c94258e4a3e6504e469f418443c78926e1a6be`.

You need Python 3.14.7, Git, access to this repository, and network access to public
package sources and the upstream NEURAL repository.

For a new checkout:

```powershell
git clone https://github.com/INFANT-Dev-Projects/neural-eeg-ui.git
Set-Location neural-eeg-ui
```

From the repository root, create a new virtual environment. Confirm both version
checks report Python 3.14.7 when reproducing the tested configuration:

```powershell
py -3.14 --version
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -m pytest
```

These commands assume `.venv` does not already contain another environment. For
an existing checkout, use a new environment path if necessary. The explicit Python
path selects this environment without activation. Do not commit the environment.

Expected results are `No broken requirements found.` and `3 passed`.
Transitive dependencies and build tooling are not fully locked.

## Verification and test scope

On **5 October 2026**, a previously unused environment directory was created with
Python 3.14.7 on Windows. Installation from this working checkout's
`requirements-dev.txt` succeeded, using pip's package cache where available.
`pip check` reported no broken requirements and pytest reported **3 passed in
6.46 seconds**, with no warnings shown. This was a fresh environment check in an
existing working checkout, not a fresh-clone test of the Python 3.14 configuration.

There are three tests across two files:

- `tests/test_imports.py`: two smoke tests covering important dependencies and
  NEURAL preprocessing and feature-generation module imports.
- `tests/test_preprocessing.py`: one structural regression test using deterministic
  synthetic signals. It checks 256-to-64 Hz downsampling, a 640-by-2 output for ten
  seconds of two-channel input, and preserved channel names/order.

The suite does not verify EDF loading, artefact handling, the separate low-pass
filter, or feature extraction. It does not establish scientific or clinical
validity.

Python 3.11.6 remains the historical comparison environment. Its setup was
previously reproduced from a fresh clone with a pinned Git installation of NEURAL,
a successful dependency check, and three passing tests. Its previous dependency
configuration is retained in Git history.

## Earlier Python 3.14 compatibility investigation

Earlier investigation exercised EDF loading through MNE, synthetic preprocessing
and artefact handling, 30 Hz low-pass filtering, 256-to-64 Hz downsampling,
selected non-IBI features, and pytest. Comparisons with the Python 3.11 reference
using identical inputs found matching preprocessing shapes and artefact-stage
values, with filtering/downsampling differences around floating-point precision.
Most compared non-IBI outputs were close; small numerical differences occurred
mainly in connectivity outputs. This is engineering compatibility evidence,
not scientific equivalence.

- A pandas 3 read-only-array compatibility issue was identified in the tested
  NEURAL preprocessing path. pandas 2.3.3 worked in the tested configuration and
  is pinned for development.
- The tested EDF-reading workflow uses MNE. NEURAL's legacy pyEDFlib writing helper
  uses `sample_rate` rather than `sample_frequency` and did not work unchanged
  with the tested modern pyEDFlib version.
- pyEDFlib 0.1.36 worked in the Python 3.11 reference environment but could not be
  installed cleanly in the tested Python 3.14 setup. The current configuration
  uses pyEDFlib 0.1.42.

The earlier comparison scripts and numerical result files are not currently
tracked in this application repository.

## Research-data safety

Do not commit patient, participant, clinical, confidential, or proprietary research
material, credentials, or environment secrets. Real EEG recordings must remain
outside version control. EDF/BDF files regardless of extension case, `data/`,
`uploads/`, `results/`, NumPy archives (`*.npz`), and local `.env`/`.env.*` files are
ignored. Keep research inputs and generated outputs in designated ignored locations;
ignore rules do not remove files already tracked by Git. Tests should use clearly
identified synthetic data.

## Proposed next steps

Define the first supported workflow with the research team, identify its NEURAL
inputs and outputs, and implement a small application-owned integration around
it. Add tests that protect that supported workflow and develop the researcher-facing
interface iteratively with feedback.

Python and pytest are already in use. Flask is the currently preferred web framework;
the application architecture has not been implemented or finalised. A proposed
approach is to keep NEURAL processing callable through ordinary Python functions
so that it can be tested independently of the web interface.
