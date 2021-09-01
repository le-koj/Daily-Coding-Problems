def rotate_array(arr: list, k: int):
    """
    Given an array on N length, rotate the array rightwards by K rotations, i.e 
    shift each element to the right by K positions.
    """

    return arr[-k::] + arr[:(len(arr) - k)]
