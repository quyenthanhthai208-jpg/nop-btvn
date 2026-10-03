ds=['chó', 'chó' , 'mèo' ,'mèo', 'chó' ,'chó' , 'lợn' , 'gà',  'mèo', 'chó']
tct=input('nhap tu can tim: ')
dem=0
for c in ds:
    if c == tct :
        dem= dem + 1
print(f'số làn xuất hiện của {tct} là {dem} lần')



