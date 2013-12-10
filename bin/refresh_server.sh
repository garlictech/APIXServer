ROOT=/home/apixserver/public_html/APIXServer/APIXServer
cd $ROOT
pushd APIXServer
ln -sf settings_prod.py settings_actual.py
popd
python manage.py syncdb --noinput
python manage.py collectstatic
sudo /etc/init.d/apache2 reload
