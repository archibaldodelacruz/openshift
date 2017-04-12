# Simple Web-Server

from flask import Flask
import subprocess

app = Flask(__name__)

def workers():

    cmd_ip = 'ifconfig | sed -n 2p | cut -d ":" -f2 | cut -d " " -f1 | tr -d "\n"'
    cmd_hostname = 'hostname | tr -d "\n"'

    ip_addr = str(subprocess.check_output(cmd_ip, shell=True))
    hostname = str(subprocess.check_output(cmd_hostname, shell=True))

    return '''
<html>
<style>
  h1   {color:red}
  h2   {color:blue}
</style>
  <div align="center">
  <head>
    <title>QA Pod</title>
  </head>
  <body>
    <h1>Hello</h1><br><h2>This page is served by a nginx pod in <b>QA</b> namespace</h2><br><h3>IP address = ''' + ip_addr + '''<br>Hostname = ''' + hostname + '''</h3>
  </body>
  </div>
</html>
'''

@app.route('/')
def root():

    return workers()

@app.route('/dev')
def qa():

    return workers()

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)
