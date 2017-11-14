from app import app
from .db_interface import Zelda

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
<<<<<<< HEAD
app.config['MYSQL_PASSWORD'] = 'mps2017'
=======
app.config['MYSQL_PASSWORD'] = '123456'
>>>>>>> 48e4940c845c63c0538779774497c8f522fbbbce
app.config['MYSQL_DB'] = 'zelda'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


# init MYSQL
db = Zelda(app)
