ics-ans-role-conserver-server
=============================

Ansible role to install conserver-server.

Requirements
------------

- ansible >= 2.2
- molecule >= 1.24

Role Variables
--------------

```yaml
conserver_host: "localhost"
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: ics-ans-role-conserver-server
```

License
-------

BSD 2-clause
