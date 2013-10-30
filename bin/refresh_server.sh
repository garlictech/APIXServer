ROOT=/home/apixserver/public_html/APIXServer/APIXServer
cd $ROOT
python manage.py syncdb --noinput
python manage.py collectstatic
pushd APIXServer
ln -sf settings_prod.py settings_actual.py
popd
sudo /etc/init.d/apache2 reload
