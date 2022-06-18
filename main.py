from modules.functions import *
import json
import time

ct = time.time()

# res = live('http://www.tsetmc.com/tsev2/data/instinfofast.aspx?i=65883838195688438&c=34')
res = live('http://www.tsetmc.com/tsev2/data/MarketWatchPlus.aspx')

print(res[0])
print(res[1])
# data = {
#     'tsetmc.com/dideban' : [
#         {
#             'ID' : res[0],
#             'code' : res[2],
#             'namad' : res[3],
#             'name' : res[4],
#             'time' : res[5],
#             'avalin' : res[6],
#             'gheymat payani' : res[7],
#             'akharin moamele' : res[8],
#             'teedad' : res[9],
#             'hajm' : res[10],
#             'arzesh' : res[12],
#             'kamtarin' : res[13],
#             'bishtarin' : res[14],
#             'diroz' : res[15],
#             'EPS' : res[16],
#             'mabna' : res[17],
#             'unkown' : res[18],
#             'teedadforosh' : res[19],
#             'unkown' : res[20],
#             'min gheumat mojaz' : res[21],
#             'max gheymat mojaz' : res[22],
#             'unkown' : res[23],
#             'unkown' : res[24],

#         }

#     ]
# }


# json_string = json.dumps(data)
# with open('assets/json/tsetmc-{}.json'.format(ct), 'w') as outfile:
#     outfile.write(json_string)
# print('done!')