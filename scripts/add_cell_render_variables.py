def cook(dat):
	dat.clear()
	cellsin = dat.inputs[0]
	celldefs = dat.inputs[1]
	dat.appendRow(cellsin.row(0) + ['cellrenderw', 'cellrenderh', 'cellrendertx', 'cellrenderty'])
	gridxrange = float(var('kinectxmin')), float(var('kinectxmax'))
	gridzrange = float(var('kinectzmin')), float(var('kinectzmax'))
	gridw = gridxrange[1] - gridxrange[0]
	gridh = gridzrange[1] - gridzrange[0]
	renderw, renderh = float(var('renderw')), float(var('renderh'))
	renderwrange, renderhrange = [-renderw / 2, renderw / 2], [renderh / 2, -renderh / 2]
	for i in range(1, cellsin.numRows):
		sizex, sizez = float(celldefs[i, 'sizex']), float(celldefs[i, 'sizez'])
		centerx, centerz = float(cellsin[i, 'centerx']), float(cellsin[i, 'centerz'])
		cellrw = int(scale(sizex, [0, gridw], [0, renderw]))
		cellrh = int(scale(sizez, [0, gridh], [0, renderh]))
		celltx = int(scale(centerx, gridxrange, renderwrange))
		cellty = int(scale(centerz, gridzrange, renderhrange))
		dat.appendRow(cellsin.row(i) + [cellrw, cellrh, celltx, cellty])

def scale(x, inrange, outrange):
	return (x - inrange[0]) * (outrange[1] - outrange[0])/(inrange[1] - inrange[0]) + outrange[0]