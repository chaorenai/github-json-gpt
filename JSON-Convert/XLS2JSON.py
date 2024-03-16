import xlrd
import json

def xls_to_json(xls_file, json_file):
    workbook = xlrd.open_workbook(xls_file)
    sheet = workbook.sheet_by_index(0)
    data = {'content': [[sheet.cell_value(row, col) for col in range(sheet.ncols)] for row in range(sheet.nrows)]}
    with open(json_file, 'w') as jf:
        json.dump(data, jf, indent=4)

xls_to_json('path/to/your/example.xls', 'path/to/your/example.json')