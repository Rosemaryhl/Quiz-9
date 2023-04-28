#Rosemary Hoffman Problem 1
import dbm
dbm1=dbm.open("myfile.txt","c")
line1="The weather today is rainy\n"
print(line1)
line2="you may need a raincoat\n"
print(line2)
line3="or an unbrella\n"
print(line3)
line4="or rain boots\n"
print(line4)
line5="and a hot coffee\n"
print(line5)

dbm1.close()
