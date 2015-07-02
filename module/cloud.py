##using example from http://libcloud.readthedocs.org/en/latest/compute/examples.html
##as boilerpate
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from config import config_read

EC2_ACCESS_ID = config_read(AWSACCESSKEYID)
EC2_SECRET_KEY = config_read(AWSSECRET)
RACKSPACE_USER = config_read(RACKSPACEUSER)
RACKSPACE_KEY = config_read(RACKSPACEKEY)

EC2Driver = get_driver(Provider.EC2)
RackspaceDriver = get_driver(Provider.RACKSPACE)

drivers = [EC2Driver(EC2_ACCESS_ID, EC2_SECRET_KEY),
           RackspaceDriver(RACKSPACE_USER, RACKSPACE_KEY)]

nodes = []
for driver in drivers:
    nodes += driver.list_nodes()
print nodes #left in for debugging
# [ <Node: provider=Amazon, status=RUNNING, name=bob, ip=1.2.3.4.5>,
#   <Node: provider=Rackspace, status=REBOOT, name=korine, ip=6.7.8.9>, ... ]

# Reboot all nodes named 'test'
#[node.reboot() for node in nodes if node.name == 'test']
