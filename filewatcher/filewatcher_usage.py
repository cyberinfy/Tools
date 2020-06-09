# pip install filewatcher


from filewatcher import getinfo

'''_______________________________________________
|getinfo    - Keyword Arguments:                  |
|_________________________________________________|
directory   - The location you want to capture files from
filemask    - To specify file type, Use '*' to retrive info of all files
recursively - Get files information from sub-directories too if value is True 
sortbytime  - Sorts the file_info_dict based on last modified time
showprint   - Prints a file_info object in console after each retrival if value is True

__________________________________________________
|getinfo - Returns a dict object for each file:   |
|_________________________________________________|
key	 - filepath+lastmodifiedtime.strftime(%d%m%Y%H%M%S)
value	 - a FileInfo object

__________________________________________________
|FileInfo object - Attributes                     |
|_________________________________________________|
path		 - file full path as a string
name		 - file name as a string
size		 - file size in maximum possible unit like MB, GB etc as a string
time		 - file modified time as a datetime object
'''


files_info_dict = getinfo(directory='/home/krishna/mygit-repos/',filemask='*.png',recursively=True,sortbytime=True,showprint=True)

files_info_dict = getinfo(directory='/home/krishna/mygit-repos/',filemask='*',recursively=False,sortbytime=False,showprint=False)

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
Execution:
> python filewatcher_usage.py 
 path: /home/krishna/mygit-repos/Arch-Linux/Window-Managers/DWM/Wallpapers/Spider Verse.png
 name: Spider Verse.png
 size: 81.35 KB
 time:2020-06-05 08:36:42.560497
key: /home/krishna/mygit-repos/New Empty File_08062020010939
value:
path: /home/krishna/mygit-repos/New Empty File
name: New Empty File
size: 8 B
time: 08062020010939
text: Information
'''
