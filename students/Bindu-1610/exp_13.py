lst=[1,2,3,2,4,5,1]
duplicates=[]
for item in lst:
 if lst.count(item)>1 and item not in duplicates:
  duplicates.append(item)
print('Duplicates:',duplicates)