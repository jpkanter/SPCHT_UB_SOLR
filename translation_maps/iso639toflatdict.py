import json

file = open("./iso639-indent.json", "r")
data = json.load(file)

file.close()

results = {}

for entry in data:
    if entry.get('http://www.loc.gov/mads/rdf/v1#authoritativeLabel') is not None:
        for label in entry['http://www.loc.gov/mads/rdf/v1#authoritativeLabel']:
            if label['@language'] == "en":
                results[label['@value']] = entry['@id']
                break

file = open("./languages_long.json", "w")

json.dump(results, file, indent=3)
file.close()
