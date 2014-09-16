def cook(scriptOP):
	scriptOP.clear()
	players = scriptOP.par.string0.eval()
	statuses = scriptOP.par.string1.eval()
	points = scriptOP.par.string2.eval()
	statuses = prep_names(players, statuses)
	points = prep_names(players, points)
	scriptOP.appendRow(['path','parameter','value'])
	scriptOP.appendRow(['kinectselect', 'channames', statuses + ' ' + points])
	scriptOP.appendRow(['kinectANTIselect', 'delscope', statuses + ' ' + points])
	scriptOP.appendRow(['kinectstatusselect', 'channames', statuses])
	scriptOP.appendRow(['kinectpointselect', 'channames', points])

def prep_names(players, names_str):
	if not names_str:
		return ''
	names = names_str.split(' ')
	for i in range(len(names)):
		names[i] = names[i].replace('~', players)
	return ' '.join(names)
