       from pyhive import hive
       import pandas
       
       conn = hive.Connection(host='localhost', port=10000,  database='default')
       cursor = conn.cursor()
       sql = 'show databases'
       cursor.execute(sql)
       print (cursor.fetchall())
       df = pandas.read_sql(sql, conn)
       print (df)
