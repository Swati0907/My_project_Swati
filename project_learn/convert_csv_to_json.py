import csv
import json


def csv_to_json(csv_file):
    data = {}
    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)

        for row in reader:
            key = row[0]
            values = {headers[i]: row[i] for i in range(1, len(row))}
            data[key] = values

    return json.dumps(data, indent=4)


csv_file_path = '/home/myshubhlife/Downloads/osv_with_aggregator_id (1).csv'
json_data = csv_to_json(csv_file_path)

with open('/home/myshubhlife/Downloads/osv_with_aggregator_id145.json', 'w') as jsonfile:
    jsonfile.write(json_data)

print("Conversion completed. JSON file saved as 'output.json'")
