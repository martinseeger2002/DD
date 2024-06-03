import json

def remove_txid_from_json(input_file, output_file):
    # Read the input JSON file
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Function to recursively remove txid from dictionaries
    def remove_txid(obj):
        if isinstance(obj, dict):
            if 'txid' in obj:
                del obj['txid']
            for key, value in obj.items():
                remove_txid(value)
        elif isinstance(obj, list):
            for item in obj:
                remove_txid(item)

    # Remove txid from the JSON data
    remove_txid(data)

    # Write the updated data to the output JSON file
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    input_file = 'inverted_doginaldogs.json'
    output_file = 'inverted_doginaldogsOUT.json'
    remove_txid_from_json(input_file, output_file)
    print(f"txid fields removed and updated JSON saved to {output_file}.")

if __name__ == "__main__":
    main()
