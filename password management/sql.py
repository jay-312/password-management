import mysql.connector
import configparser


config=configparser.ConfigParser()
config.read("config.properties")

users=config.get("dbsection",'db.table1')


mydb = mysql.connector.connect(
host=config.get("dbsection",'db.host'),
user=config.get("dbsection","db.user"),
passwd=config.get('dbsection','db.passwd'),
)
cur = mydb.cursor()

#--Functions--
def Delete(n,a,b):
    cur.execute('delete from '+n+' where site=\''
                + a +'\' and user_name=\''
                + b +'\'')
    mydb.commit()
    
def add(n,a,b,c):
    #to know if table users_data exists
    cur.execute('show tables like \''+n+'\'')
    cur.fetchall()
    if (cur.rowcount==0):       #creating table users_data if it doesn't  exists
        cur.execute('create table '+n+''' (
        site varchar(25),
        user_name varchar(25),
        password varchar(25)
        )''' )
    else:
        cur.execute('select * from '+n+' where site=\''
                + a +'\' and user_name=\''
                + b +'\' and password=\''
                + c +'\'')
        cur.fetchall()
        if (cur.rowcount==0):
            sql="insert into "+n+" values(%s,%s,%s)"
            val=(a,b,c)
            cur.execute(sql,val)
            mydb.commit()
        else:
            return False

def search(n,a,b):
    cur.execute('select * from '+n+' where site=\''
                + a +'\' and user_name=\''
                + b +'\'')
    x=cur.fetchall()
    if (cur.rowcount==0):
        return False
    else:
        for i in x:
            A=i[2]
        return A    
        
def CheckUser(a,b):
    cur.execute('select user_name,password from users where user_name=\''
                + a +'\' and password= \''
                + b + '\'')
    cur.fetchall()
    if(cur.rowcount == 0): 
        return False
    else:
        # Again executing for name in login file
        cur.execute('select name,user_name from users where user_name=\''+a+'\'')
        return True
    
def UserAvailability(n):
    cur.execute('select user_name from users where user_name=\''+n+'\'')
    cur.fetchall()
    if(cur.rowcount == 1):
        return False
    else:
        return True
    
def Register(name,user,password):

    sql="insert into users values(%s,%s,%s)"
    val=(name,user,password)
    cur.execute(sql,val)
    mydb.commit()

#--main--    

try:        #using exception if database doesn't exists
    cur.execute('use ' + config.get("dbsection","db.database"))
except:
    cur.execute('create database '+config.get("dbsection","db.database"))
    cur.execute('use ' + config.get("dbsection","db.database"))

#to know if table users exists
cur.execute("show tables like \'"+users+"\'")
cur.fetchall()

if (cur.rowcount==0):       #creating table users if it doesn't  exists
    cur.execute('''create table users(
    name varchar(25),
    user_name varchar(25),
    password varchar(25)
    )''')
else:
    pass    
    

