from local_lib.path import Path


def path_test(folder_name, file_name, file_content):
	Path(folder_name).mkdir_p().cd()
	file = Path(file_name)
	file.write_text(file_content)
	file_content = file.read_text()
	print (file_content)

if (__name__ == "__main__"):
	
	folder_name="test_Folder"
	file_name="test_File"
	file_content="Je suis un fichier :D"
	path_test(folder_name, file_name, file_content)