



import json

x='{"name":"ramjeet","age":28,"country":"india"}'

y=json.loads(x)
print(y["age"])


import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
