import json
with open("j.json","r") as f:
    x=json.loads(f)
    print(x["name"])
    
