def cook(dat):
	dat.clear()
	cellsin = dat.inputs[0]
	dat.appendRow(cellsin.row(0) + ['cellrenderw', 'cellrenderh', 'cellrendertx', 'cellrenderty'])
	gridxrange = float(var('kinectxmin')), float(var('kinectxmax'))
	gridzrange = float(var('kinectzmin')), float(var('kinectzmax'))
	gridw = gridxrange[1] - gridxrange[0]
	gridh = gridzrange[1] - gridzrange[0]
	renderw, renderh = float(var('renderw')), float(var('renderh'))
	for i in range(0, cellsin.numRows - 1):
		sizex, sizez = float(cellsin[i+1, 'sizex']), float(cellsin[i+1, 'sizez'])
		centerx, centerz = float(cellsin[i+1, 'centerx']), float(cellsin[i+1, 'centerz'])
		cellrw = int(scale(sizex, [0, gridw], [0, renderw]))
		cellrh = int(scale(sizez, [0, gridh], [0, renderh]))
		celltx = int(scale(centerx, gridxrange, [-renderw/2, renderw/2]))
		cellty = int(scale(centerz, gridzrange, [-renderh/2, renderh/2]))
		dat.appendRow(cellsin.row(i+1)+[cellrw, cellrh, celltx, cellty])

def scale(x, inrange, outrange):
	return (x-inrange[0])*(outrange[1]-outrange[0])/(inrange[1] - inrange[0]) + outrange[0]