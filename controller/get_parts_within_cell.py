def cook(scriptOP):
	scriptOP.clear()
	xbounds = scriptOP.par.value0x, scriptOP.par.value1x
	zbounds = scriptOP.par.value0z, scriptOP.par.value1z
	pointsin = scriptOP.inputs[0]
	for xchan in pointsin.chans('*:tx'):
		zchan = pointsin[xchan.name[:-1]+'z']
		xactive = xbounds[0] <= xchan[0] < xbounds[1]
		zactive = zbounds[0] <= zchan[0] < zbounds[1]
		scriptOP.appendChan(xchan.name[:-3])[0] = 1 if xactive and zactive else 0

