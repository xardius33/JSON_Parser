import json

def parse_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        print(json.dumps(data, indent=4))

# Usage
file_path = 'data.json'  # Replace with your JSON file path
parse_json(file_path)
