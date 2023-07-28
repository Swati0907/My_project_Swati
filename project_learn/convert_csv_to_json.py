import csv
import json

csvFilePath = r'/home/myshubhlife/Downloads/osv_with_aggregator_id.csv'
jsonFilePath = r'/home/myshubhlife/Downloads/osv_with_aggregator_id.json'


def make_json(csvFilePath, jsonFilePath):
    data = {}
    with open(csvFilePath, encoding='utf-8') as f:
        csvReader = csv.DictReader(f)
        for rows in csvReader:
            key = rows['empId']
            data[key] = rows
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


make_json(csvFilePath, jsonFilePath)
