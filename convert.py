#!/illumina/software/PY276/bin/python
#This is a program  for calculate the quality of my data using fastqc FastQC v0.10.1

#Author: Maurizio Polano, mauriziopolano@blu.it
#Last revision: 03/06/2014

import subprocess
import os,os.path
import sys
import time
import json
import re
from optparse import OptionParser


def main():
	# select inupt
	parser = OptionParser() 
	parser = OptionParser(usage="usage: %prog   -d [directory ]  -l list file id -h help  ",
							  version="%prog 1.0")
	parser.add_option("-i", "--input", dest="name",type="string",help=" write input file: %prg -i: Please insert the name the Path of the results files [REQUIRED]")
	parser.add_option("-o", "--output", dest="out",type="string",help=" write input file: %prg -o: out [REQUIRED]")
	


	(options, args) = parser.parse_args(args=None, values=None)


	
	
	



	options, args = parser.parse_args()
	



	import requests
	import json 
	
	 


	if options.name:

		
		
		fileh = open(options.out,"w")
		server = "http://grch37.rest.ensembl.org"
		with open( options.name,"r") as p:
			for i in p:
				if i[0] != "#":
					lines = i.rstrip("\n").split("\t")
					name = re.findall("ENST\d\d+",lines[0])
					other=  lines[3:]
					ext = "/map/cdna/"+name[0]+"/"+lines[1]+".."+str(lines[1])+"?"
			

					r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
				 
					if not r.ok:
					  r.raise_for_status()
					  sys.exit()
					 
					decoded = r.json()
				
					
					for row in decoded.keys():
						for item in decoded[row]:
							#print item["seq_region_name"],item['start'],item['end']
							print >>fileh, str(item['seq_region_name'])+"\t"+str(item['start'])+"\t"+str(item['end'])+"\t"+"\t".join(other)

			



				
		fileh.close()

	

if __name__ == "__main__":
	main()

	
