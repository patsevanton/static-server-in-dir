# static-server-in-dir
Run an ad hoc http static server in your current (or specified) directory

```bash
yum -y install yum-plugin-copr

yum copr enable antonpatsev/static-server-in-dir

yum -y install static-server-in-dir

cd to directory

static-server-in-dir start

run test, wget apk, or someting

static-server-in-dir stop
```
