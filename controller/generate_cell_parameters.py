def cook(scriptOP):
	scriptOP.clear()
	playersin = scriptOP.inputs[0]
	handsin = scriptOP.inputs[1]
	activecount = 0
	firstactive = 0
	centerx, centerz = scriptOP.par.value0x, scriptOP.par.value0z
	playername = None
	for i in range(playersin.numChans):
		playerch = playersin[i]
		if not playerch[0]:
			continue
		activecount += 1
		if firstactive == 0:
			firstactive = i
			playername = playerch.name
	scriptOP.appendChan('active')[0] = activecount > 0
	scriptOP.appendChan('activecount')[0] = activecount
	scriptOP.appendChan('activeplayer')[0] = firstactive
	if activecount == 0:
		addchan(scriptOP, 'hand_l:tx', 0)
		addchan(scriptOP, 'hand_l:ty', 0)
		addchan(scriptOP, 'hand_l:tz', 0)
		addchan(scriptOP, 'hand_r:tx', 0)
		addchan(scriptOP, 'hand_r:ty', 0)
		addchan(scriptOP, 'hand_r:tz', 0)
	else:
		addchan(scriptOP, 'hand_l:tx', handsin[playername + '/hand_l:tx'] - centerx)
		addchan(scriptOP, 'hand_l:ty', handsin[playername + '/hand_l:ty'])
		addchan(scriptOP, 'hand_l:tz', handsin[playername + '/hand_l:tz'] - centerz)
		addchan(scriptOP, 'hand_r:tx', handsin[playername + '/hand_r:tx'] - centerx)
		addchan(scriptOP, 'hand_r:ty', handsin[playername + '/hand_r:ty'])
		addchan(scriptOP, 'hand_r:tz', handsin[playername + '/hand_r:tz'] - centerz)

def addchan(chop, name, val):
	chop.appendChan(name)[0] = val
