from itertools import permutations
import sys

def readInput():
	with open('./day2Input.txt', 'r') as f:
		data = [x.split(',') for x in f.readlines()]

	data = [int(x) for x in data[0]]

	A={}

	i=0
	for x in data:
		A[i]=int(x)
		i+=1

	return A

def runIntCode(seq,noun=1,verb=1):
	#takes an input dictionary and the noun/verb pair values and runs the intcode program
	#returns the dictionary

	seq[1]=noun
	seq[2]=verb
	#print(noun,verb)

	i=0
	while True:
		z = seq.get(i,0)
		#print(z,i)

		if z == 1:
			#add the next 2 values and set in third
			seq[seq.get(i+3,0)] = seq.get(seq.get(i+1,0),0) + seq.get(seq.get(i+2,0),0)

		elif z == 2:
			#multiply the next 2 values and set in third
			seq[seq.get(i+3,0)] = seq.get(seq.get(i+1,0),0) * seq.get(seq.get(i+2,0),0)

		elif z == 99:
			#print('Program has terminated')
			break

		else:
			#print('Program has encountered non-standard opcode - stop')
			break

		#increment
		i+=4

	#program has completed
	#print('Value at position 0: {}'.format(A.get(0)))

	return seq

def part1():
	A = readInput()

	#run program
	B=runIntCode(A,noun=12,verb=2)	

def part2():
	#get desired output
	A = readInput()

	z = permutations(range(0,100),2)
	target = 19690720

	for noun, verb in z:
		B=runIntCode(seq=A.copy(),noun=noun,verb=verb)
		if B.get(0) == target:
			#target reached
			print('Target number reached, with input noun {} and verb {}'.format(noun, verb))
			print('Final answer is {}'.format(100*noun+verb))
			break

if __name__ == "__main__":
	part1()
	part2()