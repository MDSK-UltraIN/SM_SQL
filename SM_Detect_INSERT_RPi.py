import pyodbc
import random
dsn = 'sqlserverdatasource'
server = 'smp.database.windows.net'
user = 'USER'
password = 'PASSWORD'
database = 'SM'




cnsn = pyodbc.connect('DSN=%s;UID=%s;PWD=%s;DATABASE=%s;'%(dsn,user,password,database))
cursor = cnsn.cursor()


Person_ID = 'p38amucp8um4' #ID從這裡改
Person_Name = 'Person名字'#name從這裡改

#SQLCommand = "INSERT INTO [dbo].[test]([faceID],[userName],[dateregis]) VALUES ('test888-777-1859"+repr(random.randint(0,999))+"',"+repr(Namevartest)+",CONVERT(DATETIME,SYSDATETIMEOFFSET() AT TIME ZONE 'China Standard Time'))"
cursor.execute("INSERT INTO [dbo].[detect]([PersonID],[Person],[detecttime]) VALUES ('"+Person_ID+"','"+Person_Name+"',CONVERT(DATETIME,SYSDATETIMEOFFSET() AT TIME ZONE 'China Standard Time'))"
)
cnsn.commit() #hen IMPORTANT
"""cursor.execute("select * from [dbo].[test]")
row = cursor.fetchone()
while row:
    print(str(row[0]))
    row=cursor.fetchone()"""