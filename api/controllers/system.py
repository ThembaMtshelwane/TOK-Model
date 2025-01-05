import numpy as np

def best_impulse_response():
    # Simulating computation of the best impulse response
    impulse_response = [1, 2, 3, 4, 5]
    return impulse_response


def convolution(input_array, impulse_response):
    """
    Computes the convolution of an input array with an impulse response.

    Args:
        input_array (list): The input array (signal).
        impulse_response (list): The impulse response array.

    Returns:
        list: The result of the convolution.
    """
    # Perform the convolution using numpy
    result = np.convolve(input_array, impulse_response, mode='full')
    return result.tolist()