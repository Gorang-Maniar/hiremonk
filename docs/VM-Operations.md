### 1. All repos will in /mnt folder in local.hiremonk

Open 2 terminal windows

In each terminal window, type ```ssh vagrant@local.hiremonk```, then:

* Terminal #1: ```cd /mnt/web-app```
* Terminal #2: ```cd /mnt/scott```

### 2. Access the Local Site

* The site will be available at ```http://local.hiremonk:8000```

### 3. Managing the VM
Vagrant userful commands

`vagrant up` (start vm)

`vagrant halt` (stop vm)

`vagrant reload` (restart vm)

`vagrant provision` (pull new configuration from chef server)

`vagrant resume` (resume vm)

`vagrant suspend` (suspend vm)
