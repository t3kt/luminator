def cook(chop):
	chop.clear()
	playertbl = op('playername')
	if not playertbl.numRows:
		return
	player = playertbl[0,0].val
	inpfx = player + '/hand_'
	inchop = chop.inputs[0]
	outpfx = chop.var('id') + '/hand_'
	for part in ['l:tx','l:ty','l:tz',
				 'r:tx','r:ty','r:tz']:
		chop.appendChan(outpfx+part)[0] = inchop[inpfx+part]
