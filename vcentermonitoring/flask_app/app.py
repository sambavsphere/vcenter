from flask import Flask,render_template
from sqlit import get_hosts_info,get_vms_info
app = Flask(__name__)
import json
import pdb

@app.route('/')
def hosts():
    hosts = get_hosts_info()
    header = hosts.columns.tolist()
    data = hosts.to_json(orient='records')
    return render_template('home.html',header= json.dumps(header), data = data, am="hosts")

@app.route('/vms')
def vms():
    hosts = get_vms_info()
    header = hosts.columns.tolist()
    data = hosts.to_json(orient='records')
    return render_template('home.html',header= json.dumps(header), data = data, am="vms")
app.run()