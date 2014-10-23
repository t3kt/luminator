
cellpointparts = ['hand_l:tx', 'hand_l:ty', 'hand_l:tz', 'hand_r:tx', 'hand_r:ty', 'hand_r:tz']
cellparts = ['player', 'active'] + cellpointparts

allchannels = []

def generate_channels(cells):
	global allchannels
	allchannels.clear()
	for cell in cells.col('id')[1:]:
		cellname = cell.val
		for part in cellparts:
			allchannels.append(cellname + '/' + part)

def init_chop_channels(params, cells):
	params.clear()
	if len(allchannels) == 0:
		generate_channels(cells)
	for chan in allchannels:
		params.appendChan(chan)[0] = -1 if 'chan'.endswith('/player') else 0

def cook(params):
	cells = op('cells')
	if len(allchannels) == 0 or params.numChans != len(allchannels):
		init_chop_channels(params, cells)
	points = params.inputs[0]
	statuses = params.inputs[1]
	players = params.inputs[2]
	cellvals = params.inputs[3]
	cellnames = cells.col('id')[1:]
	for cell_index in range(0, len(cellnames)):
		cell = cellnames[cell_index].val
		xminmax, zminmax = cell_bounds(cellvals, cell_index)
		player = get_player_in_cell(players, points, xminmax, zminmax, cell)
		if player < 0:
			params[cell + '/active'][0] = 0
			params[cell + '/player'][0] = -1
		else:
			playername = 'p' + str(player + 1)
			params[cell + '/active'][0] = 1
			params[cell + '/player'][0] = player
			for part in cellpointparts:
				params[cell + '/' + part][0] = points[playername + '/' + part][0]

def cell_bounds(cellvals, cell_index):
	xminmax = cellvals['xmin'][cell_index], cellvals['xmax'][cell_index]
	zminmax = cellvals['zmin'][cell_index], cellvals['zmax'][cell_index]
	return xminmax, zminmax

def get_player_in_cell(players, points, xminmax, zminmax, cellname):
	for player_index in range(players.numChans):
		player = players[player_index]
		if player[0]:
			px, pz = points[player.name + '/spine:tx'][0], points[player.name + '/spine:tz'][0]
			incell = xminmax[0] <= px < xminmax[1] and zminmax[0] <= pz < zminmax[1]
			if incell:
				return player_index
	return -1