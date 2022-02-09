import re

embeded_url = "https://streamm4u.club/api/source/z7ek8ijkqwp33l8"
embeded_id = re.split(r"/", embeded_url)[-1]
print(embeded_id)
