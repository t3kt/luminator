def update():
	op('curmode_copy').copy(op('curmodeval'))

def tableChange(dat):
	update()

def start():
	update()

update()