"""phone_no={
    'ram':1234,
    'shyam':3456,
    'mona':123, #whether comma or not no error 
}
print(phone_no)

phone_no={
    'ram':1234,
    'shyam':3456,
    'mona':123, #whether comma or not no error 
}
print(phone_no['ram'])

phone_no={
    'ram':1234,
    'shyam':3456,
    'ram':123, #whether comma or not no error 
}
print(phone_no)

phone_no=dict({
    'ram':1234,
    'shyam':3456,
})
print(phone_no)


phone_no = dict([('ram', 1234), ('shyam', 3456)])
print(phone_no)
#modyfying the dictionary
phone_no=dict({
    'ram':1234,
    'shyam':3456,
})
print(phone_no)
phone_no['ram']=9999
print(phone_no)

phone_no=dict({
    'ram':1234,
    'shyam':3456,
})
print(phone_no)
phone_no['ram']={9,9,99}
print(phone_no)

phone_no=dict({
    'ram':1234,
    'shyam':3456,
})
print(phone_no)
phone_no['ram']={'siva':9,'gk':99}
print(phone_no)
print(phone_no['ram'])
print(phone_no['ram']['siva'])
print(phone_no.get('ram'))
print(phone_no.get('Ram'))#other than get method key is wrong means error
del phone_no['ram']
print(phone_no)

data={
    1:'jemmy',
    2:'phone',
    0:'mohan'
}
print(data[0]) #its not index its key
del data[1]
print(data)
print(data.pop(0))
print(data)

phone_no=dict({
    'ram':1234,
    'shyam':3456,
})
print(phone_no)
print(phone_no.popitem())#delete the last one
phone_no.clear()
print(phone_no)
"""
phone_no=dict({
    'ram':1234,
    'shyam':3456,
})
print(phone_no.keys())
print(phone_no.values())
print(phone_no.items())
"""
phone_no=dict({
    'ram':1234,
    'shyam':3456,
})
for i in phone_no:
    print(i)

phone_no=dict({
    'ram':1234,
    'shyam':3456,
})
for i in phone_no:
    print(phone_no[i])
phone_no=dict({
    'ram':1234,
    'shyam':3456,
})
for i in phone_no.items():
    print(i)

phone_no=dict({
    'ram':1234,
    'shyam':3456,
})
print(phone_no)
p=phone_no.copy()
print(p)
print(len(p))

#nested dictionaries & list

data={
    "Ram":{"roll_no":10,"age":20,"course":"python"},
     "Ra":{"roll_no":100,"age":920,"course":"pytn"}
}
print(data)
print(data["Ra"])
print(data["Ra"]["roll_no"])
data["Ram"]["phone_no"]=1234
print(data)
del data["Ram"]["phone_no"]
print(data)
print(data["Ra"].pop("roll_no"))


travel_data={
    "Alaska":["Northen lights","snow","nightsky"],
    "Australia":["Kangaroo","stevesmith"]
}
print(travel_data["Alaska"])

travel_data = [
    {
        "Ram": 2,
        "roll_no": 10,
        "age": 20,
        "course": "python"
    },
    {
        "Ra": 9,
        "roll_no": 100,
        "age": 920,
        "course": "pytn",
        "phone": [123, 44]
    }
]

print(travel_data)
print(travel_data[1])
print(travel_data[1]["phone"])
"""
from collections import defaultdict
from typing import List

def findDuplicates(nums: List[int]) -> List[int]:
    # Initialize a defaultdict with default value of 0
    d = defaultdict(int)
    
    # List to store duplicate elements
    duplicates = []
    
    # Count occurrences of each element in nums
    for num in nums:
        d[num] += 1
    
    # Find elements with count equal to 2 (duplicates)
    for num, count in d.items():
        if count == 2:
            duplicates.append(num)
    
    return duplicates

# Test the function
nums = [4, 3, 2, 7, 8, 2, 3, 1]  # Example input
result = findDuplicates(nums)
print("Duplicates:", result)

