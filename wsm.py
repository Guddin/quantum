

import os, sys, subprocess

def main():
    print "installing Mysql ...."
    subprocess.call(["zypper", "install", "mysql-community-server"])
    subprocess.call(["reboot"])
    subprocess.call(["systemctl","enable", "mysql.service"])
    subprocess.call(["rcmysql", "reload"])
    subprocess.call("mysql_secure_installation")
    print "installing apache2 ......."
    subprocess.call(["zypper", "install", "apache2"])
    subprocess.call(["systemctl", "enable", "apache2.service"])
    subprocess.call(["rcapache2", "reload"])
    print "installing mod_php5..........."
    subprocess.call(["zypper", "install", "apache2-mod_php5"])
    subprocess.call(["rcapache2", "reload"])
    print "creating info.php ..............."
    file_info_php = open('/srv/www/htdocs/info.php', 'w')
    info_code = '<?php\nphpinfo();\n?>'
    file_info_php.write(info_code)
    subprocess.call(["rcapache2", "reload"])
    print "installing phpMyAdmin.............."
    subprocess.call(["zypper", "install", "phpMyAdmin"])
    subprocess.call(["rcapache2", "reload"])
    subprocess.call(["a2enmod", "rewrite"])
    print "virtual host creating................."
    f_in = open ("/etc/apache2/listen.conf").read()
    text = f_in.replace('#NameVirtualHost *:80', 'NameVirtualHost *:80')
    f_out = open ("/etc/apache2/listen.conf", 'w').write(text)
  
def fileedit():
    print "create quantum.conf........."
    file_in= open ("/etc/apache2/vhosts.d/vhost.template").read()
    text=file_in.replace('/vhosts/dummy-host.example.com/cgi-bin', '/cgi-bin')
    text=text.replace('dummy-host.example.com', 'quantum.com')
    text=text.replace('ErrorLog ', '#ErrorLog')
    text=text.replace('CustomLog', '#CustomLog')
    text=text.replace('AllowOverride None', 'AllowOverride All')
    text=text.replace('ServerName quantum.com', ' ServerName quantum.com\n     ServerAlias quantum.org.bd')
    file_out= open ("/etc/apache2/vhosts.d/quantum.conf", 'w').write(text)
 
def localhost():
    print "create _default.conf........"
     file_in= open ("/etc/apache2/vhosts.d/quantum.conf").read()
     text=file_in.replace('vhosts/quantum.com', 'htdocs')
     text=text.replace('quantum.com', 'localhost')
     text=text.replace('ServerAlias quantum.org.bd', '#ServerAlias quantum.org.bd')
     file_out= open ("/etc/apache2/vhosts.d/_default.conf", 'w').write(text)
def directory():
    print "create new directory......."
    subprocess.call(["mkdir", "/srv/www/vhosts/quantum.com", "-p", "755"])
    file_index_html=open('/srv/www/vhosts/quantum.com/index.html', 'w')
    index_code='<html> it works \n </html>'
    file_index_html.write(index_code)
    
    
     
    
if __name__ == "__main__":
    main()
    fileedit()
    localhost()
    directory()
    

