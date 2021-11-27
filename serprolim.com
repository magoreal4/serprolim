server {

    server_name limpiezapozossepticos.com www.limpiezapozossepticos.com;
    # server_name localhost;

  #  location = /favicon.ico { 
   #     access_log off; 
    #    log_not_found off; 
     #   }

    location /static/ {
        autoindex on;
        alias /root/serprolim/app/staticfiles/;
        }
    
    location /media/ {
        autoindex on;
        alias /root/serprolim/app/media/;
        }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/serprolim.sock;
    }


    listen 443 ssl http2; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/limpiezapozossepticos.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/limpiezapozossepticos.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}

server {
    if ($host = www.limpiezapozossepticos.com) {
        rewrite ^/(.*) https://limpiezapozossepticos.com/$1 permanent;
        #return 301 https://$host$request_uri;
    } # managed by Certbot


    if ($host = limpiezapozossepticos.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    server_name limpiezapozossepticos.com www.limpiezapozossepticos.com;
    listen 80;
    return 404; # managed by Certbot

