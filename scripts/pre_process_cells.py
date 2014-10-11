def cook(dat):
	dat.clear()
	cellsin = dat.inputs[0]
	dat.copy(cellsin)
	for i in range(1, cellsin.numRows):
		xmin, xmax = cellsin[i, 'xmin'], cellsin[i, 'xmax']
		zmin, zmax = cellsin[i, 'zmin'], cellsin[i, 'zmax']
		dat[i, 'centerx'] = (xmin + xmax) / 2.0
		dat[i, 'centerz'] = (zmin + zmax) / 2.0
		dat[i, 'sizex'] = xmax - xmin
		dat[i, 'sizez'] = zmax - zmin

def scale(x, inmax, outrange):
	return x*(outrange[1]-outrange[0])/inmax + outrange[0]