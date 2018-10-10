from pytest_testconfig import config


def test_foo():
    target_server_ip = config['myapp']['servers']['main_server']
    print("\nCONFIG FILE OUTPUT: " + target_server_ip)
