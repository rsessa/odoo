

![image-20210506104427925](https://tva1.sinaimg.cn/large/008i3skNgy1gq8sv4q7cqj303k03kweo.jpg)



### ¿Que es este repositorio?

Este repositorio te permitirá desplegar **odoo** es una aplicación para





## Configuración

```
cd /root/containers
git clone https://github.com/HiveAgile/odoo.git
cd odoo
```

Ajustar las variables del fichero `.env`

```
ODOO_HOST=odoo.hiveagile.dev

COMPOSE_PROJECT_NAME=odoo16-enterprise-hiveagile-com
CONTAINER_NAME=odoo16-enterprise-hiveagile-com
ODOO_HOSTNAME=odoo16-enterprise-hiveagile-com

# ODOO_LOG_MODE: El nivel de log de odoo, y que por defecto va a mostrar por consola
# puede ser -> 'info', 'debug_rpc', 'warn', 'test', 'critical', 'debug_sql', 'error', 'debug', 'debug_rpc_answer', 'notset'
ODOO_LOG_MODE=info

# DEBUG_PTVSD: [0|1] Define si PTVSD va a estar a la escucha
DEBUG_PTVSD=0

# Versión de Odoo
ODOO_VERSION=16.0

# Versión de postgres
POSTGRES_VERSION=12

# Acceso a base de datos de postgres
DB_USER=odoo
DB_NAME=postgres
DB_PASSWORD=odoo16paraplanB123

# Puertos publicos
EXPOSE_PUBLIC_PORT_ODOO=6069
EXPOSE_PUBLIC_PORT_DB=6432
EXPOSE_PUBLIC_PORT_DEBUG=3002
EXPOSE_PUBLIC_PGADMIN_PORT=4444
```



### `ODOO_HOST`

Esta variable define el dominio donde accederas a  **odoo**, recuerda apuntar previamente el registro DNS de tipo A para que te funcione.



## USO

Una vez editado el fichero  puesdes ejecutar el contenedor como normalmente.

```
cd /root/containers/odoo
docker-compose up -d
```



## Actualizaciones automáticas (Opcional)

Puedes usar watchtower que actualiza todos los contenedores que estan como latest

Esto es algo que pongo en todas las aplicaciones pero no hace falta que se instale cada vez.

```
docker run -d \
    --name watchtower \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower -i 30
```






## Invitación a mi Canal.

Estás invitado a mi canal de telegram, donde publico más soluciones como esta.

![Telegram-icon](https://tva1.sinaimg.cn/large/008i3skNgy1guctnvd002j600w00w0r202.jpg)https://t.me/aitorroma

----------------------------------------------------------

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/J3J64AN17)

