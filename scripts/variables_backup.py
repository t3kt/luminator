def updateCopy():
	dat = op('variables_in')
	copy = op('variables_copy')
	if dat.numRows > 0 and dat.numCols > 0:
		copy.copy(dat)

def tableChange(dat):
	updateCopy()

def start():
	op('variables_in').cook(force=True)
	updateCopy()


updateCopy()