# static-server-in-dir
Run an ad hoc http static server in your current (or specified) directory

```bash
yum -y install yum-plugin-copr

yum copr enable antonpatsev/static-server-in-dir

yum -y install static-server-in-dir

export HTTP_SERVER_DIR=`pwd`

systemctl import-environment HTTP_SERVER_DIR

systemctl start static-server-in-dir
```
