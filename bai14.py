ds= [(1,2),(3,6),(6,8)]
tongx=0
tongy=0
for x,y in ds:
 tongx +=x
 tongy +=y 
tbx=tongx / len(ds)
tby = tongy / len(ds)
print(f'Trung bình của x = {tbx}')
print(f'Trung bình của y = {tby}')