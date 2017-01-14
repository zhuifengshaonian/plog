import logfile

filename = '/Users/wanglixiang/Source/test/phy1/tmpFile/log.log'
zipfilename = '/Users/wanglixiang/Source/test/phy1/tmpFile/log.zip'

print('read file')

file = logfile.Logfile(filename)
for line in file.readLines():
    print(line.strip('\n'))
print('read zip file')
file = logfile.Logfile(zipfilename)
for line in file.readLines():
    print(line.strip('\n'))
