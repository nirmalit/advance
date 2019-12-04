import json
x='[{"name":"a","age":23},{"name":"b","age":25},{"name":"c","age":22}]'
y=json.loads(x)
for i in range(0,3):
    z=dict(y[i])
    print("my name is ",end="")
    print(z["name"],end="")
    print(" and i am ",end="")
    print(z["age"])
    
