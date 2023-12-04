import re
import requests

site = requests.get('http://www.columbia.edu/~fdc/sample.html')

result = re.findall(r"<h3.*>(?P<name>.*)</h3>", site.text)
print(result)
