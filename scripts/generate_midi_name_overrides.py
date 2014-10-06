def cook(scriptOP):
	tbl = op(scriptOP.inputs[0])
	scriptOP.clear()
	scriptOP.appendRow(['path','parameter', 'value'])
	outputs = []
	params = []
	if tbl.numRows == 0:
		pass
	else:
		for i in range(1, tbl.numRows):
			mctrl = tbl[i, 'midi'].val
			if mctrl:
				outputs.append(mctrl)
				params.append(tbl[i, 'name'].val)
	scriptOP.appendRow(['selmidiouts', 'channames', ' '.join(params)])
	scriptOP.appendRow(['selmidiouts', 'renameto', ' '.join(outputs)])
