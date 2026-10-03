ds=input('nhap so nguyen: ')
ds = ds.split()
ds= [int(x) for x in ds]
dsm=[]
for i in ds:
    if i % 2 == 0 and i > 10:
        dsm.append(i)
print(dsm)
