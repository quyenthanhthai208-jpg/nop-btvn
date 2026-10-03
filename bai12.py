chuoi= input('nhap chuoi: ')
dkt={}
for i in chuoi:
        if i in dkt:
                dkt[i]= dkt[i] + 1
        else:
                dkt[i]=1
print(dkt)
        

