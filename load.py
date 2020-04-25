import json
jason_str = '[{"username": "wei", "age": "17", "country": "taiwang"}, {"username": "chan", "age": "12", "country": "china"}]'
persons = json.loads(jason_str)
print(type(persons))
for person in persons:
    print(person)