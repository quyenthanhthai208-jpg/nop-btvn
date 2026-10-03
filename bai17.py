data = [
    {"name": "A", "score": 7},
    {"name": "B", "score": 9},
    {"name": "A", "score": 8},
]
ds={}
for i in data:
    ten=i['name']
    diem=i['score']
    if ten not in ds:
        ds[ten]=[diem]
    else:
        ds[ten].append(diem)
print(ds)