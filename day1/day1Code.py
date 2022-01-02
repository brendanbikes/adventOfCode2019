

def readInput():
	with open('./day1Input.txt', 'r') as f:
		data = [int(x.strip()) for x in f.readlines()]

	return data

def fuel(m):
	return m//3-2

def part1():
	data = readInput()

	n=0
	for x in data:
		n+=(x//3-2)

	print('The final sum is {}'.format(n))


def part2():
	data = readInput()

	n=0
	for x in data:
		m=x
		while True:
			z = fuel(m)
			if z<=0:
				break
			else:
				n+=z
				m=z

	print('The final fuel required is {}'.format(n))

if __name__ == "__main__":
	part1()
	part2()