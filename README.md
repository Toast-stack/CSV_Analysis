# **CSV Analysis and Visualization Tool**

Welcome to the **CSV Analysis and Visualization Tool**, an interactive Python script designed for analyzing and visualizing data stored in CSV files. This tool is flexible, user-friendly, and can adapt to various CSV file formats.

## **Features**
- Dynamic file selection for seamless analysis.
- Automatically adapts to CSVs with different column structures.
- Provides data visualizations such as bar charts and line graphs for better insights.
- Handles invalid or missing data gracefully.

## **Installation**
To use the CSV Analysis and Visualization Tool, follow these steps:

1. Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/).
2. Install the required library `matplotlib` for data visualization by running the following command in your terminal:
   ```bash
   pip install matplotlib

## **Usage**
1. Clone or download this repository to your local machine.
2. Navigate to the directory containing the script and your CSV files.
3. Run the script using the following command:
   ```bash
   python csv_analysis_tool.py

## **How It Works**
### **File Selection**
- When you start the program, the tool lists all the files in the current directory.
- You can select a CSV file to analyze by entering the corresponding number from the displayed list.

### **Analysis Menu**
Once you load a CSV file, the program provides the following options:
1. **View Dataset Info**:
   - Displays the first 5 rows of your CSV file along with the total number of rows and column names.
2. **Visualize Categorical Data**:
   - Choose any column with categorical values (e.g., event level, source) to generate a bar chart that shows the distribution of values in the selected column.
3. **Visualize Time-Based Data**:
   - Select a column containing datetime values to create a line chart that displays the frequency of events or entries over time.
4. **Exit Analysis**:
   - Allows you to close the program once your analysis is complete.

### **Error Handling**
- The script automatically skips empty or invalid entries while processing data.
- If you select an invalid menu option, you’ll be prompted to try again.

## **Examples**
### **Bar Chart**
Visualizing the distribution of event levels (e.g., Error, Warning):
```plaintext
Bar Chart Title: Distribution of Event Levels
X-Axis: Levels (Error, Warning)
Y-Axis: Count of Occurrences
