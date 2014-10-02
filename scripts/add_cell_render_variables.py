def cook(dat):
	dat.clear()
	cellsin = dat.inputs[0]
	dat.appendRow(cellsin.row(0) + ['cellrenderw', 'cellrenderh', 'cellrendertx', 'cellrenderty'])
	gridxrange = float(var('kinectscaledxmin')), float(var('kinectscaledxmax'))
	gridzrange = float(var('kinectscaledzmin')), float(var('kinectscaledzmax'))
	gridw = gridxrange[1] - gridxrange[0]
	gridh = gridzrange[1] - gridzrange[0]
	renderw, renderh = float(var('renderw')), float(var('renderh'))
	for i in range(1, cellsin.numRows):
		sizex, sizez = float(cellsin[i, 'sizex']), float(cellsin[i, 'sizez'])
		centerx, centerz = float(cellsin[i, 'centerx']), float(cellsin[i, 'centerz'])
		cellrw = int(scale(sizex, [0, gridw], [0, renderw]))
		cellrh = int(scale(sizez, [0, gridh], [0, renderh]))
		celltx = int(scale(centerx, gridxrange, [-renderw/2, renderw/2]))
		cellty = int(scale(centerz, gridzrange, [renderh/2, -renderh/2]))
		dat.appendRow(cellsin.row(i)+[cellrw, cellrh, celltx, cellty])

def scale(x, inrange, outrange):
	return (x-inrange[0])*(outrange[1]-outrange[0])/(inrange[1] - inrange[0]) + outrange[0]