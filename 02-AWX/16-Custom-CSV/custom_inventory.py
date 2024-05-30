#!/usr/bin/env python

import csv
import json
import re
import sys

def load_csv(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def filter_hosts(data, regex):
    pattern = re.compile(regex)
    return [row for row in data if pattern.match(row['Hostname'])]

def generate_inventory(data):
    inventory = {"all": {"hosts": {}, "children": {}}}
    for item in data:
        hostname = item['Hostname']
        ip_address = item['IP Address']
        group = item['Group']

        if group not in inventory["all"]["children"]:
            inventory["all"]["children"][group] = {"hosts": {}}

        inventory["all"]["children"][group]["hosts"][hostname] = {"ansible_host": ip_address}

    return inventory

def main():
    csv_file_path = sys.argv[1]
    regex_filter = sys.argv[2]

    data = load_csv(csv_file_path)
    filtered_data = filter_hosts(data, regex_filter)
    inventory = generate_inventory(filtered_data)

    print(json.dumps(inventory, indent=2))

if __name__ == "__main__":
    main()

