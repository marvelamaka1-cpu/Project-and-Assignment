# Student Score Analyzer

A Python-based CSV analysis tool that reads student or employee data from CSV files and generates useful insights and statistics.

## Features

* Load data from CSV files
* Analyze student scores and performance
* Calculate summary statistics

  * Average score
  * Highest score
  * Lowest score
* Display data in a readable format
* Support for employee data analysis from CSV files

## Requirements

* Python 3.x

## Project Structure

```text
.
├── main.py
├── students.csv
├── employees.csv
└── README.md
```

## Usage

Run the program:

```bash
python main.py
```

The program will read the CSV file and display the analysis results.

## Example Data

### students.csv

```csv
Name,Score
John,85
Mary,92
Peter,78
```

### employees.csv

```csv
Name,Department,Salary
Alice,IT,50000
Bob,HR,45000
Charlie,Finance,60000
```

## Example Output

```text
Average Score: 85.0
Highest Score: 92
Lowest Score: 78
```

## Future Improvements

* Data visualization
* Export reports
* Support for multiple CSV formats
* Interactive command-line interface

## License

This project is open source and available for learning and educational purposes.
