# Neural-EEG-Interface

An early-stage software engineering residency project at INFANT Research Centre,
UCC. The aim is to make neonatal quantitative EEG preprocessing and feature
extraction accessible through a web application using
[NEURAL](https://github.com/BrianMur92/NEURAL_py_EEG_feature_set), an external
research dependency. This application repository is separate from upstream NEURAL.

## Project status

- **Completed:** a Python 3.11.6 reference environment, initial pytest tests, and
  compatibility investigations using Python 3.14.7.
- **In progress:** documentation and reproducibility preparation for shared development.
- **Planned:** a web interface, backend, independent NEURAL integration/service
  layer, and structured results. No frontend, backend, or API is implemented here yet.
- **Known limitations:** IBI/burst features are unavailable without the external
  burst detector. Scientific equivalence with MATLAB and clinical equivalence have
  not been established. The project is not production-ready.

## Reference environment and tests

`requirements.txt` records the Python 3.11.6 reference dependencies, not the final
Python 3.14 configuration. NEURAL is pinned to commit
`78c94258e4a3e6504e469f418443c78926e1a6be`.

With Python 3.11.6 and Git installed, run from the repository root in Windows
PowerShell. Confirm the selected interpreter reports 3.11.6:

```powershell
py -3.11 --version
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pytest
```

Installation requires access to public package sources and the upstream Git
repository. `requirements-dev.txt` includes the reference dependencies and pytest.
Transitive dependencies and build tooling are not fully locked. The existing local
environment uses an editable NEURAL checkout; fresh installation from the pinned
Git requirement remains a reproducibility check to complete.

There are three tests across two files: two import smoke tests in
`tests/test_imports.py`, and a structural downsampling regression test in
`tests/test_preprocessing.py`. The latter uses deterministic synthetic signals to
check 256-to-64 Hz conversion, output dimensions, and channel names. It does not
test EDF loading, artefact handling, the separate low-pass filter, or feature
extraction. The suite has passed in the tested Python 3.11.6 and 3.14.7 environments.

## Python 3.14 compatibility summary

Python 3.14.7 is the modern candidate runtime. Investigations exercised EDF loading
through MNE, preprocessing and artefact handling on deterministic synthetic data,
30 Hz low-pass filtering, 256-to-64 Hz downsampling, selected features, and pytest.
Comparisons using byte-identical input found matching preprocessing shapes and
artefact-stage values, with filtering/downsampling differences around floating-point
precision. Most non-IBI features matched closely; small differences occurred mainly
in connectivity features. This is engineering compatibility evidence, not scientific
or clinical equivalence.

- pandas 3.0.x exposed a read-only-array problem in NEURAL preprocessing; pandas
  2.3.3 worked in the tested Python 3.14 pipeline.
- The tested EDF-reading workflow uses MNE and worked with modern pyEDFlib installed.
  NEURAL's legacy EDF-writing helper instead uses `sample_rate` rather than
  `sample_frequency` and does not work unchanged with current pyEDFlib.
- pyEDFlib 0.1.36 worked in the Python 3.11 reference environment but could not be
  installed cleanly in the tested Python 3.14 environment.

The comparison scripts/results and complete candidate dependency configuration are
not currently tracked here. Detailed evidence can be documented in
`docs/COMPATIBILITY.md` once the supporting scripts/results are tracked.

## Research-data safety

Do not commit patient, participant, clinical, confidential, or proprietary research
material, credentials, or environment secrets. Real EEG recordings must remain
outside version control. EDF/BDF files regardless of extension case, `data/`,
`uploads/`, `results/`, NumPy archives (`*.npz`), and local `.env`/`.env.*` files are
ignored. Keep research inputs and generated outputs in designated ignored locations;
ignore rules do not remove files already tracked by Git. Tests should use clearly
identified synthetic data.

## Proposed next steps

Flask is the current proposed backend framework, subject to team confirmation.
The proposed NEURAL service layer should remain independent of Flask, with
processing logic outside route functions.

Next steps are to verify a fresh dependency installation, record a reproducible
Python 3.14 configuration, expand synthetic preprocessing and non-IBI feature tests,
and then implement the minimal service layer and agreed web interface/backend.
