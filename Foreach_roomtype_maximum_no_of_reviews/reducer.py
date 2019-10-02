#reading data from mapperouutput.txt file
mapin = open("mapperoutput.txt","r")
#opening r.txt file to write the output
mapout = open("r.txt","w")
thisKey = ""
thisValue = 0
fullList = []a
for line in mapin:
  #reading and sepeerating coloums
  rowList = []
  data = line.split('\t')
  #assigning read data to variables
  State = data[0]
  Averagetotalpayements = data[1]
  rowList.append(State)
  rowList.append(Averagetotalpayements)
  fullList.append(rowList)
 

fullList.sort()
maxValue = 0
finalObject = {}
for row in fullList:
  #assigning the default values to thisValue and maxValue
  if row[0] != thisKey:
    thisKey = row[0]
    thisValue = 0
    maxValue = 0
#checking the loop for the maximum reviews 
  thisKey = row[0]
  row[1] = row[1].replace(",","")
  thisValue = row[1]
  if thisValue > maxValue:
    maxValue = thisValue
  finalObject[thisKey] = maxValue
  

for keyValue in finalObject:
  #printing to console
  print(keyValue + " " + str(finalObject[keyValue]))
  #printing to r.txt file
  mapout.write(keyValue + " " + str(finalObject[keyValue]))



# close redinput and redouput file
mapin.close()
mapout.close()
