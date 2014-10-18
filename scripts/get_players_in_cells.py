def cook(scriptOP):
	cells = scriptOP.inputs[0]
	points = scriptOP.inputs[1]
	players = scriptOP.inputs[2]
	scriptOP.clear()
	scriptOP.numSamples = cells.numSamples
	cell_players = [get_player_in_cell(players, points, cells, i) for i in range(cells.numSamples)]
	scriptOP.appendChan('activeplayer').vals = cell_players

def get_player_in_cell(players, points, cells, cell_index):
	xmin, xmax = cells['xmin'][cell_index], cells['xmax'][cell_index]
	zmin, zmax = cells['zmin'][cell_index], cells['zmax'][cell_index]
	for player_index in range(players.numChans):
		player = players[player_index]
		if player[0]:
			px, pz = points[player.name + '/spine:tx'][0], points[player.name + '/spine:tz'][0]
			incell = xmin <= px < xmax and zmin <= pz < zmax
			#print('cell#', cell_index, 'x,z:', (px,pz), 'xmin,xmax:', (xmin,xmax), 'zmin,zmax:', (zmin,zmax), 'IN CELL!' if incell else 'not in cell')
			if incell:
				return player_index
	return -1