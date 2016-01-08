# -*- coding: utf-8 -*-
"""
A really dumb test to check we can import things properly
Created on Fri Jan  8 10:35:31 2016

@author: laurence
"""

import dumb_funcs
from numpy.testing import assert_allclose

def test_a_dumb_func():
    """
    Make sure we can connect the tests up to the code

    Parameters
    ----------
    None

    Returns
    -------
    1

    Side Effects
    ------------
    Tests `dumb_func`
    """
    expected = 1
    got = dumb_funcs.a_dumb_func()
    assert_allclose(got, expected)
