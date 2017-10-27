import MySQLdb

def createDB(mysqlServer, mysqlUser, mysqlRootPassword, domainShort, ipv4, mysqlpassword):
    db = MySQLdb.connect(''+mysqlServer, ''+mysqlUser, ''+mysqlRootPassword)

    # Create a Cursor object to execute queries.
    cur = db.cursor()

    # Select data from table using SQL query.
    cur.execute("CREATE DATABASE IF NOT EXISTS " + domainShort)

    cur.execute("GRANT ALL PRIVILEGES ON " +domainShort + ".* TO %s@%s IDENTIFIED BY %s ", (domainShort, ipv4, mysqlpassword))
    cur.execute("FLUSH PRIVILEGES")
    db.commit()
    db.close()

createDB(mysqlServer, mysqlUser, mysqlRootPassword, domainShort, ipv4, mysqlpassword)