##using example from
##http://libcloud.readthedocs.org/en/latest/compute/examples.html
##as boilerpate
import sys

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
import libcloud.security

from celery import Celery
#from config import config_read



sys.path.insert(0, "../../")

from scaley.module import db

celery = Celery('app', broker='amqp://guest@localhost//') #need to move config over to  flask-ini setup

#the following variables need to be pulled from a configuration file or
#from a config.db
#will need to have encryption built around this

#aws ec2
EC2_ACCESS_ID = ''
EC2_SECRET_KEY = ''
#rackspace
RACKSPACE_USER = ''
RACKSPACE_KEY = ''
#openstack
OS_USERNAME = ''
OS_PASSWORD = ''
OPENSTACKURL = ''
#vcloud
VC_USERNAME = ''
VC_PASSWORD = ''
VCHOST = ''


class EC2:
    @celery.task
    def ec2_compute_details(EC2_ACCESS_ID, EC2_SECRET_KEY):
        EC2Driver = get_driver(Provider.EC2)
        drivers = [EC2Driver(EC2_ACCESS_ID, EC2_SECRET_KEY)]
        instances = []
        locations = []
        for driver in drivers:
            instances += driver.list_nodes()
            locations += driver.list_locations()
            #keypairs += driver.ex_describe_all_keypairs()
            for i in instances:
                instance_id = i.id
                name = i.name
                public_ip = i.public_ips
                private_ip = i.private_ips
                state = i.state
                provider = 'Amazon EC2'
                return instance_id, name, public_ip, private_ip, state, provider

class RSPACE:
    @celery.task
    def rs_compute_details(RACKSPACE_USER, RACKSPACE_KEY):
        RackspaceDriver = get_driver(Provider.RACKSPACE)
        drivers = [RackspaceDriver(RACKSPACE_USER, RACKSPACE_KEY)]
        instances = []
        locations = []
        for driver in drivers:
            instances += driver.list_nodes()
            locations += driver.list_locations()
            for i in instances:
                instance_id = i.id
                name = i.name
                public_ip = i.public_ips
                private_ip = i.private_ips
                state = i.state
                provider = 'Rackspace'
                return instance_id, name, public_ip, private_ip, state, provider

class OPENSTACK:
    @celery.task
    def openstack_compute_details(self, OS_USERNAME, OS_PASSWORD, OPENSTACKURL):
        OpenStack = get_driver(Provider.OPENSTACK)
        driver = OpenStack(USERNAME, PASSWORD,
                   ex_force_auth_url= OPENSTACKURL, #set to 'https://nova-api.trystack.org:5443' to test
                   ex_force_auth_version='2.0_password')
        instances = []
        locations = []
        self.instances = instances
        self.locations = locations
        for driver in drivers:
            instances += driver.list_nodes()
            locations += driver.list_locations() #some of this will be driver specific and may not work
            for i in instances:
                instance_id = i.id
                name = i.name
                public_ip = i.public_ips
                private_ip = i.private_ips
                state = i.state
                provider = "Open Stack"
                return instance_id, name, public_ip, private_ip, state, provider

class VCLOUD:
    @celery.task
    def vcloud_compute_details(self, VC_USERNAME, VC_PASSWORD, VCHOST):
        vcloud = get_driver(Provider.VCLOUD)
        driver = vcloud(USERNAME, PASSWORD,
                host=VCHOST, api_version='1.5')
        instances = []
        locations = []
        self.instances = instances
        self.locations = locations
        for driver in drivers:
            instances += driver.list_nodes()
            locations += driver.list_nodes() #not sure if this will be applicable to this driver
            for i in instances:
                instance_id = i.id
                name = i.name
                public_ip = i.public_ips
                private_ip = i.private_ips
                state = i.state
                provider = "vCloud"
                return instance_id, name, public_ip, private_ip, state, provider
