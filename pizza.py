print("welcome to python pizza Deliveries")
pizza={"smallpizza":150,"mediumpizza":200,"largepizza":250}
print("how many pizza do you want:")
a=int(input("enter the number of small pizza:"))
b=int(input("enter the number of large pizza:"))
c=int(input("enter the number of medium pizza:"))

cost = (a*pizza["smallpizza"]+b*pizza["largepizza"]+c*pizza["mediumpizza"])
print(cost)