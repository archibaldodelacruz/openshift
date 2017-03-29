#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: SAVITHRU M LOKANATH
# Contact: SAVITHRU AT JUNIPER.NET
# Copyright (c) 2017 Juniper Networks, Inc. All rights reserved.

import os, sys, json, requests, jinja2

def generateTemplate(ip_address, ip_port, ip_protocol, term_name):

	loader = jinja2.FileSystemLoader(os.getcwd())
	jenv = jinja2.Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)

	template = jenv.get_template("srx-config.j2")
	return template.render(ip_address=ip_address, port=ip_port, protocol=ip_protocol, term_name=term_name)

def fetch():

	command_list = []
	term_list = []

	data = requests.get("http://10.84.29.38:8082/floating-ips")
	data_dict = json.loads(data.content)['floating-ips']
	
	for fip in data_dict:
		try:
			if fip['fq_name'][-1].startswith('frontend'):
				fip_data = requests.get("http://10.84.29.38:8082/floating-ip/" + fip['uuid'])
				fip_data_dict = json.loads(fip_data.content)['floating-ip']
				ip_address = str(fip_data_dict['floating_ip_address']) + "/32"
				ip_port = str(fip_data_dict['floating_ip_port_mappings']['port_mappings'][0]['src_port'])
				ip_protocol = str(fip_data_dict['floating_ip_port_mappings']['port_mappings'][0]['protocol']).lower()
				term_name = str(fip_data_dict['display_name'])	
				config = generateTemplate(ip_address, ip_port, ip_protocol, term_name)

				if not command_list:
					command_list = [line.rstrip("\n") for line in (config.split("\n"))]
				else:
					for line in config.split("\n"):
						command_list.append(line.rstrip("\n"))

				term_list.append(term_name)
		except:
			pass

	return command_list, term_list
fetch()	
