ds=input('nhap ds: ')
ds=ds.split()
ds=[int(x) for x in ds]
so_lan_max=0
xhnn=ds[0]
for i in ds:
    sl=ds.count(i)
    if sl > so_lan_max:
        so_lan_max = sl
        xhnn=i
print(xhnn , so_lan_max)

