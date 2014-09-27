def cook(dat):
	dat.clear()
	cellsin = dat.inputs[0]
	numx = max(cellsin.col('cellx')[1:])
	numz = max(cellsin.col('cellz')[1:])
	dat.appendRow(cellsin.row(0)+ ['xmin', 'xmax', 'zmin', 'zmax'])
	bounds = op('kinectbounds')
	xbounds = float(bounds['kinectxmin', 1].val), float(bounds['kinectxmax', 1].val)
	zbounds = float(bounds['kinectzmin', 1].val), float(bounds['kinectzmax', 1].val)
	for i in range(1, cellsin.numRows):
		x, z = int(cellsin[i, 'cellx']), int(cellsin[i, 'cellz'])
		parts = cellsin.row(i)
		parts += [ scale(x, (0, numx), xbounds), scale(x+1, (0, numx), xbounds) ]
		parts += [ scale(z, (0, numz), zbounds), scale(z+1, (0, numz), zbounds) ]
		dat.appendRow(parts)

def scale(x, inrange, outrange):
	return (x-inrange[0])*(outrange[1]-outrange[0])/(inrange[1] - inrange[0]) + outrange[0]