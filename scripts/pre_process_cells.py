def cook(dat):
	dat.clear()
	cellsin = dat.inputs[0]
	numx = max(cellsin.col('cellx')[1:])
	numz = max(cellsin.col('cellz')[1:])
	dat.appendRow(cellsin.row(0) + ['xmin', 'xmax', 'zmin', 'zmax', 'centerx', 'centerz'])
	xbounds = float(dat.var('kinectscaledxmin')), float(dat.var('kinectscaledxmax'))
	zbounds = float(dat.var('kinectscaledzmin')), float(dat.var('kinectscaledzmax'))
	for i in range(1, cellsin.numRows):
		x, z = int(cellsin[i, 'cellx']), int(cellsin[i, 'cellz'])
		parts = cellsin.row(i)
		xmin, xmax = scale(x, numx, xbounds), scale(x + 1, numx, xbounds)
		parts += [xmin, xmax]
		zmin, zmax = scale(z, numz, zbounds), scale(z + 1, numz, zbounds)
		parts += [zmin, zmax]
		center = (xmin + xmax) / 2.0, (zmin + zmax) / 2.0
		parts += center
		dat.appendRow(parts)

def scale(x, inmax, outrange):
	return x*(outrange[1]-outrange[0])/inmax + outrange[0]