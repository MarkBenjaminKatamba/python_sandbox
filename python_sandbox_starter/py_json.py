# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON
userJSON = '{"firstName": "Rhaimes", "lastName": "Global", "age": 30}'

# Parse to dict
user = json.loads(userJSON)

print(user)
print(user['firstName'])

# Doing the opposite: Taking a dict and turning it into json format
car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON = json.dumps(car)

print(carJSON)