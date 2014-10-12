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
    pass

def update(points, players, cell_states):
    for i in range(1, cell_states.numRows):
        id = cell_states[i, 'id'].val
        active = cell_states[i, 'active'] == '1'
        pass
    pass

def update_active_cell(points, players, cell_states, id):
    pass

def deactivate_cell(cell_states, id):
    pass

def activate_cell(cell_states, id, points, player):
    pass

