#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nmap import nmap
import netifaces

FIND_PORT = 8080

class Finder:

	port = 8080

	def __init__(self, port, debug = False):
		self.port = port
		self.debug = debug

	def get_nets(self):
		nets = []
		ifs = netifaces.interfaces()
		ifs.remove('lo')
		ifs.remove('ppp0')
		for ifs_name in ifs:
			try:
				info = netifaces.ifaddresses(ifs_name)
				inet = info[netifaces.AF_INET]
				addr = inet[0]['addr']
				base = addr[:addr.rindex('.')]
				scan = base + '.*'
				nets.append(scan)
			except:
				pass
		if self.debug:
			print 'find nets: %s' % ' '.join(nets)
		return nets

	def scan_net(self, net, port):
		if self.debug:
			print 'scan net %s, try to find port %s' % (net, port)
		targets = []
		scanner = nmap.PortScanner()
		result	= scanner.scan(net)
		hosts 	= scanner.all_hosts()
		if self.debug:
			print 'found hosts in net: %s' % ' '.join(hosts)
		for host in hosts:
			if scanner[host]['tcp'].has_key(self.port):
				targets.append(host)
		if self.debug:
			print 'find hosts with port %s: %s' % (self.port, ' '.join(targets)) 
		return targets

	def find_targets(self):
		nets = self.get_nets()
		all_targets = []
		for net in nets:
			net_targets = self.scan_net(net, self.port)
			all_targets += net_targets
		return all_targets

def main():
	import sys
	try:
		port = int(sys.argv[1])
	except:
		print 'usage: %s %s' % (sys.argv[0], '[port] -d(debug)')
		return None

	debug = False
	try:
		debug = sys.argv[2]
		if debug == '-d':
			debug = True
	except:
		pass

	finder = Finder(port, debug)
	targets = finder.find_targets()
	for target in targets:
		print target

if __name__ == '__main__':
	main()