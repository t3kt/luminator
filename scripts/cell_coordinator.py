changing_parts = ['centerx', 'centerz', 'xmin', 'xmax', 'zmin', 'zmax']

def init(cell_defs, cell_states, cell_state_vals):
    cell_states.clear()
    cell_states.appendRow(['id', 'player', 'index'])
    #cell_state_vals.clear()
    #for part in changing_parts + ['active']:
    #    cell_state_vals.appendChan(part)
    #cell_state_vals.numSamples = cell_defs.numRows - 1
    for i in range(1, cell_defs.numRows):
        cell_states.appendRow()
        cell_states[i, 'id'] = cell_defs[i, 'id']
        #cell_states[i, 'active'] = 0
        #cell_state_vals['active'][i - 1] = 0
        cell_states[i, 'player'] = ''
        cell_states[i, 'index'] = i - 1
        #for part in changing_parts:
        #    cell_state_vals[part][i - 1] = cell_defs[i, part]

def update(cell_defs, cell_def_vals, cell_states, cell_state_vals, points, players_active):
    for cell_index in range(1, cell_states.numRows):
        cell_id = cell_states[cell_index, 'id'].val
        active = int(cell_state_vals['active'][cell_index - 1])
        if active:
            player_id = cell_states[cell_index, 'player']
            if not players_active[player_id][0]:
                deactivate_cell(cell_def_vals, cell_states, cell_state_vals, cell_id)
                pass
            else:
                update_active_cell(cell_def_vals, cell_states, cell_state_vals, cell_index, points)
        else:
            player_id = get_player_in_cell(points, players_active, cell_def_vals, cell_index)
            if player_id:
                activate_cell(cell_states, cell_state_vals, cell_index, player_id)
                update_active_cell(cell_def_vals, cell_states, cell_state_vals, cell_index, points)
            else:
                pass

def get_player_in_cell(points, players_active, cell_def_vals, cell_index):
    xmin, xmax = cell_def_vals['xmin'][cell_index - 1], cell_def_vals['xmax'][cell_index - 1]
    zmin, zmax = cell_def_vals['zmin'][cell_index - 1], cell_def_vals['zmax'][cell_index - 1]
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

def activate_cell(cell_states, cell_state_vals, cell_index, player_id):
    cell_states[cell_index, 'player'] = player_id
    cell_state_vals['active'][cell_index - 1] = 1

def update_active_cell(cell_def_vals, cell_states, cell_state_vals, cell_index, points):
    player_id = cell_states[cell_index, 'player']
    px, pz = get_player_position(points, player_id)
    sizex, sizez = cell_def_vals['sizex'][cell_index - 1], cell_def_vals['sizez'][cell_index - 1]
    cell_state_vals['centerx'][cell_index - 1], cell_state_vals['centerz'][cell_index - 1] = px, pz
    cell_state_vals['xmin'][cell_index - 1], cell_state_vals['xmax'][cell_index - 1] = px - (sizex / 2), px + (sizex / 2)
    cell_state_vals['zmin'][cell_index - 1], cell_state_vals['zmax'][cell_index - 1] = pz - (sizez / 2), pz + (sizez / 2)

def deactivate_cell(cell_def_vals, cell_states, cell_state_vals, cell_index):
    cell_states[cell_index, 'player'] = ''
    cell_state_vals['active'][cell_index - 1] = 0
    for part in ['xmin', 'xmax', 'zmin', 'zmax', 'centerx', 'centerz']:
        cell_state_vals[part][cell_index - 1] = cell_def_vals[part][cell_index - 1]
