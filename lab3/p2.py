#problem 2

def extract_info_from_file(text_name):
	f = open(text_name).readlines()
	result = []
	for l in f:
		tmp = l.split(' ')
		tmp[1] = int(tmp[1])
		result.append(tmp)
	return result


print(extract_info_from_file('p2_input.txt'))


# problem 3

silly = 'newly formed bland ideas are inexpressible in an infuriating way'
bland = silly.split(' ')

res1 = ''
for w in bland:
	res1 = res1 + w[1]

res2 = ' '.join(bland)
print(res1)
print(res2)
