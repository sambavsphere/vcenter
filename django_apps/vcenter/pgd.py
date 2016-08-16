import psycopg2
import vcenter_moule
import pdb
con = psycopg2.connect(user="nexii",password="nexii",host="localhost",port=5432,database="django_db")
cur = con.cursor()
import pandas as pd
def get_hosts_info():
	data = pd.read_sql('select * from host_host',con)
	return data
def get_vms_info():
	data = pd.read_sql('select * from vm_vm',con)
	return data
def fill_vm():
	# vm objects from the vcenter
	allvms = vcenter_moule.get_all_vms()
	# vm's dataframe from the database
	db_vms = get_vms_info()
	record_ids = db_vms['id']
	if len(record_ids.values)>0:
		record_id = record_ids.max()+1
	else:
		record_id=1
	for vm in allvms:
		summary = vm.summary
		if not summary.config.instanceUuid in db_vms['uuid'].values:
			record_id = record_id+1
			name = vm.name
			ip = ""
			uuid = summary.config.instanceUuid
			query = "insert into vm_vm(id,name,ip,uuid) values(%s,'%s','%s','%s')"%(str(record_id),name,ip,uuid)
			cur.execute(query)
			con.commit()
def fill_host():
	# host ovjects from vcenter
	allhosts = vcenter_moule.get_allhosts()
	# hosts dataframe from the database
	db_hosts = get_hosts_info()
	record_ids = db_hosts['id']
	if len(record_ids.values)>0:
		record_id = record_ids.max()+1
	else:
		record_id=1
	for host in allhosts:
		if not host.name in db_hosts['name'].values:
			record_id = record_id+1
			name = host.name
			ip = ""
			uuid = ""
			query = "insert into host_host values(%s,'%s','%s','%s')"%(str(record_id),name,ip,uuid)
			cur.execute(query)
			con.commit()
def get_host_id(name):
	fill_host()
	query = "select id from host_host where name = '%s'"%name
	cur.execute(query)
	data = cur.fetchone()
	return data[0]

def insert_host_details(host_info):
	for host in host_info:
		query = "insert into host_hostdetails ("
		keys1 = map(lambda x:x.lower(),host.keys())
		keys1.remove('name')
		columns = ",".join(keys1)
		columns = "host_id,"+columns
		query = query+columns + ') '
		query = query+ "values("
		values = ""
		for col,val in host.iteritems():
			if not col=="name":
				if not col in ['numberofdatastores',
								'numCpuCores',
								'numNics',
								'numCpuPkgs',
								'numHBAs'
								]:
					if val:
						values = values + "'"+str(val)+"'"+","
					else:
						values = values + "'null',"

				else:
					values = values + str(val) +","
		values = values[:-1]
		host_id = get_host_id(host['name'])
		db_hosts = get_hosts_info()
		record_ids = db_hosts['id'].values
		values = "%s,%s"%(str(host_id),values)
		query = query+values
		query = query+")"
		cur.execute(query)
		con.commit()

def get_vm_id(name):
	fill_vm()
	query = "select id from vm_vm where name = '%s'"%name
	cur.execute(query)
	data = cur.fetchone()
	return data[0]

		
def insert_vm_details(vm_info):
	for vm in vm_info:
		query = "insert into vm_vmdetails ("
		keys = vm.keys()
		keys.remove('name')
		keys = map(lambda x:x.lower(),keys)
		columns = ",".join(keys)
		columns = "vm_id,"+columns
		query = query+columns + ') '
		query = query+ "values("
		values = ""
		for col,val in vm.iteritems():
			if not col=="name":
				if not col in ['memorySizeMB',
								'numCpu',
								'numEthernetCards',
								'numVirtualDisks',
							
								'overallCpuUsage',
								'overallCpuDemand',
							
								]:
					if val:
						values = values + "'"+str(val)+"'"+","
					else:
						values = values + "'null',"

				else:
					values = values + str(val) +","
		values = values[:-1]
		vmid = get_vm_id(vm['name'])
		values = "'%s',%s"%(vmid,values)
		query = query+values
		query = query+")"
		cur.execute(query)
		con.commit()
	