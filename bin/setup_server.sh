#! /bin/bash

USER=apixserver
SSH_CONFIG_FILE=/etc/ssh/sshd_config
APT_COMMAND="sudo aptitude install -y"
PIP_INSTALL="sudo pip install"
SITE_NAME=APIXServer
HTML_ROOT=$HOME/public_html/
SITE_ROOT=$HTML_ROOT/$SITE_NAME
EASY_INSTALL="sudo easy_install"

adduser $USER
visudo
echo "UseDNS no" >> $SSH_CONFIG_FILE
echo "AllowUsers $USER" >> $SSH_CONFIG_FILE
echo "PermitRootLogin no" >> $SSH_CONFIG_FILE
su -l $USER
$APT_COMMAND libapache2-mod-wsgi apache2 apache2.2-common apache2-mpm-prefork apache2-utils libexpat1 ssl-cert vim python-setuptools firebird2.5-superclassic python-setuptools
$EASY_INSTALL pip
dpkg-reconfigure firebird2.5-superclassic
reload ssh
ssh-keygen
nano .ssh/authorized_keys
sudo service apache2 restart
mkdir -p $HTML_ROOT
cd $HTML_ROOT
sudo locale-gen hu_HU
sudo update-locale LANG=hu_HU
cp $SITE_ROOT/config/bashrc $HOME/.bashrc
source $HOME/.bashrc
sudo cp $SITE_ROOT/config/apache_site_conf_$SITE_NAME /etc/apache2/sites-available/$SITE_NAME
cd $SITE_ROOT
$PIP_INSTALL -r requirements.txt
# patch django-firebird...
sudo cp patch/operations.py /usr/local/lib/python2.7/dist-packages/firebird

sudo a2dissite default
sudo a2ensite $SITE_NAME
sudo /etc/init.d/apache2 reload
chmod 777 $SITE_ROOT # http://bit.ly/13e3jU4
