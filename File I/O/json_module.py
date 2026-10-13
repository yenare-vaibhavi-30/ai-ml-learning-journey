# import json
# json_str = '{"name":"Vaibhavi", "isStudent": true,}'
# py_obj = json.loads(json_str)
# print(type(py_obj), py_obj)

# import json

# student = {
#      "name":"Vaibhavi",
#      "age":22,
#      "course": "MCA"
# }
# data = json.dumps(student)
# print(data)
# print(type(data))


import json

student = {
     "name": "vaibhavi",
     "age": 22,
     "course": "MCA"
}

with open("Student.json", "w") as file:
     json.dump(student, file, indent=4)