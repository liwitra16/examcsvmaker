import pandas as pd
import json

# Function to load JSON file with explicit encoding
def load_json_file(json_file_path):
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File not found: {json_file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON: {json_file_path}")
        return None

# Function to create DataFrame and save to CSV
def create_csv_from_json(json_file_path):
    data = load_json_file(json_file_path)
    if data is not None:
        # Define DataFrame with appropriate columns
        df = pd.DataFrame(data, columns=[
            "Question", "Option A", "Option B", "Option C", "Option D", "Option E", "Correct Answer"
        ])
        
        # Generate CSV file name
        csv_file_path = json_file_path.replace('.json', '.csv')
        
        # Save DataFrame to CSV
        df.to_csv(csv_file_path, index=False, sep=';')
        print(f"CSV file created: {csv_file_path}")
    else:
        print("Failed to create CSV due to JSON loading error.")

# Main function to prompt user
def main():
    json_file_path = input("Please enter the name of the JSON file (including .json extension): ")
    create_csv_from_json(json_file_path)

# Run the main function
if __name__ == "__main__":
    main()
