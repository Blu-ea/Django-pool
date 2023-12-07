import sys
from antigravity import geohash

def antigrav(long, lat, date) -> None:
	hash = geohash(latitude=float(lat), longitude=float(long), datedow=bytes(date, encoding="UTF-8"))
	print (hash)

if __name__ == "__main__":
	if (len(sys.argv) == 4):
		try:
			antigrav(sys.argv[1], sys.argv[2], sys.argv[3])
		except Exception as e:
			print (f"Error: {e}")
	else:
		print ("Error :Wrong number of arguments\nExemple: python3 geohashing.py 53.124546 -27.11156 2023-05-20-12345.67")
