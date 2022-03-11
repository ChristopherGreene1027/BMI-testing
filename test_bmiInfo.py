from bmiInfo import *
import pytest 

def n_test():
    bmi_calc(6, 3, 180)

def geninputs():
    inputs = ["6", "3", "180"]

    for item in inputs:
        yield item

GEN = geninputs()

def test_n_test(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))

    assert n_test() == 1



def n_test():
    bmi_calc(5, 6, 200)

def geninputs():
    inputs = ["6", "3", "180"]

    for item in inputs:
        yield item

GEN = geninputs()

def test_n_test(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))

    assert n_test() == 1

