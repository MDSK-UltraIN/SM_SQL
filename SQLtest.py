
# coding: utf-8

# In[11]:

import pyodbc
server = 'smp.database.windows.net'
database = 'SM'
username = '{UN}'
password = '{PW}'
driver = '{ODBC Driver 13 for SQL Server}'
Namevartest ='MSPVarTest'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password)
cursor =cnxn.cursor()
#cursor.execute("INSERT INTO [dbo].[test]([faceID],[userName],[dateregis]) VALUES ('test777-666-77777888',"+repr(Namevartest)+",CONVERT(DATETIME,SYSDATETIMEOFFSET() AT TIME ZONE 'China Standard Time'))") #寫入資料

cursor.execute("select * from [dbo].[test]")


row = cursor.fetchone()
while row:
    #if str(row[0]) == 'test321-123-8787878':
    print(str(row[0])+" "+str(row[1])+" "+str(row[2]))
    row = cursor.fetchone()

    




# In[ ]:



