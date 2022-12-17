class Purchase:
	
	def __init__(self,description: str,price: float,quantity=0):
		self.description=description
		self.price=price
		self.quantity=quantity

		assert price >=0, f"price {price} is not greater than or equal to zero!"
		assert quantity >=0, f"quantity {quantity} is not greater than or equal to zero!"

	
	def setDescription(self,other: str):
		self.description = other

	def getDescription(self):
		return self.description

	def setPrice(self,other: float):
		self.price=other

	def getPrice(self):
		return self.price

	def setQuantity(self,other:int):
		self.quantity=other

	def getQuantity(self):
		return self.quantity

class Cart:
	
	
	def __init__(self,article=[],total=0):
		self.article=article
		self.total=total

	def addItemToCart(self,other):

		self.article.append(other)

	def getItems(self):
		return self.article

	def calculateTotal(self):

		for i in range(len(self.article)):

			self.total+=self.article[i].getPrice()* self.article[i].getQuantity()

		return self.total


		
