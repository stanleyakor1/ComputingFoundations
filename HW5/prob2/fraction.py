
class Fraction:
        # constructor that takes in the numerator and denominator
	def __init__(self,numerator:int, denominator:int):
		self.numerator=numerator
		self.denominator=denominator     

	def setNumerator(self,other):
		self.numerator=other

	def getNumerator(self):
		return self.numerator

	def setDenominator(self,other):
		self.denominator=other

	def getDenominator(self):
		return self.denominator
        # implementing a recursive method for the gcd
	def GCD(self,numerator,denominator):
		if denominator == 0:return numerator
		return self.GCD(self,denominator,numerator %denominator)
	
	def __str__(self):
		return f"{self.numerator}/{self.denominator}"




