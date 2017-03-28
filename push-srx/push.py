from ncclient import manager
import populate
import time

def push(host, port, user, password):
    try:
    	conn = manager.connect(host=host,
            port=port,
            username=user,
            password=password,
            timeout=40,
            device_params = {'name':'junos'},
            hostkey_verify=False)

    	firewall = conn.command(command='show configuration firewall family inet filter OpenShift', format='text').tostring
	firewall_term_list = [firewall_term.split()[0] for firewall_term in firewall.split("term") if firewall_term.strip().startswith("frontend")]

    	config, config_term_list = populate.fetch()

	try:
		delete_list = list(set(firewall_term_list) - set(config_term_list))
		if delete_list:
			for term_frontend in delete_list:
				command='delete firewall family inet filter OpenShift term ' + str(term_frontend)
				conn.load_configuration(action='set', config=command)
				print "Deleted vSRX term {}".format(term_frontend)
			check_config = conn.validate()
			conn.commit()
                        conn.close_session()
		else:
			pass
	except:
		pass

    	for term in config_term_list:
		if term in firewall:
			pass
		else:
    			command =[line.rstrip("\n") for line in config if line.startswith(("set","delete"))]
    			send_config = conn.load_configuration(action='set', config=command)
			print "Pushed config to vSRX"
#    			print send_config.tostring

    			check_config = conn.validate()
#    			print check_config.tostring

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
