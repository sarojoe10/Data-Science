from Item import item
from phone import Phone

#item.instantiate_from_csv(r'C:\Users\NITRO\Data Science\item.csv')
#print(item.all)

item1 = item('My item',750)

item1.send_email()
print(item1.name)