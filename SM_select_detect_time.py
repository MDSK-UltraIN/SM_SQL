import pyodbc
dsn = 'sqlserverdatasource'
server = 'smp.database.windows.net'
user = 'msp12'
password = 'MicrosoftSP12'
database = 'SM'
driver = '{ODBC Driver 13 for SQL Server}'
cnsn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+user+';PWD='+password)
cursor = cnsn.cursor()

######command here
timestart = '2017-09-03 10:00' #開始時間
timefinish = '2017-09-03 13:00' #結束時間
SQLCommand = "select * from [dbo].[detect] where detecttime >= CONVERT(datetime,'"+timestart+"',110) and detecttime <= CONVERT(datetime,'"+timefinish+"',110) order by detecttime;"
cursor.execute(SQLCommand)

#cnsn.commit() #你懂的
row = cursor.fetchone()

while row:
    print("ID:"+str(row[0])+" person:"+str(row[1])+" Time:"+str(row[2]))
    row=cursor.fetchone()