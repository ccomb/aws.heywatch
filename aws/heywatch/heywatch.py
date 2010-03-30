from restlib import RestfulRequest
import os
import string
import urllib2

ACCOUNT_URL = 'http://heywatch.com/account.xml'
URL = 'http://heywatch.com/'
REALM = ''

# read the heywatch user/pass from the user's home
CONFIG = os.path.join(os.path.expanduser('~'), '.heywatch')
if not os.path.exists(CONFIG):
    raise IOError(u'Please provide a config file %s containing user:pass' % CONFIG)

USER, PASS = map(string.strip, open(CONFIG).read().split(':'))


auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password('Web Password', URL, USER, PASS)
opener = urllib2.build_opener(auth_handler)
urllib2.install_opener(opener)

class HeyWatchService(object):
    def _get_account(self):
        request = RestfulRequest(ACCOUNT_URL, method='GET')
        response = urllib2.urlopen(request)
        print response.read()

    account = property(_get_account)
