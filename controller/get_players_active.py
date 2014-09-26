def cook(scriptOP):
	scriptOP.clear()
	statuses = scriptOP.inputs[0]
	for playerCell in op('players').col(0):
		player = playerCell.val
		active = is_player_active(statuses, player)
		ch = scriptOP.appendChan(player)
		ch.vals = [1 if active else 0]

def is_player_active(statuses, player):
	level  = get_tracked(statuses, player, 'spine')
	level += get_tracked(statuses, player, 'hand_l')
	level += get_tracked(statuses, player, 'hand_r')
	return level > 3

def get_tracked(statuses, player, part):
	ch = statuses[player+'/'+part+'_tracked']
	return ch[0] if ch else 0