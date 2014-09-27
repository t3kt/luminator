def cook(scriptOP):
	scriptOP.clear()
	partsin = scriptOP.inputs[0]
	playersin = scriptOP.inputs[1]
	for playerch in playersin.chans():
		outch = scriptOP.appendChan(playerch.name)
		if not playerch[0]:
			outch[0] = 0
			continue
		activeparts = 0
		for partch in partsin.chans(playerch.name + '/*'):
			if partch[0]:
				activeparts += 1
		outch[0] = activeparts >= 2
