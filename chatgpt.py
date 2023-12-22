import json

def sort_json(json_data, key):
    sorted_data = sorted(json_data, key=lambda x: x[key])
    return sorted_data

# Example JSON data
json_data = '''
[
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20}
]
'''

# Load JSON data
data = json.loads(json_data)

# Sort JSON data by the "name" key
sorted_data = sort_json(data, "name")

# Print sorted JSON data
for item in sorted_data:
    print(item)
