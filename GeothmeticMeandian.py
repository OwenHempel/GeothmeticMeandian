from collections.abc import Iterable
from math import log, exp

def Gmdn(Sequence, Precision=3):
	if isinstance(Sequence, Iterable):
		##Sequence is iterable, proceed with GMDN

		GMDN = [ArithmeticMean(Sequence), GeometricMean(Sequence), Median(Sequence)]
		
	else:
		raise TypeError

def ArithmeticMean(Sequence):
	n = len(Sequence)
	if n==0:
		##Raise error relating to empty sequence
		pass
	else:
		sum = 0
		for i in Sequence:
			sum +=i
		return sum/float(n)

def GeometricMean(Sequence):
	try:
		log_Sequence = [math.log(i) for i in Sequence]
		log_Average = ArithmeticMean(log_Sequence)
		return math.exp(log_Average)
	except e:
		raise e


def Median(Sequence):
	pass

