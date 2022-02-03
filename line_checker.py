
def yfinder(p1, p2, x):

	#get dX from p1 to p2 & dY from p1 to p2
	#get dX2 from p2 to new x, multiply dX2(dY/dX)
	#add this to y from p2
	
	dx1 = float(p2[0]) - float(p1[0])	
	dy1 = float(p2[1]) - float(p1[1])
	
	if dx1 == 0:
		if dy1 == 0:
			y = "any"
		elif x == float(p1[0]):
			y = "any"
		else:
			y = "none"
	else:
		dx2 = float(x) - float(p2[0])
		dy2 = dx2*(dy1/dx1)
		y = float(p2[1]) + dy2
	
	return y