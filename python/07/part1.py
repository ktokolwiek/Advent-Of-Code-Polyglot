# On the 7th day of codemas...

# 1
with open('input.txt') as f:
	data = [line for line in f]

gates = dict()

while not gates.get('a', None):
	print(len(gates))
	for line in data:
		try:
			operands = line.split()
			if len(operands) == 3:
				# simpleton - LHS is either value or reference
				try:
					# try casting value
					gates[operands[2]] = np.array([int(operands[0])], dtype="uint16")
				except ValueError:
					pass
				# try using reference, if present
				gates[operands[2]] = gates[operands[0]]
			elif len(operands) == 4:
				# not
				gates[operands[3]] = ~ gates[operands[1]]
			elif len(operands) == 5:
				a, op, b, arrow, res = operands
				try:
					a = np.array([int(a)], dtype="uint16")
				except ValueError:
					a = gates[a]
				try:
					b = np.array([int(b)], dtype="uint16")
				except ValueError:
					b = gates[b]
				if op == 'OR':
					gates[res] = a | b
				elif op == 'AND':
					gates[res] = a & b
				elif op == 'RSHIFT':
					gates[res] = a >> int(b)
				elif op == 'LSHIFT':
					gates[res] = a << int(b)
		except KeyError:
			pass