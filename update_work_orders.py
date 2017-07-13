#!/usr/bin/python
import requests
import sys
import csv
import configparser
import xml.etree.ElementTree as ET

def get_key():
	return config.get('Params', 'apikey')

def get_url():
	return config.get('Params','baseurl')

def get_library():
	return config.get('Params','library')

def get_circdesk():
	return config.get('Params','circdesk')

def get_wo_status():
	return config.get('Params','workorder_status')

def get_wo():
	return config.get('Params','workorder')

# Creates item API URL
def createurl(row):
	bib_id = row[0]
	holding_id = row[1]
	item_id = row[2]
	return '/almaws/v1/bibs/' + bib_id + '/holdings/'+ holding_id +'/items/' + item_id;

# Creates URL query parameters
def make_query():
	query = '?op=scan' + '&library=' + get_library() + '&circ_desk=' + get_circdesk()
	query =  query + '&work_order_type='+ get_wo() + '&status=' + get_wo_status()
	return query

# Reads in file of physical items, as exported from Alma
f = open(items_file, 'rt')
try:
    reader = csv.reader(f)
    next(reader)#skip header line
    for row in reader:
    	if row[0] != 'end-of-file':
    		apicall = createurl(row)
    		url = get_url() + apicall + make_query()
    		print (url)
    		response = requests.post(url, data={'apikey' : get_key()})
    		print (response.content)
finally:
    f.close()


# Read campus parameters
config = configparser.RawConfigParser()
config.read(sys.argv[1])

# CSV file of items to be checked in
items_file = sys.argv[2]
