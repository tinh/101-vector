#! /usr/bin/env python3.3                                                                                

import sys, random

def add(u, v):
	print('vecteur u+v :', end = '\t\t')
	for i in range(len(u)):
		print(u[i] + v[i], end = '\t')
	print()

def product(u, p):
	print('vecteur p.u :', end = '\t\t')
	for i in range(len(u)):
		print(u[i] * p, end = '\t')
	print()

def scalar_product(u, v):
	product = 0
	print('produit scalaire uv :', end = '\t')
	for i in range(len(u)):
		product += u[i] * v[i]
	print (product)

def vector_product(u, v):
	print('produit vectoriel u^v :', end = '\t')
	print(u[1] * v[2] - u[2] * v[1], end = '\t')	
	print(u[2] * v[0] - u[0] * v[2], end = '\t')	
	print(u[0] * v[1] - u[1] * v[0])	
	
def gen_vect(dim = 3):
	vect = list(range(dim))
	for i in vect:
		vect[i] = random.randint(0, 100)
	return vect

def print_vect(vect):
	for i in range(len(vect)):
		print(vect[i], end = '\t')
		i += 1
	print()

def main():
	func = [add, product, scalar_product]
	if len(sys.argv) == 3 and int(sys.argv[1]) == 1:
		dim = int(sys.argv[2])
		u = gen_vect(dim)
		v = gen_vect(dim)
		print('vecteur u :', end = '\t\t')
		print_vect(u)
		print('vecteur v :', end = '\t\t')
		print_vect(v)
		for n in range(len(func)):
			if n == 1:
				func[n](u, random.randint(0, 100))
			else:
				func[n](u, v)
	elif len(sys.argv) == 2 and int(sys.argv[1]) == 2:
		u = gen_vect()
		v = gen_vect()
		print('vecteur u :', end = '\t\t')
		print_vect(u)
		print('vecteur v :', end = '\t\t')
		print_vect(v)
		vector_product(u, v)
	else:
		print('usage:', sys.argv[0], '[1: add & product & scalar_product\
| dim] [2:vector_product]')

main()



