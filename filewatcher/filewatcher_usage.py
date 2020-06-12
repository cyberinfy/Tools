from filewatcher import glob, sortfilesby, getdict

if __name__=='__main__':
	
	# location from where the files information is required
	directory = '/run/media/krishna/Trans Silv/'
	
	# prefered file type to capture like('*'-> for all files, '*.ext' for a particular extension, etc.)
	filemask = '*'
	
	# give true to monitor files from sub directories too else give False
	recursive = True
	
	# give true to see each captured file's info during execution in console 
	watch = True
	
	'''
		pass the above created variables to glob to generate required files info.
		A file's information is genrated as a dict object with the following keys:
			1) name: contains file name as str
			2) path: contains file path as str
			3) time: contains file's last modified time as datetime
			4) size: contains file size as str in maximum possible unit like( KB, MB, GB, etc.)
			5) stat: contains file info extraction status as str like('Extraction successful' or 'Extraction failed due to ...')
	 '''
	files_info_gen = glob(directory, filemask, recursive, watch)
	
	# to convert files_info_gen to list
	files_info_list = list(files_info_gen)
	
	# to sort files_info based on a key like('name','path','time','size') and an order like('asc','desc')
	sortfilesby(files_info_list, 'time', 'asc')
	
	'''
		to create a dictionary with items of files_info_list,
		where each item will become a value with key as filename+lastmodifiedtime.strftime('%d%m%Y%H%M%S')
	'''
	files_info_dict = getdict(files_info_list)
