import zipfile
class Logfile(object):
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.type = self.fileType()

    def readFileLines(self):
        try:
            fileobject = open(self.filename, "r")
        except IOError:
            print("the file " + self.filename + "is not exist, Please double check.")
            exit()
        alllines = fileobject.readlines()
        return alllines

    def readZipFileLines(self):
        lines = []
        with zipfile.ZipFile(self.filename) as myzip:
            for file in myzip.namelist():
                with myzip.open(file, 'r') as myfile:
                    for line in myfile.readlines():
                        lines.append(line.decode())
            return lines

    def fileType(self):
        if zipfile.is_zipfile(self.filename):
            return 'zip'
        else:
            return 'log'

    def readLines(self):
        if self.type == 'zip':
            return self.readZipFileLines()
        else:
            return self.readFileLines()

