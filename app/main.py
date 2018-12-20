import os
import logging
import socket
from flask import Flask
from flask_kerberos import requires_authentication, init_kerberos

HOME_DIR = os.environ.get('OPENSHIFT_HOMEDIR', os.getcwd())
SERVICE_PRINCIPAL = os.environ.get('SERVICE_PRINCIPAL', 'flask')

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)

DEBUG=True

init_kerberos(app, hostname=SERVICE_PRINCIPAL)

@app.route('/')
def root():
    return """
    <ul>
    <li>HOST_NAME: {}</li>
    <li>SERVICE_PRINCIPAL: {}</li>
    </ul>
    <a href="/secured">continue to krb5 secured site</a>
    """.format(socket.gethostname(), SERVICE_PRINCIPAL)

@app.route('/secured')
@requires_authentication
def secured(user):
    return """
    <ul>
    <li>HOST_NAME: {}</li>
    <li>SERVICE_PRINCIPAL: {}</li>
    <li>USER: {}</li>
    </ul>
    <a href="/">back to unsecured site</a>
    """.format(socket.gethostname(), SERVICE_PRINCIPAL, user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
