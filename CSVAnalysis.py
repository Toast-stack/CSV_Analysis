import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

# Function to list files in the current directory
def list_files_in_directory():
    """List all files in the current directory."""
    print("\nFiles in the current directory:")
    files = os.listdir(os.getcwd())
    for idx, file in enumerate(files, start=1):
        print(f"{idx}. {file}")
    return files

# Function to load a CSV file
def load_csv():
    """Prompt the user to select a CSV file to load into a list of dictionaries."""
    files = list_files_in_directory()

    while True:
        try:
            file_index = int(input("\nEnter the number of the file you want to load: ")) - 1
            if file_index < 0 or file_index >= len(files):
                print("Invalid choice. Please select a valid file number.")
                continue
            file_name = files[file_index]
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    file_path = os.path.join(os.getcwd(), file_name)

    try:
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            data = list(reader)
            print(f"\nFile '{file_name}' loaded successfully!")
            return data
    except Exception as e:
        print(f"Error loading the file: {e}")
        return None

# Function to display dataset information
def display_data(data):
    """Display basic information about the dataset."""
    if not data:
        print("\nNo data to display!")
        return

    print("\nFirst 5 rows of the dataset:")
    for row in data[:5]:
        print(row)

    print(f"\nTotal rows: {len(data)}")
    print(f"Columns: {list(data[0].keys())}")

# Function to visualize a categorical column
def visualize_categorical(data):
    """Create a bar chart for a selected categorical column."""
    columns = list(data[0].keys())
    print("\nColumns available:")
    for idx, column in enumerate(columns, start=1):
        print(f"{idx}. {column}")

    # User selects column for visualization
    while True:
        try:
            column_index = int(input("\nEnter the number of the column to visualize: ")) - 1
            if column_index < 0 or column_index >= len(columns):
                print("Invalid choice. Please select a valid column number.")
                continue
            column_name = columns[column_index]
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Count occurrences of unique values
    values = [row[column_name] for row in data if row[column_name].strip()]
    value_counts = {value: values.count(value) for value in set(values)}

    # Create the bar chart
    plt.bar(value_counts.keys(), value_counts.values(), color='blue')
    plt.title(f"Distribution of {column_name}")
    plt.xlabel(column_name)
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Function to visualize time-based data
def visualize_time_based(data):
    """Create a line chart for a selected datetime column."""
    columns = list(data[0].keys())
    print("\nColumns available:")
    for idx, column in enumerate(columns, start=1):
        print(f"{idx}. {column}")

    # User selects the datetime column
    while True:
        try:
            column_index = int(input("\nEnter the number of the column with datetime data: ")) - 1
            if column_index < 0 or column_index >= len(columns):
                print("Invalid choice. Please select a valid column number.")
                continue
            column_name = columns[column_index]
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Parse and count occurrences by date
    date_strings = [row[column_name] for row in data if row[column_name].strip()]
    dates = []
    for date_str in date_strings:
        try:
            date = datetime.strptime(date_str, "%m/%d/%Y %H:%M")
            dates.append(date.date())
        except ValueError:
            print(f"Skipping invalid date format: {date_str}")

    # Count occurrences by day
    date_counts = {day: dates.count(day) for day in set(dates)}

    # Create the line chart
    plt.plot(list(date_counts.keys()), list(date_counts.values()), marker='o')
    plt.title(f"Events Over Time ({column_name})")
    plt.xlabel("Date")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main menu function
def analyze_data(data):
    """Provide options to analyze the dataset."""
    while True:
        print("\n=== Data Analysis Menu ===")
        print("1. View first 5 rows and dataset info.")
        print("2. Visualize a categorical column (e.g., Levels, Sources).")
        print("3. Visualize a time-based column (e.g., Date and Time).")
        print("4. Exit analysis.")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            display_data(data)
        elif choice == "2":
            visualize_categorical(data)
        elif choice == "3":
            visualize_time_based(data)
        elif choice == "4":
            print("\nExiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    """Main program logic."""
    print("Welcome to the Generic CSV Analysis and Visualization Tool!")
    data = load_csv()
    if data:
        analyze_data(data)

if __name__ == "__main__":
    main()
