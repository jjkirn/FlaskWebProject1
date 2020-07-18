sudo ln -sT /home/ubuntu/FlaskWebProject1/FlaskWebProject1/ /var/www/html/FlaskWebProject1

Modify the file /etc/apache2/sites-enabled/000-default.conf:

        WSGIDaemonProcess flaskapp threads=5
        WSGIScriptAlias / /var/www/html/FlaskWebProject1/FlaskWebProject1.wsgi
#        WSGIScriptAlias / /var/www/html/flaskapp/flaskapp.wsgi

        <Directory flaskapp>
                WSGIProcessGroup flaskapp
                WSGIApplicationGroup %{GLOBAL}
                Order deny,allow
                Allow from all
        </Directory>

