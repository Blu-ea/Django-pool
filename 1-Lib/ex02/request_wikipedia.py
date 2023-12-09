import json, dewiki, sys
from requests import api

def get_wiki(input: str):

	acces_point = "https://en.wikipedia.org/w/api.php"

	
	search = api.get(f"{acces_point}?action=opensearch&format=json&search={input}&formatversion=2").json()
	if (not len(search[1])):
		print (f"Nothing found for {input}")
		return
	result_search = search[1][0]
	print (f"Found result for {result_search}")


	page = api.get(f"{acces_point}?action=parse&format=json&page={result_search}&prop=wikitext&redirects=true").json()
	if "error" in page:
		print (page["error"]["info"])
		return


	page = page["parse"]["wikitext"]["*"]
	page = dewiki.from_string(page)

	file = open(f"{input}.wiki", 'w')
	file.write(page)


if (__name__ == "__main__"):
	if (len(sys.argv) == 2):
		get_wiki(sys.argv[1])
	else:
		print(f"Error: Expected 1 arumgment, got {len(sys.argv) - 1}")
