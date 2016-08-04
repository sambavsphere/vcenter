import sqlite3
con = sqlite3.connect('db.sqlite3')
import pandas as pd
def get_hosts_info():
	data = pd.read_sql('select * from app1_hostinfo',con)
	return data
def get_vms_info():
	data = pd.read_sql('select * from app1_vminfo',con)
	return data
def get_host_info(host):
	return "host"
def get_vm_info(vm):
	return "vm"
def insert_host_info(host_info):
	for host in host_info:
		query = "insert into app1_hostinfo ("
		columns = ",".join(host.keys())
		#columns = columns[:-1]
		query = query+columns + ') '
		query = query+ "values("
		values = ""
		for col,val in host.iteritems():
			if not col in ['numberofdatastores',
							'memorySize',
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
		query = query+values
		query = query+")"
		con.execute(query)
		con.commit()
		
def insert_vm_info(vm_info):
	for vm in vm_info:
		query = "insert into app1_vminfo ("
		columns = ",".join(vm.keys())
		query = query+columns + ') '
		query = query+ "values("
		values = ""
		for col,val in vm.iteritems():
			if not col in ['memorySizeMB',
							'numCpu',
							'numEthernetCards',
							'numVirtualDisks',
							'committed',
							'uncommitted',
							'overallCpuUsage',
							'overallCpuDemand',
							'guestMemoryUsage',
							'hostMemoryUsage',
							'privateMemory'
							]:
				if val:
					values = values + "'"+str(val)+"'"+","
				else:
					values = values + "'null',"

			else:
				values = values + str(val) +","
		values = values[:-1]
		query = query+values
		query = query+")"
		con.execute(query)
		con.commit()
	