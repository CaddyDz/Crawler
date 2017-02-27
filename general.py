import os


# Each website you crawl is a separate project (folder)
def createProjectDir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)


# Create queue and crawled files (if not crawled)
def createDataFiles(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        writeFile(queue, base_url)
    if not os.path.isfile(crawled):
        writeFile(crawled, '')


# Create a new file
def writeFile(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

createDataFiles('caddy', 'https://caddydz.github.io/')


