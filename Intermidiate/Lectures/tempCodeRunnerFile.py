import json

sports = ['cricket' , 'kabaddi' , 'tennis' , 'badminton']

dict_enumerate = dict(list(enumerate(sports , 1)))

f = open('dict_enumerate.json' , 'w')
json.dump(dict_enumerate , f)

f.close()