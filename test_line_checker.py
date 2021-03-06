import pytest

#Rule: must be a line between 2 given pts & the returned pt

@pytest.mark.parametrize("p1, p2, x, y", [
    [(0,0), (0,0), 5, "any"], #overlapping points - multiple answers
	[(0,0), (0,1), 0, "any"], #vertical line - multiple answers
	[(0,0), (0,1), 1, "none"], #vertical line - no answers
	[(0,0), (1,0), 5, 0], #horizontal line - same value
	[(0,0), (1,0), -3, 0], #horizontal line - same value
	[(0,0), (1,1), 100000, 100000], #y=x, big numbers
	[(0,-1), (-1,0), 2, -3], #negative values
	[(0,0), (1,-1), "3", -3], #strings
	[(0,0), (1,"-1"), 3, -3], #strings
	[(0,0), (.1,-.3), "1.5", -4.5]] #decimals
	)
def test_yfinder(p1, p2, x, y):
    from line_checker import yfinder
    ans = yfinder(p1, p2, x)
    assert ans == pytest.approx(y)