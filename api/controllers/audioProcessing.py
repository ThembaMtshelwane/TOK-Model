import scipy.signal as signal

def butter_lowpass_filter(data, sample_rate,  cutoff_freq=10000 ,order=4):
    """
    Applies a Butterworth low-pass filter to the input signal.

    This function filters the input signal by allowing frequencies below
    the specified cutoff frequency to pass while attenuating frequencies
    above the cutoff. The filter is implemented using a Butterworth filter 
    design with zero-phase filtering to avoid phase distortion.

    Args:
        data (list or np.ndarray): The input signal (time-series data) to be filtered.
        sample_rate (float): The sample rate of the data in Hz.
        cutoff_freq (float, optional): The cutoff frequency of the low-pass filter in Hz (default is 10000 Hz).
        order (int, optional): The order of the filter, which controls the steepness of the cutoff (default is 4).

    Returns:
        np.ndarray: The filtered signal with high-frequency components attenuated.
    """
    # Normalize the cutoff frequency with respect to Nyquist frequency
    nyquist = 0.5 * sample_rate
    normalized_cutoff = cutoff_freq / nyquist

    # Get the filter coefficients (b, a) for the Butterworth filter
    b, a = signal.butter(order, normalized_cutoff, btype='low', analog=False)

    # Apply the filter to the signal using filtfilt (zero-phase filtering)
    filtered_data = signal.filtfilt(b, a, data)

    return filtered_data