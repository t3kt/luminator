def cook(scriptOP):
	scriptOP.clear()
	playersin = scriptOP.inputs[0]
	handsin = scriptOP.inputs[1]
	activecount = 0
	firstactive = 0
	xbounds = scriptOP.par.value0x, scriptOP.par.value1x
	ybounds = scriptOP.par.value0y, scriptOP.par.value1y
	zbounds = scriptOP.par.value0z, scriptOP.par.value1z
	outbounds = 0, 1
	playername = op('cell')[1, 'player'].val
	active = playername is not None and playername != ''
	scriptOP.appendChan('active')[0] = active
	if not active:
		addchan(scriptOP, 'hand_l:tx', 0)
		addchan(scriptOP, 'hand_l:ty', 0)
		addchan(scriptOP, 'hand_l:tz', 0)
		addchan(scriptOP, 'hand_r:tx', 0)
		addchan(scriptOP, 'hand_r:ty', 0)
		addchan(scriptOP, 'hand_r:tz', 0)
	else:
		addchan(scriptOP, 'hand_l:tx', handsin[playername + '/hand_l:tx'], xbounds, outbounds)
		addchan(scriptOP, 'hand_l:ty', handsin[playername + '/hand_l:ty'], ybounds, outbounds)
		addchan(scriptOP, 'hand_l:tz', handsin[playername + '/hand_l:tz'], zbounds, outbounds)
		addchan(scriptOP, 'hand_r:tx', handsin[playername + '/hand_r:tx'], xbounds, outbounds)
		addchan(scriptOP, 'hand_r:ty', handsin[playername + '/hand_r:ty'], ybounds, outbounds)
		addchan(scriptOP, 'hand_r:tz', handsin[playername + '/hand_r:tz'], zbounds, outbounds)

def addchan(chop, name, val, inrange = None, outrange = None):
	if inrange is not None:
		val = scale(val, inrange, outrange)
	chop.appendChan(name)[0] = val

def scale(x, inrange, outrange):
	return (x-inrange[0])*(outrange[1]-outrange[0])/(inrange[1] - inrange[0]) + outrange[0]
