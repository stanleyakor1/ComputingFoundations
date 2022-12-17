import random

class Contestant():
	def __init__(self,name: str,score=0):
		self.score=score
		self.name=name
        # whenever a contest win, we add one to their score
	def Win(self):
		self.score+=1
	def getScore(self):
		return self.score

class Human(Contestant): # we ain't adding new features
	pass
	
class Computer(Contestant):
	def __init__(self,name: str,score=0,l=['rock', 'paper', 'scissors']):
		self.list=l
		super().__init__(name,score)
        # radomly selects a string from self.list        
	def Cplay(self):
		return random.choice(self.list)

