#test module for simple_math

import simple_math as math
import pytest

@pytest.mark.parametrize("a,b", [(1,2),(3,5),(9,4),(256,678),(886,233)])
def test_calculate(a,b):
    assert math.simple_add(a,b) == (a+b)

@pytest.mark.parametrize("a,b", [(1,2),(3,5),(9,4),(256,678),(886,233)])
def test_sub(a,b):
    assert math.simple_sub(a,b) == (a-b)

@pytest.mark.parametrize("a,b", [(1,2),(3,5),(9,4),(256,678),(886,233)])
def test_mult(a,b):
    assert math.simple_mult(a,b) == (a*b)

@pytest.mark.parametrize("a,b", [(1,2),(3,5),(9,4),(256,678),(886,233)])
def test_div(a,b):
    assert math.simple_div(a,b) == (a/b)

@pytest.mark.parametrize("x,a0,a1,a2",[(2,3,5,9)])
def test_poly1(x,a0,a1,a2):
    assert math.poly_first(x,a0,a1) == a0+a1*x

@pytest.mark.parametrize("x,a0,a1,a2",[(-3,3,5,9)])
def test_poly2(x,a0, a1, a2):
    assert math.poly_second(x,a0,a1,a2) == a0+a1*x+a2*x*x