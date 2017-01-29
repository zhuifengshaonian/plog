import datetime
import uuid


# 2017-01-03 16:34:37,657 | INFO  | _timer_service_1 | timersrevise|call（） 243 | 495 - com.huawei.controller.dbworkflow- 1.0.1.SNAPSHOT | message info 1

class LogEntity(object):
    def __init__(self, logentity):
        self._logentity = logentity.split('|', 6)
        self._parselog_()
        self.id = uuid.uuid1().__str__()

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
        self.timestr = timestr

    def __repr__(self):
        if 7 == len(self._logentity):
            return 'LogEntity:[id:{0}, time:{1}, level:{2}, pid:{3}, classname:{4}, methodname:{5}, bunddle:{6},' \
                   ' msginfo"{7}]'.format(self.id, self.time, self.level, self.pid, self.classname,
                                          self.methodname, self.bunddle, self.msginfo)
        else:
            return 'LogEntity:[null]'
