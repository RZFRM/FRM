import pymysql
from  etc.MysqlSetting import *




class Mysql_base(object):
    ''' 数据库操作基本类, 包含于业务无关的的操作方法'''
    def __init__(self, host, user, passwd, dbname, port):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbname = dbname
        self.port = port
        self.conn = self.connect()


    def connect(self):
        conn = pymysql.connect(self.host, self.user, self.passwd, self.dbname, self.port)
        return conn

    def select(self, table, filed):

        try:
            print('select def :======================', filed)
            filed = "'" + filed + "'"
            sql = "SELECT END_TIME, START_TIME,STATUS  from {table} where JOB_NO ={filed}".format(table=table, filed=filed)
            print('select + ======================sql ====', sql)
            cursor = self.conn.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            print('Select %d lines' % cursor.rowcount)
            cursor.close()
            self.conn.commit()
            return results
        except Exception as e:
            print('DataBase Select Error: %s' % e)
            # TODO(blkart): raise SelectError

    def insert(self, table, values, fields=None):

        invoice_code = int(values[0])
        invoice_number=int(values[1]),
        invoice_data = int(values[2]),
        check_code= int(values[3]),
        PurchaserRegisterNum = values[4],
        seller_register_num = values[5] ,
        GoodsServerName = values[6],
        invoice_type = values[7],
        PurchaserName = values[8] ,
        AmountInWords = values[9] ,
        AmountInFiguers = float(values[10]),
        print(invoice_type,invoice_code, invoice_number)


        if fields:
            sql = 'INSERT INTO {table} {fields} VALUES {values}'.format(
                table=table, fields=fields, values=(tuple(values)))
            print('sql lanuager:', sql)
        else:
            sql = 'INSERT INTO {table} VALUES {values}'.format(
                table=table, values=values)

        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            cursor.close()
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print('DataBase Insert Error: %s' % e)
            # TODO(blkart): raise InsertError

    def delete(self, table, condition):
        sql = 'DELETE FROM {table} WHERE {condition}'.format(
            table=table, condition=condition
        )

        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            cursor.close()
            self.conn.commit()
        except Exception as e:
            print('DataBase Delete Error: %s' % e)
            # TODO(blkart): raise DeleteError

    def update(self, table, assignments, condition):
        sql = 'UPDATE {table} SET {assignments} WHERE {condition}'.format(
            table=table, assignments=assignments, condition=condition
        )

        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            cursor.close()
            self.conn.commit()
        except Exception as e:
            print('DataBase Update Error: %s' % e)
            # TODO(blkart): raise UpdateError






#  TODO  查询 远程艺赛琪数据库的信息  回写咱们的数据库
class Mysql_client(Mysql_base):
    ''' TODO 与业务有关的数据库操作方法'''
    def __init__(self):
        self.host = I_MYSQL_HOST
        self.user = I_MYSQL_USERNAME
        self.passwd = I_MYSQL_PASSWORD
        self.dbname = I_MYSQL_DATABASE_NAME
        self.port = I_MYSQL_PORT
        super().__init__(self.host, self.user, self.passwd, self.dbname, self.port)


    def add_invoice(self, args):
        print('add_voice===values===:',args)
        # TODO: 处理插入异常
        self.insert('general_invoice', args,
                    "(invoice_code, invoice_number, invoice_data,"
                    "check_code, PurchaserRegisterNum, seller_register_num,GoodsServerName, "
                    "invoice_type, PurchaserName, AmountInWords,AmountInFiguers)"
                    )


    def get_rpa_exe(self, filed=None):
        try:
            print(type(filed), filed)
            print(11)
            rpa_info = self.select(table = 'T_RPA_JOB', filed= filed);
            print(11)
            print('rpa_info ===============',rpa_info)
        except:
            rpa_info = '没有获取数据'
        return rpa_info


    def get_invoice(self,):
        pass












    #
    # def edu_mysql_found_user(*args):
    #     conn_edu = pymysql.connect(host = E_MYSQL_HOST,
    #                            port=E_MYSQL_PORT,
    #                            user=E_MYSQL_USER,
    #                            password=E_MYSQL_PASSWORD,
    #                            database = E_MYSQL_DATABASES,
    #                            charset='utf8')
    # 得到一个可以执行SQL语句的光标对象
    # cursor = conn_edu.cursor()
    # 定义要执行的SQL语句
    # sql = " select  StuName,StuCode from yxcx_classstudent  where StuCode= '%s'" % args
    # print(sql)

    # 执行SQL语句
    # cursor.execute(sql)
    # data = cursor.fetchone()
    # if data:
    #     print('获取到了数据库:', data)
    #     return data
    # else:
    #     print('此学生不存在')
    #     return data
    #
# 关闭光标对象
# cursor.close()
# 关闭数据库连接
# conn_edu.close()
#
#
# if __name__  == '__main__':
#     mysql_client.get_rpa_exe(filed='ac5b3c08-9c95-48d3-9e76-292f0e25b3ee')