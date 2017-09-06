#!flask/bin/python
from app import app
from flaskext.mysql import MySQL


#To configure access to your MySQL database server by using these settings :
#MYSQL_DATABASE_HOST 	default is ‘localhost’
#MYSQL_DATABASE_PORT 	default is 3306
#MYSQL_DATABASE_USER 	default is None
#MYSQL_DATABASE_PASSWORD 	default is None
#MYSQL_DATABASE_DB 	default is None
#MYSQL_DATABASE_CHARSET 	default is ‘utf-8’

#mysql = MySQL()
#mysql.init_app(app)

#cursor = mysql.get_db().cursor()

app.run(debug=True)
