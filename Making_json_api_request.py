import requests
req=requests.get("https://swapi.dev/api/people/5/")
print(req.json())          #it will print the site json data
person=req.json()           #giving a variable name to json file(actually it is now dictionary)

print(f"Name:\t\t{person['name']}")                             #accessing key-value pair of dictionary
print(f"height:\t\t{person['height']}")
print(f"mass:\t\t{person['mass']}")


for i in person['films']:
    print(f"films are {i} movies")

print(type(person))




#request is used to check website status