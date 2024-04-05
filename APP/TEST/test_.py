import re
import getpass
import pytest

import sys
sys.path += ['../function']

from func import *

def test_username():
    assert validate_username("Mike") == True
    assert validate_username("Mike 123") == False
    assert validate_username("") == False
    assert validate_username("Mike!") == False
    
def test_password():
    assert validate_password("Mike123!") == True
    assert validate_password("Mike123") == False
    assert validate_password("Mike!") == False
    assert validate_password("Mikedonovan") == False
    assert validate_password("!1258467924") == False
    assert validate_password("") == False
    
def test_email():
    assert validate_email("mikedonovan@dsti.com") == True
    assert validate_email("mikedonovan@dsti") == False
    assert validate_email("mikedonovan.com") == False
    assert validate_email("mikedonovancom") == False