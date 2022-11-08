#!/usr/bin/env python3

from os.path import exists

import argparse
import csv

class bcolours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def welcome():
  print("Parse Nessus CSV to output issues based on template file.")
  print()

def main():
    parser = argparse.ArgumentParser(description="Parse Nessus CSV to output issues based on template file.")
    parser.add_argument("--csv", required=True,
                        help="Nessus CSV file")
    parser.add_argument("--template", required=True,
                        help="Template to build issues from")

    parsed = parser.parse_args()

    # Open file
    csv_file = csv.DictReader(open(paresd.csv))
    for row in csv_file:
      print(row)

if __name__ == "__main__":
    main()
