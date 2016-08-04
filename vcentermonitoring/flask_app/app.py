from flask import Flask,render_template
from sqlit import get_hosts_info,get_vms_info
app = Flask(__name__)

@app.route('/')
def hello_world():
    allhsots = get_hosts_info()
    print allhsots,'$$$$$$$$$$$$$$$$$$$$$$$4'
    return render_template('home.html',hosts=allhsots)
app.run()