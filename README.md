# CSV Analysis and Visualization Tool

This project is a command-line tool for analyzing and visualizing CSV data. It allows users to load a CSV file, explore its contents, and generate visualizations for categorical and time-based data.

## Features

- **List Available Files**: Displays all files in the current directory for selection.
- **Load CSV Data**: Reads a CSV file and stores its content as a list of dictionaries.
- **View Dataset Information**: Shows the first five rows, total row count, and column names.
- **Categorical Data Visualization**: Generates bar charts for selected categorical columns.
- **Time-Based Data Visualization**: Creates line charts for datetime-based columns.

## Requirements

Ensure you have the following dependencies installed:

```bash
pip install matplotlib
```

## Usage

1. Run the script:

   ```bash
   python CSVAnalysis.py
   ```

2. Select a CSV file from the list.
3. Choose from the menu options to:
   - View dataset information.
   - Visualize categorical data.
   - Visualize time-based data.

## Example

When executed, the script will guide you through selecting a CSV file and choosing an analysis option.

```
Welcome to the Generic CSV Analysis and Visualization Tool!
Files in the current directory:
1. data.csv
2. report.csv

Enter the number of the file you want to load: 1

File 'data.csv' loaded successfully!

=== Data Analysis Menu ===
1. View first 5 rows and dataset info.
2. Visualize a categorical column (e.g., Levels, Sources).
3. Visualize a time-based column (e.g., Date and Time).
4. Exit analysis.
```

## License

This project is licensed under the MIT License.
