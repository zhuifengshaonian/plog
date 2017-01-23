import datetime


# 2017-01-03 16:34:37,657 | INFO  | _timer_service_1 | timersrevise|call（） 243 | 495 - com.huawei.controller.dbworkflow- 1.0.1.SNAPSHOT | message info 1

class LogEntity(object):
    def __init__(self, logentity):
        self._logentity = logentity.split('|', 6)
        self._parselog_()

    def _parselog_(self):
        if 7 == len(self._logentity):
            self._parsetime_(self._logentity[0].strip())
            self.level = self._logentity[1].strip()
            self.pid = self._logentity[2].strip()
            self.classname = self._logentity[3].strip()
            self.methodname = self._logentity[4].strip()
            self.bunddle = self._logentity[5].strip()
            self.msginfo = self._logentity[6].strip()

    def _parsetime_(self, timestr):
        self.time = datetime.datetime.strptime(timestr, '%Y-%m-%d %H:%M:%S,%f')

    def __repr__(self):
        if 7 == len(self._logentity):
            return 'LogEntity:[time:{0}, level:{1}, pid:{2}, classname:{3}, methodname:{4}, bunddle:{5}, msginfo"{6}]'.format(
                self.time, self.level, self.pid, self.classname, self.methodname, self.bunddle, self.msginfo)
        else:
            return 'LogEntity:[null]'
