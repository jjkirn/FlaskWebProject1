#flaskapp.wsgi
import sys
sys.path.insert(0, '/var/www/html/FlaskWebProject1')

from FlaskWebProject1 import app as application
