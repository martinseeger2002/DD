import json
import re

def get_number_from_name(name):
    match = re.search(r'\d+', name)
    return int(match.group()) if match else float('inf')

def reorder_json(input_file, output_file):
    # Read the input JSON file
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Sort the data based on the number in the name field
    sorted_data = sorted(data, key=lambda x: get_number_from_name(x['name']))

    # Write the sorted data to the output JSON file
    with open(output_file, 'w') as file:
        json.dump(sorted_data, file, indent=4)

def main():
    input_file = 'doginaldogs.json'
    output_file = 'sorted_doginaldogs.json'
    reorder_json(input_file, output_file)
    print("JSON data reordered and saved to new file.")

if __name__ == "__main__":
    main()
