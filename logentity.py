import time
#2017-01-03 16:34:37,657 | INFO  | _timer_service_1 | timersrevise|call（） 243 | 495 - com.huawei.controller.dbworkflow- 1.0.1.SNAPSHOT | message info 1

class LogEntity(object):

    def __init__(self, logentity):
        self.logentity = logentity.split('|', 6)
        self._parselog_(self.logentity)

    def _parselog_(self):
        self._parsetime_(self.logentity[0])
        self.level = self.logentity[1]
        self.pid = self.logentity[2]
        self.classname = self.logentity[3]
        self.methodname = self.logentity[4]
        self.bunddle = self.logentity[5]
        self.msginfo = self.logentity[6]

    def _parsetime_(self, timestr):
        self.time = timestr.split()
