import json
   
with open('10%threshold_data.json', 'r+') as data:
	d=json.load(data)
	
	def walk(d, level=""):
		d["id"] = level
		children = d.get("children")
		if children:
			for i, child in enumerate(children, 1):
				walk(child, level + "." + str(i))
				
	walk(d["tree"])

	data.seek(0)        # <--- should reset file position to the beginning.
	json.dump(d, data, indent=4)
	data.truncate()     # remove remaining part