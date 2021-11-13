# serprolim django

<h3>1. Clonando el repositorio</h3>

```$
git clone https://github.com/magoreal4/serprolim.git
mv serprolim <your project>
```
<h3>2. Entorno virtual y paquetes</h3>

```$
python3.8 -m venv virtual
source virtual/bin/activate
pip install -r requirements.txt
```
<h3>3. Realizar cambios en los archivos</h3>

```txt
web_base.com
web_base.socket
web_base.service
```
<h3>3. Base de datos y archivos estaticos</h3>

```$
python ./app/manage.py migrate
python ./app/manage.py collectstatic
```

<h3>4. Service, socket</h3>

```$
sudo cp web_base.socket /etc/systemd/system/web_base.socket
sudo cp web_base.service /etc/systemd/system/web_base.service
sudo systemctl enable web_base
sudo systemctl start web_base
```

<h3>5. Nginx</h3>

```$
sudo cp web_base.com /etc/nginx/sites-available/web_base.com
sudo ln -s /etc/nginx/sites-available/web_base.com /etc/nginx/sites-enabled/web_base.com
sudo nginx -t
sudo systemctl restart nginx
```

<h3>Oros comandos</h3>

```$
python ./app/manage.py runserver 8005
python ./app/manage.py createsuperuser
pip freeze> requirements.txt
python ./app/manage.py collectstatic --no-input --clear
sudo chmod 777 static_volume/
systemctl status nginx
systemctl status web_base

systemctl stop [servicename]
systemctl disable [servicename]
rm /etc/systemd/system/[servicename]
rm /etc/systemd/system/[servicename] # and symlinks that might be related
rm /usr/lib/systemd/system/[servicename] 
rm /usr/lib/systemd/system/[servicename] # and symlinks that might be related
systemctl daemon-reload
systemctl reset-failed
```
# serprolim

