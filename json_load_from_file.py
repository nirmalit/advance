import json
x=open("json_file.json","r")
y=x.readline()
z=json.loads(y)
print(z.keys())
