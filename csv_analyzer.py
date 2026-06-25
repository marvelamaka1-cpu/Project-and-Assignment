  
#!/usr/bin/env python3
"""
CSV Data Analyzer — Mini Project 1
Reads a CSV file and prints statistical summaries for each column.
"""

import csv
import sys
import json
from pathlib import Path


# ---------------- READ CSV ----------------
def read_csv(filename):
    path = Path(filename)

    if not path.exists():
        raise FileNotFoundError(f"File '{filename}' not found.")

    with path.open("r") as file:
        reader = csv.DictReader(file)
        data = list(reader)

    if not data:
        raise ValueError("CSV file is empty")

    return data


# ---------------- DETECT NUMERIC ----------------
def detect_numeric(data):
    numeric_cols = []

    for col in data[0].keys():
        is_numeric = True

        for row in data:
            try:
                float(row[col])
            except:
                is_numeric = False
                break

        if is_numeric:
            numeric_cols.append(col)

    return numeric_cols


# ---------------- CALCULATE STATS ----------------
def calculate_stats(values):
    nums = [float(v) for v in values]

    return {
        "count": len(nums),
        "sum": sum(nums),
        "mean": sum(nums) / len(nums),
        "min": min(nums),
        "max": max(nums)
    }


# ---------------- FORMAT REPORT ----------------
def format_report(data, filename):
    report = {}

    columns = data[0].keys()
    numeric_cols = detect_numeric(data)

    print("\n" + "=" * 60)
    print("CSV ANALYSIS REPORT")
    print("=" * 60)

    print(f"File: {filename}")
    print(f"Total rows: {len(data)}")
    print(f"Total columns: {len(columns)}")

    print("\nNUMERIC COLUMNS:")
    print("-" * 60)

    for col in columns:
        values = [row[col] for row in data]

        if col in numeric_cols:
            stats = calculate_stats(values)
            report[col] = stats

            print(f"\nColumn: {col}")
            print(f"Count : {stats['count']}")
            print(f"Sum   : {stats['sum']:.2f}")
            print(f"Mean  : {stats['mean']:.2f}")
            print(f"Min   : {stats['min']:.2f}")
            print(f"Max   : {stats['max']:.2f}")

    print("\nNON-NUMERIC COLUMNS:")
    print("-" * 60)

    for col in columns:
        if col not in numeric_cols:
            values = [row[col] for row in data]
            unique_vals = set(values)

            report[col] = {
                "count": len(values),
                "unique": len(unique_vals)
            }

            print(f"\nColumn: {col} → {len(values)} values, {len(unique_vals)} unique")

    print("\n" + "=" * 60)

    return report


# ---------------- SAVE JSON ----------------
def save_json(report, filename="report.json"):
    with open(filename, "w") as f:
        json.dump(report, f, indent=4)

    print(f"Report saved to {filename}")


# ---------------- MAIN ----------------
def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter CSV filename: ").strip()

    try:
        data = read_csv(filename)
        report = format_report(data, filename)

        # BONUS: JSON export
        if "--output" in sys.argv:
            index = sys.argv.index("--output")

            if index + 1 < len(sys.argv) and sys.argv[index + 1] == "json":
                save_json(report)

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()