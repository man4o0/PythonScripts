from tld import get_tld
urls = [
    "https://google.com", "https://yahoo.co.uk"
]
formatted_urls = set()
for url in urls:
    res = get_tld(url, as_object=True)

    formatted_urls.add(res.fld)

print('\n'.join('*.' + x for x in formatted_urls))

## Example output: *.google.com
################## *.yahoo.co.uk
