import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_conserver_server_enabled_and_running(Service):
    service = Service('conserver')
    assert service.is_running
    assert service.is_enabled
