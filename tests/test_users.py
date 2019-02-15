import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('users_group')


def test_mariadb_databases_created(Command):
    cmd = Command('mysql -u root --execute="show databases"')
    assert cmd.rc == 0
    assert 'mydb' in cmd.stdout
    assert 'anotherdb' in cmd.stdout


def test_mariadb_database_initialized(Command):
    cmd = Command('mysql -u root --execute="show tables" mydb')
    assert cmd.rc == 0
    assert 'Person' in cmd.stdout
    assert 'Tasks' in cmd.stdout


def test_mariadb_users_created(Command):
    cmd = Command('mysql -u root  --execute="SELECT host, user FROM mysql.user"')
    # Split lines and replace multiple spaces with one
    result = [' '.join(line.split()) for line in cmd.stdout.split('\n')]
    assert 'localhost foo' in result
    assert '192.168.0.% bar' in result


def test_mariadb_user_login(Command):
    cmd = Command('mysql -u foo -pbad_passwd mydb --execute="show tables"')
    assert cmd.rc == 1
    assert 'Access denied for user' in cmd.stderr
    cmd = Command('mysql -u foo -pchange_me mydb --execute="show tables"')
    assert cmd.rc == 0
    cmd = Command('mysql -u foo -pchange_me non_existing_db --execute="show tables"')
    assert cmd.rc == 1
    assert 'Access denied for user' in cmd.stderr
