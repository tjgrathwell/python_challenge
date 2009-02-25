from xmlrpclib import Server
import urllib2, Cookie

cookie = Cookie.SimpleCookie()
cookie['info'] = 'the+flowers+are+on+their+way'

#server_url = 'http://www.pythonchallenge.com/pc/phonebook.php'
server_url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
server = Server(server_url)
f = urllib2.urlopen(server_url)
print f.info()
#print server

result = server.system.listMethods()
#result = server.phone('Leopold')
#print result

#solution italy

#second solution violin

#final solution balloons