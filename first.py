from pyVim.connect import SmartConnect
import ssl
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
si=SmartConnect(host="",port=443,user="root",pwd="",sslContext=gcontext)
c = si.RetrieveContent()
rootfolder = c.rooFolder()
for datacenter in rootfolder.childEntity:
	print datacenter.name
