def cook(scriptOP):
	if not scriptOP['hand_l:tx']:
		scriptOP.clear()
		scriptOP.copy(op('defaults'))
	pointsin = scriptOP.inputs[0]
	cellplayerin = scriptOP.inputs[1]
	if not cellplayerin:
		print('!!!! cellplayer input not found!!!!')
		return
	cellplayerchan = cellplayerin['activeplayer']
	if not cellplayerchan:
		print('!!!! cellplayer channel not found!!!!')
		return	
	cellplayer = cellplayerchan[0]
	xbounds = scriptOP.par.value0x, scriptOP.par.value1x
	ybounds = scriptOP.par.value0y, scriptOP.par.value1y
	zbounds = scriptOP.par.value0z, scriptOP.par.value1z
	active = cellplayer != -1
	if not active:
		return
	playername = 'p' + (cellplayer + 1)
	scriptOP['active'][0] = active
	scriptOP['hand_l:tx'][0] = scale(pointsin[playername + '/hand_l:tx'], xbounds)
	scriptOP['hand_l:ty'][0] = scale(pointsin[playername + '/hand_l:ty'], ybounds)
	scriptOP['hand_l:tz'][0] = scale(pointsin[playername + '/hand_l:tz'], zbounds)
	scriptOP['hand_r:tx'][0] = scale(pointsin[playername + '/hand_r:tx'], xbounds)
	scriptOP['hand_r:ty'][0] = scale(pointsin[playername + '/hand_r:ty'], ybounds)
	scriptOP['hand_r:tz'][0] = scale(pointsin[playername + '/hand_r:tz'], zbounds)

def scale(x, inrange):
	return (x - inrange[0]) / (inrange[1] - inrange[0])
