a = int(input(' nhap so sinh vien: '))
sv= {}
dsm=[]
for _ in range(a):
    ten= input('ten: ')
    diem= float(input('nhap diem:'))
    sv[ten]= diem
while len(sv) > 0:
    ten_m= None
    diem_m=-1
    for ten in sv:
        if sv[ten] > diem_m:
            diem_m = sv[ten]
            ten_m = ten
    dsm.append((ten_m , diem_m))
    del sv[ten_m]
print(dsm)
    
    
        

