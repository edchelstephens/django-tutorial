# Database connections

## To get the default connection instance

* use connections from django.db
* from django.db import connections

* get the "default" key value

* connection = connections["default"]
* it should return something like this below for postgresql back-end
* <django.db.backends.postgresql.base.DatabaseWrapper object at 0x7f1dfb3406a0>
