ds=[1, 5, 8,6,4,3,12, 20]
Q=16
gan= 0
cap= None
for i in range(len(ds)):
    for j in range(i+1,len(ds)) :
        tong=ds[i] + ds[j]
        lech=abs(Q - tong)
        if lech <= gan:
           gan= lech
           cap=(ds[i] , ds[j])
print(cap)
        