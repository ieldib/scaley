import ConfigParser

config = ConfigParser.ConfigParser()



class ConfigWrite:

    def write_aws_config(accesskeyid,secret):
        #some code
        pass
    def write_rackspace_config(accesskeyid,secret):
        #some code
        pass
    def write_openstack_config(accesskeyid,secret):
        #somecode
        pass
    def write_azure_config(accesskeyid,secret):
        #somecode
        pass
    def write_azure_config(accesskeyid, secret):
        #somecode
        pass

    def default_write_config(self):
        config['AWS'] = {'AWSACCESSKEYID': 'NONE',
                         'AWSACESSSECRETKEY': 'NONE'}
        config['RACKSPACE'] = {'RACKSPACEACCESSKEY': 'NONE',
                               'RACKSPACESECRET': 'NONE'}
        with open('../config.cfg', 'w') as configfile:
            configfile.write(configfile)

    def __init__(self):
        self.accesskeyid = accesskeyid
        self.secret = secret

class ConfigRead:
    def readconfig(self):
        configread = config.read('../config.cfg')

    def __init__(self):
        self.configread = self.readconfig(configread)
