'''
Assignment 7
Author: Sanittawan Tan 
'''
import improved_smallest_factor as isf

def test_improved_smallest_factor():
    '''
    Test case for smallest_factor function when the function should work
    '''
    assert isf.improved_smallest_factor(2) == 2

def test_improved_smallest_factor2():
    '''
    Test case for smallest_factor function when the function should work
    '''
    assert isf.improved_smallest_factor(10) == 2

def test_improved_smallest_factor3():
    '''
    Test case for smallest_factor function when the function should work
    '''
    assert isf.improved_smallest_factor(4) == 2

def test_improved_smallest_factor4():
    '''
    Test if inpiut is zero
    '''
    assert isf.improved_smallest_factor(0) == \
            None, "Zero is not a positive integer"

def test_improved_smallest_factor5():
    '''
    This test will throw a TypeError for -1 as it is a complex type
    '''
    assert isf.improved_smallest_factor(-1) == \
            None, "Expected a positive integer. Got negative"

def test_improved_smallest_factor6():
    '''
    Test when input is the wrong type
    '''
    assert isf.improved_smallest_factor(0.5) == \
            None, "Expected a positive integer, Got a float"

def test_improved_smallest_factor7():
    '''
    Test large prime number
    '''
    assert isf.improved_smallest_factor(83) == \
            83, "Wrong answer"

def test_improved_smallest_factor8():
    '''
    Test large non-prime number
    '''
    assert isf.improved_smallest_factor(150) == \
            2, "Wrong answer"