def init(cell_defs, cell_states):
    cell_states.clear()
    cell_states.appendRow(['id', 'active', 'player',
                           'rest_centerx', 'rest_centerz',
                           'rest_xmin', 'rest_xmax', 'rest_zmin', 'rest_zmax',
                           'centerx', 'centerz',
                           'xmin', 'xmax', 'zmin', 'zmax',
                           'sizex', 'sizez'])
    for i in range(1, cell_defs.numRows):
        cell_states.appendRow()
        cell_states[i, 'id'] = cell_defs[i, 'id']
        cell_states[i, 'rest_centerx'] = cell_states[i, 'centerx'] = cell_defs[i, 'centerx']
        cell_states[i, 'rest_centerz'] = cell_states[i, 'centerz'] = cell_defs[i, 'centerz']
        cell_states[i, 'rest_xmin'] = cell_states[i, 'xmin'] = cell_defs[i, 'xmin']
        cell_states[i, 'rest_xmax'] = cell_states[i, 'xmax'] = cell_defs[i, 'xmax']
        cell_states[i, 'rest_zmin'] = cell_states[i, 'zmin'] = cell_defs[i, 'zmin']
        cell_states[i, 'rest_zmax'] = cell_states[i, 'zmax'] = cell_defs[i, 'zmax']
        cell_states[i, 'sizex'] = cell_defs[i, 'sizex']
        cell_states[i, 'sizez'] = cell_defs[i, 'sizez']
        cell_states[i, 'active'] = 0
        cell_states[i, 'player'] = ''

def update(cell_states, points, players_active):
    for cell_index in range(1, cell_states.numRows):
        cell_id = cell_states[cell_index, 'id'].val
        active = cell_states[cell_index, 'active'] == '1'
        if active:
            player_id = cell_states[cell_index, 'player']
            if not players_active[player_id][0]:
                deactivate_cell(cell_states, cell_id)
                update_inactive_cell(cell_states, cell_index, points)
            else:
                update_active_cell(cell_states, cell_index, points)
        else:
            player_id = get_player_in_cell(points, players_active, cell_states, cell_index)
            if player_id:
                activate_cell(cell_states, cell_index, points, player_id)
                update_active_cell(cell_states, cell_index, points)
            else:
                update_inactive_cell(cell_states, cell_index, points)

def get_player_in_cell(points, players_active, cell_states, cell_index):
    xmin, xmax = get_dat_value_pair(cell_states, cell_index, 'rest_xmin', 'rest_xmax')
    zmin, zmax = get_dat_value_pair(cell_states, cell_index, 'rest_zmin', 'rest_zmax')
    for player in players_active.chans():
        if not player[0]:
            continue
        px, pz = get_player_position(points, player.name)
        if xmin <= px < xmax and zmin <= pz < zmax:
            return player.name

def get_dat_value_pair(dat, row, col_a, col_b):
    return float(dat[row, col_a]), float(dat[row, col_b])

def get_player_position(points, player_id):
    return points[player_id + '/spine:tx'][0], points[player_id + '/spine:tz'][0]

def activate_cell(cell_states, cell_index, points, player_id):
    cell_states[cell_index, 'player'] = player_id
    cell_states[cell_index, 'active'] = 1
    pass

def update_active_cell(cell_states, cell_index, points):
    player_id = cell_states[cell_index, 'player']
    px, pz = get_player_position(points, player_id)
    sizex, sizez = get_dat_value_pair(cell_states, cell_index, 'sizex', 'sizez')
    cell_states[cell_index, 'centerx'], cell_states[cell_index, 'centerz'] = px, pz
    cell_states[cell_index, 'xmin'], cell_states[cell_index, 'xmax'] = px - (sizex / 2), px + (sizex / 2)
    cell_states[cell_index, 'zmin'], cell_states[cell_index, 'zmax'] = pz - (sizez / 2), pz + (sizez / 2)
    pass

def deactivate_cell(cell_states, cell_index):
    cell_states[cell_index, 'player'] = ''
    cell_states[cell_index, 'active'] = 0
    for part in ['xmin', 'xmax', 'zmin', 'zmax', 'centerx', 'centerz']:
        cell_states[cell_index, part] = cell_states[cell_index, 'rest_' + part]

def update_inactive_cell(cell_states, cell_index, points):
    pass

