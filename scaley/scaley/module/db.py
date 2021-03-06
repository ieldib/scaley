import sys
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

sys.path.insert(0, "../../")

from scaley import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////scaley/scaley/db/scaley.db'

db = SQLAlchemy(app)
class CloudConfig(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    awsaccesskeyid = db.Column(db.String(80), unique=True)
    awssecretkey = db.Column(db.String(120), unique=True)
    rackspace_user = db.Column(db.String(80), unique=True)
    rackspace_key = db.Column(db.String(120), unique=True)
    os_username = db.Column(db.String(80), unique=True)
    os_password = db.Column(db.String(120), unique=True)
    openstackurl = db.Column(db.String(160), unique=True)
    vc_username = db.Column(db.String(80), unique=True)
    vc_password = db.Column(db.String(120), unique=True)
    vchost = db.Column(db.String(160), unique=True)


    def __init__(self, awsaccesskeyid, awssecretkey, rackspace_user,
                 rackspace_key, os_username, os_password, openstackurl,
                 vc_username, vc_password, vchost, uid ):
        self.awsaccesskeyid = awsaccesskeyid
        self.awssecretkey = awssecretkey
        self.rackspace_user = rackspace_user
        self.rackspace_key = rackspace_key
        self.os_username = os_username
        self.os_password = os_password
        self.openstackurl = openstackurl
        self.vc_username = vc_username
        self.vc_password = vc_password
        self.vchost = vchost
        self.uid = uid

    def __repr__(self):
        return 'CloudConfig(uid=%s) % self.uid'
