# import csv, json
# csvFilePath = 'C:/aicode/readtext/dts.csv'
# jsonFilePath = 'driver2.json'
# #read csv file and add to data
# data = {}
# id = 0
# with open(csvFilePath) as z:
#     a = csv.reader(z)
#     for r in a:
#         # print(r)
#         pass

with open('dts.txt','r',encoding='utf-16LE') as a:
    b = a.read()
    c = {}
    e = 0
    # print(b.split('\t')[18:35])
    g = b.split('\t')
    for i in range(18,len(g),17):
        try:
            c[f'{e}'] = {}
            c[f'{e}'][f'{0}'] = g[i][1:]
            for j in range(1,16):
                c[f'{e}'][f'{j}'] = g[i+j]
            c[f'{e}'][f'{17}']=g[i+17]
            e+=1
        except:
            print(g[i:])

# print(c)
with open('dts.json','wb') as f:
    f.write(str(c).replace("'",'"').encode('utf-8'))

# print('\ufeff')