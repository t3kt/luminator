import re

def cook(dat):
	dat.clear()
	prevars = dat.inputs[1]
	replace_var = lambda m: get_pre_var(m.group('var'), prevars)
	for row in dat.inputs[0].rows():
		val = pre_proc_value(row[1].val, replace_var)
		dat.appendRow([row[0], val])

def get_pre_var(varname, prevars):
	cell = prevars[varname, 1]
	return cell.val if cell is not None else '{varname}'

def pre_proc_value(val, replace_var):
	val = val.replace('~', '{rootdir}')
	val = re.sub(r'\{(?P<var>[a-z]+)\}', replace_var, val)
	return val
