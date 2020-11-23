Automating Hive Query

    1. Login in EMR (with hive hadoop)
       > open terminal and make ssh access to your EMR in which cluster is made.
       e.g: ssh -i <location of emrkey in local machine> hadoop@ec2-54-172-255-35.compute-1amazonaws.com

    2. Make a two shell script to execute all the installation environment needed to run Hive:
       > First script is to create mini.sh to execute installation for minicoda: below is the content for mini.sh,(chmod +x mini.sh, to make the script executable).
       wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
       bash ~/miniconda.sh -b -p $HOME/miniconda
       conda init bash
       eval "$(/home/hadoop/miniconda/bin/conda shell.bash hook)"
       
       > Second script is for automating installation for hive environment. In this case we create rec.sh (make sure to change mode to executable (chmod +x rec.sh)) . Rec.sh content:
       conda create --name py38 python=3.8
       conda init bash
       conda activate py38
       pip3 install pandas
       pip3 install pyhive
       pip3 install wheel
       pip3 install thrift
       sudo yum install python3-devel
       sudo yum install gcc-c++ python-devel.x86_64 cyrus-sasl-devel.x86_64
       pip3 install thrift-sasl
    3. now you can both scripts assuming it is in executable mode(chmod +x <shell_name>) via
       > . ./mini.sh –  to run installation for minicoda
       > . ./rec.sh – to run installation for hive environment
       
    4. copy the commmand to aws location:
       aws s3 cp /bucketpath/mini.sh
       aws s3 cp /bucketpath/rec.sh
       5. Now create python script to query hive database, below is the python script for data base query: (in this case we create test.py)
       
       from pyhive import hive
       import pandas
       
       conn = hive.Connection(host='localhost', port=10000,  database='default')
       cursor = conn.cursor()
       sql = 'show databases'
       cursor.execute(sql)
       print (cursor.fetchall())
       df = pandas.read_sql(sql, conn)
       print (df)
       

       6. Try to run test.py using command:
       > python3 test.py
       
       
       
																				



END
