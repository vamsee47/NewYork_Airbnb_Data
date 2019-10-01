#opens mapperoutput.txt file to read
mIn = open("mapperoutput.txt","r")
#opens reduceroutput.txt to write
mOut = open("reducerOutput.txt","w")
thisKey = ""
#assign 0 to thisValue
thisValue = 0
fullList = []
#reading data and assigning to varialbles
for line in mIn:
  rowList = []
  data = line.split('\t')
  State = data[0]
  Averagetotalpayements = data[1]
  rowList.append(State)
  rowList.append(Averagetotalpayements)
  fullList.append(rowList)
   #print(fullList)

fullList.sort()
minValue = 0
finalObject = {}
for row in fullList:
  #assign default values to thisKey, thisValue, minValue 
  if row[0] != thisKey:
    thisKey = row[0]
    thisValue = 0
    minValue = 0
#Checking the minimum number of reviews
  thisKey = row[0]
  row[1] = row[1].replace(",","")
  thisValue = row[1]
  if thisValue < minValue:
    minValue = thisValue
  finalObject[thisKey] = minValue
for keyValue in finalObject:
  #print to comsole
  print(keyValue + " " + str(finalObject[keyValue]))
  #print to file
  mOut.write(keyValue + " " + str(finalObject[keyValue]))

# close redinput and redouput file
mIn.close()
mOut.close()
