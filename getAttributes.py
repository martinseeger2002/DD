import json

def extract_unique_attributes(input_file, output_file):
    unique_attributes = {}

    # Read the input JSON file
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Iterate through each item in the JSON data
    for item in data:
        attributes = item.get("attributes", {})
        for key, value in attributes.items():
            if key not in unique_attributes:
                unique_attributes[key] = set()
            unique_attributes[key].add(value)

    # Write the unique attributes and their values to the output text file
    with open(output_file, 'w') as file:
        for key, values in unique_attributes.items():
            file.write(f"{key}:\n")
            for value in sorted(values):
                file.write(f"  - {value}\n")
            file.write("\n")

def main():
    input_file = 'doginaldogs.json'
    output_file = 'unique_attributes.txt'
    extract_unique_attributes(input_file, output_file)
    print(f"Unique attributes and their values have been saved to {output_file}.")

if __name__ == "__main__":
    main()
