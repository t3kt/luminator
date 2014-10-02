def replicate(comp, allops, newops, template, master):
	prev = None
	for c in allops:	
		c.par.clone = comp.par.master
		c.par.externaltox = ''
		if prev:
			c.inputConnectors[1].disconnect()
			c.inputConnectors[1].connect(prev.outputConnectors[0])
		prev = c
	if prev:
		op('add_to_background').inputConnectors[1].connect(prev.outputConnectors[0])

