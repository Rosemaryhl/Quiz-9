#Rosemary Hoffman
#Quiz problem 3
import dbm
dbm2=dbm.open("Houses","c")
dbm2.close()
dbm1=dbm.open("Houses","w")
dbm1["bathrooms.png"]="there are two bathrooms"
dbm1["bedrooms.png"]="there are three bedrooms"
dbm1["kitchen.png"]="there is a large kitchen with two ovens"
dbm1["flooring.jpeg"]="the floors are wooden"
dbm1["furniture.jpeg"]="the house in unfurnished"
print(dbm1)
for line in dbm1:
    print(line,dbm1[line])
dbm1.close()
