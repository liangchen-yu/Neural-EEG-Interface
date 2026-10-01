import numpy
import pandas
import scipy
import mne
import pyedflib

from NEURAL_py_EEG import preprocessing_EEG
from NEURAL_py_EEG import generate_all_features


def test_dependencies_import():
    assert numpy is not None
    assert pandas is not None
    assert scipy is not None
    assert mne is not None
    assert pyedflib is not None


def test_neural_modules_import():
    assert preprocessing_EEG is not None
    assert generate_all_features is not None