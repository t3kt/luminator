def cook(scriptOP):
	invals = scriptOP.inputs[0]
	tracked, u, v = invals.chan('*:tracked')[0], invals.chan('*:u')[0], invals.chan('*:v')[0]
	scriptOP.clear()
	zonetbl = op('zones')
	for i in range(1, zonetbl.numRows):
		ch = scriptOP.appendChan(zonetbl[i, 'event'])
		if tracked and float(zonetbl[i, 'umin'].val) <= u < float(zonetbl[i, 'umax'].val) and float(zonetbl[i, 'vmin'].val) <= v < float(zonetbl[i, 'vmax'].val):
			ch.vals = [1]
		else:
			ch.vals = [0]
