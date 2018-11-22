import pandas as pd
import json
import os


def create_json_for_semantic_substract(df, key_to_groupby, json_output_file):

	imports = df.groupby('from').to.agg(list)
	imports.index.name = "name"
	imports.name = "imports"

	json_data = json.loads(imports.to_json(orient='table'))['data']

	with open (json_output_file, mode='w') as json_file:
		json_file.write(json.dumps(json_data, indent=3).replace("null", ""))

	print("JSON file produced in '{}'".format(os.path.abspath(json_output_file)))