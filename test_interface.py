
import pytest


@pytest.mark.parametrize("LDL, expected", [
    [170, "High"],
    [190, "Very High"],
    [130, "Borderline High"],
    [120, "Normal"]
    ])
def test_analyze_LDL(LDL, expected):
    from interface import analyze_LDL
    ans = analyze_LDL(LDL)
    assert ans == expected


def test_analyze_HDL():
    from interface import analyze_HDL
    ans = analyze_HDL(70)
    assert ans == "Normal"


def test_analyze_HDL_1():
    from interface import analyze_HDL
    ans = analyze_HDL(40)
    assert ans == "Borderline Low"


def test_analyze_HDL_2():
    from interface import analyze_HDL
    ans = analyze_HDL(39)
    assert ans == "Low"
