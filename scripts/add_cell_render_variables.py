def cook(dat):
	dat.clear()
	cellsin = dat.inputs[0]
	dat.appendRow(cellsin.row(0) + ['cellrenderw', 'cellrenderh', 'cellrendertx', 'cellrenderty'])
	cellvals = op('cellvals')
	gridxrange = float(var('kinectxmin')), float(var('kinectxmax'))
	gridzrange = float(var('kinectzmin')), float(var('kinectzmax'))
	gridw, gridh = gridxrange[1] - gridxrange[0], gridzrange[1] - gridzrange[0]
	renderw, renderh = float(var('renderw')), float(var('renderw'))
	renderwrange, renderhrange = [-renderw / 2, renderw / 2], [renderh / 2, -renderh / 2]
	#print('gridxrange', gridxrange, 'gridzrange', gridzrange)
	#print('gridw', gridw, 'gridh', gridh, 'renderw', renderw, 'renderh', renderh)
	#print('renderwrange', renderwrange, 'renderhrange', renderhrange)
	for i in range(0, cellvals.numSamples):
		sizex, sizez = cellvals['sizex'][i], cellvals['sizez'][i]
		centerx, centerz = cellvals['centerx'][i], cellvals['centerz'][i]
		cellrw = int(scale(sizex, [0, gridw], [0, renderw]))
		cellrh = int(scale(sizez, [0, gridh], [0, renderh]))
		celltx = int(scale(centerx, gridxrange, renderwrange))
		cellty = int(scale(centerz, gridzrange, renderhrange))
		dat.appendRow(cellsin.row(i + 1) + [cellrw, cellrh, celltx, cellty])

def scale(x, inrange, outrange):
	return (x - inrange[0]) * (outrange[1] - outrange[0])/(inrange[1] - inrange[0]) + outrange[0]