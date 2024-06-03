import json

# Define a dictionary for common colors and their inverted colors
color_inversion = {
    "Aqua": "Fuchsia",
    "Blue": "Yellow",
    "Green": "Magenta",
    "Pink": "Cyan",
    "Purple": "Green",
    "Red": "Cyan",
    "Rose": "Cyan",
    "Tan": "Blue",
    "Yellow": "Blue",
    "Beige": "Navy",
    "Black": "White",
    "Bronze": "Cyan",
    "Brown": "Cyan",
    "Diamond": "Black",
    "Gold": "Blue",
    "Gray": "Gray",
    "Orange": "Blue",
    "Rose Gold": "Cyan",
    "Silver": "Black",
    "White": "Black",
}

def invert_color(color):
    return color_inversion.get(color, color)

def invert_colors_in_json(input_file, output_file):
    # Read the input JSON file
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Iterate through each item in the JSON data
    for item in data:
        attributes = item.get("attributes", {})
        for key, value in attributes.items():
            if key in ["Background", "Fur Color"] and value in color_inversion:
                attributes[key] = invert_color(value)

    # Write the updated data to the output JSON file
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    input_file = 'sorted_doginaldogs.json'
    output_file = 'inverted_doginaldogs.json'
    invert_colors_in_json(input_file, output_file)
    print(f"Colors inverted and saved to {output_file}.")

if __name__ == "__main__":
    main()
