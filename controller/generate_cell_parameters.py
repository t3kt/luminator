def cook(scriptOP):
	if not scriptOP['hand_l:tx']:
		scriptOP.clear()
		scriptOP.copy(op('defaults'))
	handsin = scriptOP.inputs[1]
	xbounds = scriptOP.par.value0x, scriptOP.par.value1x
	ybounds = scriptOP.par.value0y, scriptOP.par.value1y
	zbounds = scriptOP.par.value0z, scriptOP.par.value1z
	playername = op('cell')[1, 'player'].val
	active = 1 if playername else 0
	scriptOP.appendChan('active')[0] = active
	if not active:
		return
	scriptOP['hand_l:tx'][0] = scale(handsin[playername + '/hand_l:tx'], xbounds)
	scriptOP['hand_l:ty'][0] = scale(handsin[playername + '/hand_l:ty'], ybounds)
	scriptOP['hand_l:tz'][0] = scale(handsin[playername + '/hand_l:tz'], zbounds)
	scriptOP['hand_r:tx'][0] = scale(handsin[playername + '/hand_r:tx'], xbounds)
	scriptOP['hand_r:ty'][0] = scale(handsin[playername + '/hand_r:ty'], ybounds)
	scriptOP['hand_r:tz'][0] = scale(handsin[playername + '/hand_r:tz'], zbounds)

def scale(x, inrange):
	return (x - inrange[0]) / (inrange[1] - inrange[0])
