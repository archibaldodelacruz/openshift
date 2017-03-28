from ncclient import manager
import populate
import time

def push(host, port, user, password):
    try:
    	conn = manager.connect(host=host,
            port=port,
            username=user,
            password=password,
            timeout=10,
            device_params = {'name':'junos'},
            hostkey_verify=False)

    	firewall = conn.command(command='show configuration firewall family inet filter OpenShift', format='text').tostring

    	config, term_list = populate.fetch()

    	for term in term_list:
		if term in firewall:
			pass
		else:
    			command =[line.rstrip("\n") for line in config if line.startswith(("set","delete"))]
    			send_config = conn.load_configuration(action='set', config=command)
    			print send_config.tostring

    			check_config = conn.validate()
    			print check_config.tostring

    			conn.commit()
    			conn.close_session()

    except:
        pass

if __name__ == '__main__':

    host = '10.84.53.3'
    port = '22'
    user = 'root'
    password = 'c0ntrail123'

    while True:
        push(host, port, user, password)
	time.sleep(10)
