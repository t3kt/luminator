def replicate(comp, allops, newops, template, master):
	combine = op('combine_cells')
	for con in combine.inputConnectors:
		con.disconnect()
	combine.inputConnectors[0].connect(op('bg').outputConnectors[0])
	for c in allops:
		c.par.clone = comp.par.master
		c.par.externaltox = ''
		c.outputConnectors[0].connect(combine)

