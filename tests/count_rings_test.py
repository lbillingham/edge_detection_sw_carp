import numpy as np
import count_rings as cr


def count_test_1():
    test_array = np.array([0, 1, 0])
    exp_count = 1
    obs_count = cr.count_rings(test_array)
    assert (exp_count == obs_count)

    
def count_test_2():
    test_array = np.array([0, 1, 0, 1, 0, 1, 0])
    exp_count = 3
    obs_count = cr.count_rings(test_array)
    assert (exp_count == obs_count)


def count_test_3():
    test_array = np.array([0, 1, 0, 0, 0, 1, 0])
    exp_count = 2
    obs_count = cr.count_rings(test_array)
    assert (exp_count == obs_count)

def count_test_4():
    test_array = np.array([0, 1, 1, 0, 0, 1, 0])
    exp_count = 2
    obs_count = cr.count_rings(test_array)
    assert (exp_count == obs_count)

