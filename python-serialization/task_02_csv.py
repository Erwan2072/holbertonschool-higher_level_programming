#!/usr/bin/env python3
"""Converting CSV Data to JSON Format"""

import csv
import json


def convert_csv_to_json(csv):
    """Converts data from a CSV file to a JSON file."""
    try:
        """Initialize an empty list to store the CSV data"""

        with open(csv, "r", newline='') as csv_file:
            """Create a CSV DictReader object"""
            csv_read = csv.DictReader(csv_file)
            data = [ row for row in csv_read]

        """ write the json file"""
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        print("An error occurred: {}".format(e))
        return False
