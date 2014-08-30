def cook(scriptOP):
	invals = scriptOP.inputs[0]
	tracked, u, v = invals.chan('*:tracked')[0], invals.chan('*:u')[0], invals.chan('*:v')[0]
	scriptOP.clear()
	zonetbl = op('zones')
	for i in range(1, zonetbl.numRows):
		ch = scriptOP.appendChan(zonetbl[i, 'zone'])
		if not tracked:
			ch.vals = [0]
		elif float(zonetbl[i, 'umin'].val) <= u < float(zonetbl[i, 'umax'].val) and float(zonetbl[i, 'vmin'].val) <= v < float(zonetbl[i, 'vmax'].val):
			ch.vals = [1]
		else:
			ch.vals = [0]

# class ZoneTrigger:
# 	def __init__(self, zonetbl, zonename):
# 		self.zonetbl = zonetbl
# 		self.zonename = zonename
# 		self.eventname = ''
# 		self.urange = (0., 0.)
# 		self.vrange = (0., 0.)
# 		self.reinit(zonetbl, zonename)
#
# 	def reinit(self, zonetbl, zonename):
# 		self.urange = (float(zonetbl[zonename, 'umin'].val), float(zonetbl[zonename, 'umax'].val))
# 		self.vrange = (float(zonetbl[zonename, 'vmin'].val), float(zonetbl[zonename, 'vmax'].val))
# 		self.zonename = zonename
# 		self.eventname = zonetbl[zonename, 'event'].val
#
# 	def inzone(self, u, v):
# 		return self.urange[0] <= u < self.urange[1] and self.vrange[0] <= v < self.vrange[1]
#
# 	def cook(self, scriptOP):
# 		scriptOP.clear()
# 		#ch = scriptOP.chan(self.zonename)
# 		#if ch is None:
# 		ch = scriptOP.appendChan(self.zonename)
# 		ins = scriptOP.inputs[0]
# 		active = ins.chan('*:tracked').vals[0] != 0 and self.inzone(ins.chan('*:u').vals[0], ins.chan('*:v').vals[0])
# 		ch.vals = [1 if active else 0]

