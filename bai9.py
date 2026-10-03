ds=[1,2,3,9,9,8,7,6,3,2,1]
dsm=[]
for i in ds:
    if i not in dsm:
        dsm.append(i)
print(dsm)
