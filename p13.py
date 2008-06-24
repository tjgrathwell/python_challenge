# http://www.pythonchallenge.com/pc/return/disproportional.html

# ahh the old RPC one...

# http://www.pythonchallenge.com/pc/phonebook.php returns XML

# we want to phone bert

from xmlrpclib import ServerProxy, Error
server = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print server.system.listMethods()
# ['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']
print server.phone('Bert')
# 555-ITALY