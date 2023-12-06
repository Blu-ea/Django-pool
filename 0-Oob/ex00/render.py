import sys, os, re
import settings

def render(file_name: str):
	# patern = re.compile()
	if not re.match("^.*\.template$" ,file_name):
		print("Wrong extension file")
		return
	if not os.access(file_name, os.R_OK):
		print("This file does not exist")
		return
	file = open(file_name, 'r')
	data = settings.__dict__
	lines = "".join(file.readlines())
	lines = lines.format(**data)
	out_file_name = os.path.splitext(file_name)[0] + ".html"
	out_file = open(out_file_name, 'w')
	out_file.write(lines)

if (__name__ == "__main__"):
	if (len(sys.argv) == 2):
		render(sys.argv[1])