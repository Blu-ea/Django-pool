import sys
from antigravity import geohash

if __name__ == "__main__":
	if (len(sys.argv) == 4):
		try:
			geohash(float(sys.argv[1]), float(sys.argv[2]), bytes(sys.argv[3], 'UTF-8'))
		except Exception as e:
			print (f"Error: {e}")
	else:
		print("Error :Wrong number of arguments\nExemple: python3 geohashing.py 53.124546 -27.11156 2023-05-20-12345.67")
