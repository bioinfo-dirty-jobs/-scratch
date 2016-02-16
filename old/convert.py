#!/usr/bin/python

#Author: Maurizio Polano, mauriziopolano@blu.it
#Last revision: 03/06/2014

import subprocess
import os,os.path
import sys
import time

import re
from optparse import OptionParser


def main():
	# select inupt
	parser = OptionParser() 
	parser = OptionParser(usage="usage: %prog   -d [directory ]  -l list file id -h help  ",
							  version="%prog 1.0")
	parser.add_option("-i", "--input", dest="name",type="string",help=" write input file: %prg -i: Please insert the name the Path of the results files [REQUIRED]")
	parser.add_option("-l", "--left", dest="left",type="string",help=" write input file: %prg -l: position  left [REQUIRED]")
	parser.add_option("-r", "--right", dest="dx",type="string",help=" write input file: %prg -r: position  dx [REQUIRED]")
	parser.add_option("-o", "--output", dest="out",type="string",help=" write input file: %prg -o: out [REQUIRED]")
	


	(options, args) = parser.parse_args(args=None, values=None)


	
	
	



	options, args = parser.parse_args()
	



	import requests
	 
	
	 


	if options.name:

		
		
		fileh = open(options.out,"w")
		server = "http://rest.ensembl.org"
		ext = "/map/cdna/"+options.name+"/"+options.left+".."+options.dx+"?"
		 
		r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
		 
		if not r.ok:
		  r.raise_for_status()
		  sys.exit()
		 
		decoded = r.json()
		print repr(decoded)
		print  >> fileh, decoded	



				
		fileh.close()

	

if __name__ == "__main__":
	main()

	

