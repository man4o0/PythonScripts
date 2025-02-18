from tld import get_tld
from urllib.parse import urlparse

# Read URLs from the file
with open('all_urls.txt', 'r') as file:
    urls = file.readlines()

formatted_urls = set()

for url in urls:
    url = url.strip()
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    try:
        res = get_tld(url, as_object=True)
        formatted_urls.add(res.fld)
    except Exception as e:
        print(f"Error processing URL {url}: {e}")

# Print out the formatted URLs with '*.' wildcard , ex. sonarsource.com -> *.sonarsource.com
print('\n'.join(f'*.{x}' for x in formatted_urls))

