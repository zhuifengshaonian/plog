import logfile
import logentity
import mysqlutil

filename = '/Users/wanglixiang/Source/test/phy1/tmpFile/log.log'
zipfilename = '/Users/wanglixiang/Source/test/phy1/tmpFile/log.zip'

print('read file')
mydb = mysqlutil.Mysql(user='root', passwd='root', db='ac_log')
file = logfile.Logfile(filename)
for line in file.readLines():
    log = logentity.LogEntity(line)
    print(mydb.insert(log))
    print(log)
print('read zip file')
file = logfile.Logfile(zipfilename)
for line in file.readLines():
    log = logentity.LogEntity(line)
    mydb.insert(log)
print(log)



