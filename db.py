import pymysql 

username = "root"
host="localhost"
password=""
dbname = "net_banking"

def connect():
    db = pymysql.connect(user=username,host=host,db=dbname)
    return db

def insert_data(account_no,account_name,account_balance,account_pin):
    try:
        db = connect()
        cs = db.cursor()
        sql = "insert into account_data (account_no,account_name,account_balance,account_pin) values (%s,%s,%s,%s)"
        values = (account_no,account_name,account_balance,account_pin)
        cs.execute(sql,values)
        db.commit()
        return True
    except:
        return False
    finally:
        db.close()

def get_account_data():
    
    try:
        db = connect()
        cs = db.cursor()
        sql = "select * from account_data "
        cs.execute(sql)
        accounts = cs.fetchall()
        return accounts
    except:
        return False
    finally:
        db.close()

def get_account(account_no):
    
    try:
        db = connect()
        cs = db.cursor()
        sql = "select * from account_data where account_no=%s"
        value = (account_no,)
        cs.execute(sql,value)
        account = cs.fetchone()
        return account
    except Exception as e:
        print(e)
        return False
    finally:
        db.close()


def get_pin(account_no):
    
    try:
        db = connect()
        cs = db.cursor()
        sql = "select account_balance, account_pin from account_data where account_no=%s"
        value = (account_no,)
        cs.execute(sql,value)
        pin = cs.fetchone()
        return pin
    except Exception as e:
        print(e)
        return False
    finally:
        db.close()


def update_balance(account_no,account_balance):
    try:
        db = connect()
        cs = db.cursor()
        sql = "update account_data set account_balance=%s where account_no=%s"
        values = (account_balance,account_no)
        cs.execute(sql,values)
        db.commit()
        return True
    except:
        return False
    finally:
        db.close()   


get_account(1237)
get_pin(1237)
