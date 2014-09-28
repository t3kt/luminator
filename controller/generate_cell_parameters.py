def cook(scriptOP):
	scriptOP.clear()
	playersin = scriptOP.inputs[0]
	handsin = scriptOP.inputs[1]
	activecount = 0
	firstactive = 0
	xbounds = scriptOP.par.value0x, scriptOP.par.value1x
	zbounds = scriptOP.par.value0z, scriptOP.par.value1z
	xzoutbounds = -1, 1
	ybounds = 0, 1
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
		addchan(scriptOP, 'hand_l:tx', handsin[playername + '/hand_l:tx'], xbounds, xzoutbounds)
		addchan(scriptOP, 'hand_l:ty', handsin[playername + '/hand_l:ty'], ybounds, ybounds)
		addchan(scriptOP, 'hand_l:tz', handsin[playername + '/hand_l:tz'], zbounds, xzoutbounds)
		addchan(scriptOP, 'hand_r:tx', handsin[playername + '/hand_r:tx'], xbounds, xzoutbounds)
		addchan(scriptOP, 'hand_r:ty', handsin[playername + '/hand_r:ty'], ybounds, ybounds)
		addchan(scriptOP, 'hand_r:tz', handsin[playername + '/hand_r:tz'], zbounds, xzoutbounds)

def addchan(chop, name, val, inrange = None, outrange = None):
	if inrange is not None:
		val = scale(val, inrange, outrange)
	chop.appendChan(name)[0] = val

def scale(x, inrange, outrange):
	return (x-inrange[0])*(outrange[1]-outrange[0])/(inrange[1] - inrange[0]) + outrange[0]
