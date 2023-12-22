import json
import requests


r = requests.get('https://formulae.brew.sh/api/analytics-linux/install/30d.json')
print(r)

packages_json = r.json()
packages_str = json.dumps(packages_json, indent=2)


print(packages_json)