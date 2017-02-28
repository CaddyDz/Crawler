import os

# Each website you crawl is a separate project (folder)
def createProjectDir(directory):
	if not os.path.exists(directory):
		print('Creating project ' + directory)
		os.makedirs(directory)

# Create queue and crawled files (if not crawled)
def createDataFiles(projectName, baseUrl):
	queue = projectName + '/queue.txt'
	crawled = projectName + '/crawled.txt'
	if not os.path.isfile(queue):
		writeFile(queue, baseUrl)
	if not os.path.isfile(crawled):
		writeFile(crawled, '')
		
# Create a new file
def writeFile(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close()

# Add data onto an existing file
def appendToFile(path, data):
	with open(path, 'a') as file:
		file.write(data + '\n')

# Delete the content of a file
def deleteFileContent(path):
	with open(path, 'w'):
		pass

# Read a file and convert each line to set items
def fileToSet(fileName):
	results = set()
	with open(fileName, 'rt') as f:
		for line in f:
			results.add(line.replace('\n', ''))
	return results

# Iterate through a set, each item will be a new line in the file
def setToFile(links, file):
	deleteFileContent(file)
	for link in sorted(links):
		appendToFile(file, link)
