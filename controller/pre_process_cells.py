def cook(dat):
	dat.clear()
	cellsin = dat.inputs[0]
	numx = max(cellsin.col('cellx')[1:])
	numz = max(cellsin.col('cellz')[1:])
	dat.appendRow(cellsin.row(0)+ ['xmin', 'xmax', 'zmin', 'zmax'])
	bounds = op('kinectbounds')
	xbounds = float(dat.var('kinectscaledxmin')), float(dat.var('kinectscaledxmax'))
	zbounds = float(dat.var('kinectscaledzmin')), float(dat.var('kinectscaledzmax'))
	for i in range(1, cellsin.numRows):
		x, z = int(cellsin[i, 'cellx']), int(cellsin[i, 'cellz'])
		parts = cellsin.row(i)
		parts += [ scale(x, (0, numx), xbounds), scale(x+1, (0, numx), xbounds) ]
		parts += [ scale(z, (0, numz), zbounds), scale(z+1, (0, numz), zbounds) ]
		dat.appendRow(parts)

def scale(x, inrange, outrange):
	return (x-inrange[0])*(outrange[1]-outrange[0])/(inrange[1] - inrange[0]) + outrange[0]