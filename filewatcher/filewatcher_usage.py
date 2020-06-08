# pip install filewatcher


import filewatcher


# Retrieves files information from sub-directories too if recuresively=True
files_info_dict = filewatcher.get_files_info(directory='/home/krishna/mygit-repos/',recursively=True,sortbytime=False)

# Doesn't retrieve files information from sub-directories if recursively=False
files_info_dict = filewatcher.get_files_info(directory='/home/krishna/mygit-repos/',recursively=False,sortbytime=True)

for k,v in files_info_dict.items():
	print('key:', k)
	print('value:')
	# path attribute consists of file path in str
	print('path: '+ v.path)
	# name attribute consists of file name in str
	print('name: '+ v.name)
	# size attribute consists of file size in str
	print('size: '+ v.size)
	# time attribute consists of file modified time in datetime
	print('time: '+ v.time.strftime('%d%m%Y%H%M%S'))
	# text attribute consists of retrival data type deatails in str
	print('text: '+ v.text)

'''
output:
key: /home/krishna/mygit-repos/New Empty File_08062020010939
value:
path: /home/krishna/mygit-repos/New Empty File
name: New Empty File
size: 8 B
time: 08062020010939
text: Information
'''
