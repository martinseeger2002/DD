import json
import re

def get_number_from_name(name):
    match = re.search(r'\d+', name)
    return int(match.group()) if match else None

def find_missing_numbers(data, total_range):
    present_numbers = {get_number_from_name(item['name']) for item in data}
    all_numbers = set(range(1, total_range + 1))
    missing_numbers = sorted(all_numbers - present_numbers)
    return missing_numbers

def main():
    input_file = 'sorted_doginaldogs.json'
    total_range = 10000

    # Read the input JSON file
    with open(input_file, 'r') as file:
        data = json.load(file)

    missing_numbers = find_missing_numbers(data, total_range)
    print(f"Missing numbers: {missing_numbers}")

if __name__ == "__main__":
    main()
