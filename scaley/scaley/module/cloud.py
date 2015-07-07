##using example from http://libcloud.readthedocs.org/en/latest/compute/examples.html
##as boilerpate
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from config import config_read

def getKey(Node):
    return Node.private_ips

EC2_ACCESS_ID = ''
EC2_SECRET_KEY = ''
#RACKSPACE_USER = config_read(RACKSPACEUSER)
#RACKSPACE_KEY = config_read(RACKSPACEKEY)

EC2Driver = get_driver(Provider.EC2)
#RackspaceDriver = get_driver(Provider.RACKSPACE)

# drivers = [EC2Driver(EC2_ACCESS_ID, EC2_SECRET_KEY),
#            RackspaceDriver(RACKSPACE_USER, RACKSPACE_KEY)]

drivers = [EC2Driver(EC2_ACCESS_ID, EC2_SECRET_KEY)]
nodes = []
instances = []
locations = []
keypairs = []
for driver in drivers:
    instances += driver.list_nodes()
    locations += driver.list_locations()
    keypairs += driver.ex_describe_all_keypairs()
    for i in instances:
        #print i
        instance_id = i.id
        name = i.name
        public_ip = i.public_ips
        private_ip = i.private_ips
        state = i.state
        provider = 'Amazon EC2'
        print instance_id, name, public_ip, private_ip, state, provider
        #for l in locations:
            #location_name = l.name
            #print location_name
            #for k in keypairs:
                #print k
        #print sorted(i, key='name')
    #print locations
    #print keypairs
#print keypairs
#left in for debugging
# [ <Node: provider=Amazon, status=RUNNING, name=bob, ip=1.2.3.4.5>,
#   <Node: provider=Rackspace, status=REBOOT, name=korine, ip=6.7.8.9>, ... ]

# Reboot all nodes named 'test'
#[node.reboot() for node in nodes if node.name == 'test']
