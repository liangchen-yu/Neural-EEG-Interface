import numpy as np
import pandas as pd

from NEURAL_py_EEG import preprocessing_EEG


def test_downsample_256_to_64():
    fs = 256
    fs_new = 64
    duration_seconds = 10

    number_of_samples = fs * duration_seconds
    t = np.arange(number_of_samples, dtype=np.float64) / fs

    data = pd.DataFrame({
        "channel_1": np.sin(2 * np.pi * 5 * t),
        "channel_2": np.sin(2 * np.pi * 10 * t),
    })

    downsampled_data, returned_fs = preprocessing_EEG.signal_downsample(
        data,
        fs,
        fs_new,
    )

    assert returned_fs == 64
    assert downsampled_data.shape == (640, 2)
    assert list(downsampled_data.columns) == [
        "channel_1",
        "channel_2",
    ]