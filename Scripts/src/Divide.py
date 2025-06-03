
#Divide.py

"""! 
@brief Example Python program with Doxygen style documentation
@author lufer (lufer@ipca.pt)
@date June 2, 2025
"""


##
# @mainpage Doxygen Example Project for AdTrans Project
#
# @section description_main Description
# An example Python program demonstrating how to use Doxygen style comments for
# generating source code documentation with Doxygen.
#
# @section notes_main Notes
# - Add special project notes here that you want to communicate to the user.
#
# Copyright (c) 2025 IPCA-ES-lufer.  All rights reserved.


#Functions

def divide_unsafe(a, b):
    """!Divides a by b with no error protection.

    @param a   First value.
    @param b   Second value.
    
    @return    the division.
   
    """
 
    return a / b
    
    
#----------------------------------


def safe_divide(a, b):
    """
    Divides a by b with error protection.

    Args:
        a (float or int): Numerator
        b (float or int): Denominator

    Returns:
        float: The result of the division

    Raises:
        TypeError: If inputs are not int or float
        ZeroDivisionError: If b is zero
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers (int or float).")
    
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")

    return a / b

#----------------------------------

def divide(a, b):
    """!Divides a by b with error protection.

    @param a   First value (numerator).
    @param b   Second value (denominator).
    @return    The result of division, or a string describing the error.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero."
    except TypeError:
        return "Error: Inputs must be numbers."