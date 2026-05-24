l = [1,2,3,2,4,1]
d = []
for i in l:
    if l.count(i)>1 and i not in d:
        d.append(i)
print(d)
