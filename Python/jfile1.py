import json
with open ("jfile.json", 'r') as sr:
    data = json.load(sr)
    for package_name, versions in data.items():
        for version, attributes in versions.items():
            #print(version)
            #print(attributes)
            if version == '5.3.13':
                #for i in attributes.items():
                #print(i)
                with open ("json_output", 'w') as sr:
                    json.dump(attributes, sr, indent=4)
                    print(f"version = {version} details copied to json_output")
