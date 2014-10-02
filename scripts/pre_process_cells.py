def cook(dat):
	dat.clear()
	cellsin = dat.inputs[0]
	dat.appendRow(cellsin.row(0) + ['centerx', 'centerz', 'sizex', 'sizez'])
	for i in range(1, cellsin.numRows):
		parts = cellsin.row(i)
		xmin, xmax = cellsin[i, 'xmin'], cellsin[i, 'xmax']
		zmin, zmax = cellsin[i, 'zmin'], cellsin[i, 'zmax']
		parts += [(xmin + xmax) / 2.0, (zmin + zmax) / 2.0]
		parts += [(xmax - xmin), (zmax - zmin)]
		dat.appendRow(parts)

def scale(x, inmax, outrange):
	return x*(outrange[1]-outrange[0])/inmax + outrange[0]