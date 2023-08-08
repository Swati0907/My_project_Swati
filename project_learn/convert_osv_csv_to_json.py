import csv
import json

csvFilePath = r'/home/myshubhlife/Downloads/osv_with_aggregator_id (1).csv'
jsonFilePath = r'/home/myshubhlife/Downloads/osv_with_aggregator_id9.json'

def make_json(csvFilePath, jsonFilePath):
    data = {}
    with open(csvFilePath, 'r') as f:
        csvReader = csv.DictReader(f)
        for rows in csvReader:
            key = rows['empId']
            if key not in data:
                data[key] = []  # Create an empty list for each unique key

            # Append a new dictionary to the list for each row in the CSV
            data[key].append({
                'key_1': rows['aggregatorId'],
                'key_2': rows['agentName'],
                'key_3': rows['empId']
            })

    with open(jsonFilePath, 'w') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

make_json(csvFilePath, jsonFilePath)
