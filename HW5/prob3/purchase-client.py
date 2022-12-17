from purchase import *


# user's input
a=input("Enter description of the article: ")
b=float(input("Enter the price of the article: "))
c=int(input("Enter the quantity of article: "))

ask=input('Do you want to enter more articles (Y/N)?: ')

# adding items to class Cart
Cart().addItemToCart(Purchase(a,b,c));Name=[a];X=[str(c)]

while ask == 'Y':
	a=input("Enter description of the article: ")
	b=float(input("Enter the price of the article: "))
	c=int(input("Enter the quantity of article: "))
	Cart().addItemToCart(Purchase(a,b,c));Name.append(a);X.append(str(c))
	ask=input('Do you want to enter more articles (Y/N)?: ')

# This will be helpful in aligning the outputs
n=len(max(Name,key=len)) # length of the  longest string character/description
N=len(max(X,key=len))

# obtaining all the items added to Cart
cart=Cart().getItems()

print()
print("ARTICLE"+" "*abs(n-len("ARTICLE")+1),"PRICE ","QUANTITY")
for i in range(len((cart))):
	print(cart[i].getDescription(),' '*(n-len(Name[i])),'${:.2f}'.format(cart[i].getPrice())," "*(N-len(X[i])+3),cart[i].getQuantity())

print()

print("TOTAL COST: ",'${:.2f}'.format(Cart().calculateTotal()))

