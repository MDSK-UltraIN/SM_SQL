import pyodbc
import random
dsn = 'sqlserverdatasource'
server = 'smp.database.windows.net'
user = 'USER'
password = 'PASSWORD'
database = 'SM'


PERSONGROUPID = 'Person'+repr(random.randint(0,999)) #PersonGroupID在這裡

cnsn = pyodbc.connect('DSN=%s;UID=%s;PWD=%s;DATABASE=%s;'%(dsn,user,password,database))
cursor = cnsn.cursor()
#SQLCommand = "INSERT INTO [dbo].[test]([faceID],[userName],[dateregis]) VALUES ('test888-777-1859"+repr(random.randint(0,999))+"',"+repr(Namevartest)+",CONVERT(DATETIME,SYSDATETIMEOFFSET() AT TIME ZONE 'China Standard Time'))"
cursor.execute("INSERT INTO [dbo].[detect]([PersonGroupID],[detecttime]) VALUES ("+repr(PERSONGROUPID)+",CONVERT(DATETIME,SYSDATETIMEOFFSET() AT TIME ZONE 'China Standard Time'))"
)
cnsn.commit() #hen IMPORTANT
"""cursor.execute("select * from [dbo].[test]")
row = cursor.fetchone()
while row:
    print(str(row[0]))
    row=cursor.fetchone()"""