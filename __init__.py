from GeothmeticMeandian import *
import random


if __name__=="__main__":
	n = 1000000
	sample = []
	for i in range(n):
		sample.append(random.random())
	a = Gmdn(sample)
	print(a)