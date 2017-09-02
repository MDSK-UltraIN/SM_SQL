
# coding: utf-8

# In[11]:

import pyodbc
server = 'smp.database.windows.net'
database = 'SM'
username = '{UN}'
password = '{PW}'
driver = '{ODBC Driver 13 for SQL Server}'
Namevartest ='MSP_RPi_inserttest'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password)
cnxn.autocommit = True
cursor =cnxn.cursor()
SQLCommand = "INSERT INTO [dbo].[test]([faceID],[userName],[dateregis]) VALUES ('test777-666-1859"+repr(random.randint(0,999))+"',"+repr(Namevartest)+",CONVERT(DATETIME,SYSDATETIMEOFFSET() AT TIME ZONE 'China Standard Time'))" #中間隨機產生數字
cursor.execute(SQLCommand)
cursor.execute("select * from [dbo].[test]")


row = cursor.fetchone()
while row:
    #if str(row[0]) == 'test321-123-8787878':
    print(str(row[0])+" "+str(row[1])+" "+str(row[2]))
    row = cursor.fetchone()




