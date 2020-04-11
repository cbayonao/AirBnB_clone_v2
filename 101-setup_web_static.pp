#  Puppet for setup
exec { 'update':
  command => '/usr/bin/env apt-get -y update',
}
-> exec {'instNginx':
  command => '/usr/bin/env apt-get -y install nginx',
}
-> exec {'crea1':
  command => '/usr/bin/env mkdir -p /data/web_static/releases/test/',
}
-> exec {'crea2':
  command => '/usr/bin/env mkdir -p /data/web_static/shared/',
}
-> exec {'fake':
  command => '/usr/bin/env echo "html fake" > /data/web_static/releases/test/index.html',
}
-> exec {'simlink':
  command => '/usr/bin/env ln -sf /data/web_static/releases/test /data/web_static/current',
}
-> exec {'chown':
  command => '/usr/bin/env chown -R ubuntu:ubuntu /data',
}
-> exec {'configure':
  command => '/usr/bin/env sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
}
-> exec {'restart':
  command => '/usr/bin/env service nginx restart',
}
