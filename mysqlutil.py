#!/usr/bin/python  
import pymysql


class Mysql(object):
    insertsql = 'INSERT INTO `ac_log`.`log_info` (`id`, `level`, `pid`, `classname`, `methodname`, `bunddle`, `msginfo`, `parsetime`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'

    # 数据库连接参数设置 默认连接localhost
    def __init__(self, user, passwd, db, host="localhost"):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db

    # 连接数据库
    def getconn(self):
        _conn = pymysql.connect(self.host, self.user, self.passwd, self.db)
        _cur = _conn.cursor()
        return _conn, _cur

    # 更新操作
    def update(self, logentity):
        _conn, _cur = self.getconn()
        _sta = _cur.execute(self.insertsql)
        _conn.commit()
        self.connClose(_conn, _cur)
        return _sta

    # 插入操作(`id`, `level`, `pid`, `classname`, `methodname`, `bunddle`, `msginfo`, `parsetime`)
    def insert(self, logentity):
        _conn, _cur = self.getconn()
        try:
            sta = _cur.execute(self.insertsql,
                               (logentity.id,
                                logentity.level,
                                logentity.pid,
                                logentity.classname,
                                logentity.methodname,
                                logentity.bunddle,
                                logentity.msginfo,
                                logentity.time
                                )
                               )
            _conn.commit()
            return sta
        except Exception as e:
            print(e)
            _conn.rollback()
        finally:
            self.connClose(_conn, _cur)

    # 查找操作
    def query(self, sql):
        _conn, _cur = self.getconn()
        _cur.execute(sql)
        _data = _cur.fetchall();
        _conn.commit()
        self.connClose(_conn, _cur)
        return _data

    # 关闭连接，释放资源
    @staticmethod
    def connClose(conn, cur):
        cur.close()
        conn.close()
