def cook(scriptOP):
	invals = scriptOP.inputs[0]
	tracked, x, z = invals.chan('*_tracked')[0], invals.chan('*:tx')[0], invals.chan('*:tz')[0]
	scriptOP.clear()
	zonetbl = op('zones')
	xbounds = float(zonetbl[i, 'xmin']), float(zonetbl[i, 'xmax'])
	zbounds = float(zonetbl[i, 'zmin']), float(zonetbl[i, 'zmax'])
	for i in range(1, zonetbl.numRows):
		ch = scriptOP.appendChan(zonetbl[i, 'event'])
		if tracked and xbounds[0] <= x < xbounds and zbounds[0] <= z < zbounds[1]:
			ch.vals = [1]
		else:
			ch.vals = [0]
