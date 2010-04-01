from restlib import RestfulRequest
from cStringIO import StringIO
from lxml import etree
from lxml import objectify
import os
import string
import urllib2
import time

URL = 'http://heywatch.com/'
REALM = 'Web Password'

# read the heywatch user/pass from the user's home
CONFIG = os.path.join(os.path.expanduser('~'), '.heywatch')
if not os.path.exists(CONFIG):
    raise IOError(u'Please provide a config file %s containing user:pass' % CONFIG)

USER, PASS = map(string.strip, open(CONFIG).read().split(':'))


auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password(REALM, URL, USER, PASS)
opener = urllib2.build_opener(auth_handler)
urllib2.install_opener(opener)


class HeyWatchService(object):

    _cache = {} # {'account': (access_time, value), }

    def _get(self, service, cache_timeout=0):
        """get a possibly cached value by HTTP GET
        """
        access_time, value = self._cache.get(service, (0, ''))
        if time.time() - access_time > cache_timeout:
            request = RestfulRequest(URL+service, method='GET')
            response = urllib2.urlopen(request)
            value = response.read()
            self._cache[service] = (time.time(), value)
        return value

    def _post(self, service, data):
        """send values by HTTP POST
        """
        request = RestfulRequest(URL+service, data=data, method='POST')
        response = urllib2.urlopen(request)
        value = response.read()
        return value

    def get_account(self):
        """get account information
        """
        value = self._get('account.xml', 60)
        return objectify.parse(StringIO(value)).getroot()

    def get_encoded_videos(self):
        """Get information about your encoded videos
        """
        value = self._get('encoded_video.xml', 10)
        return objectify.parse(StringIO(value)).getroot()

    def get_encoded_video(self, id):
        """Get information about a specific encoded video
        id is the HeyWatch identifier of the video (int or str)
        """
        assert(str(id).isdigit())
        value = self._get('encoded_video/%s.xml' % str(id), 10)
        return objectify.parse(StringIO(value)).getroot()

    def get_videos(self):
        """Get information about your encoded videos
        """
        value = self._get('video.xml', 30)
        return objectify.parse(StringIO(value)).getroot()

    def get_video(self, id):
        """Get information about a specific video
        id is the HeyWatch identifier of the video (int or str)
        """
        assert(str(id).isdigit())
        value = self._get('video/%s.xml' % str(id), 10)
        return objectify.parse(StringIO(value)).getroot()

    def get_formats(self):
        """Get information about all formats
        """
        value = self._get('format.xml', 60)
        return objectify.parse(StringIO(value)).getroot()

    def get_format(self, id):
        """Get information about a specific format
        id is the HeyWatch identifier of the format (int or str)
        """
        assert(str(id).isdigit())
        value = self._get('format/%s.xml' % str(id))
        return objectify.parse(StringIO(value)).getroot()

    def get_jobs(self):
        """Get information about all jobs
        """
        value = self._get('job.xml', 10)
        return objectify.parse(StringIO(value)).getroot()

    def get_job(self, id):
        """Get information about a specific job
        id is the HeyWatch identifier of the job (int or str)
        """
        assert(str(id).isdigit())
        value = self._get('job/%s.xml' % str(id), 10)
        return objectify.parse(StringIO(value)).getroot()

    def get_downloads(self):
        """Get information about all downloads
        """
        value = self._get('download.xml', 10)
        return objectify.parse(StringIO(value)).getroot()

    def get_download(self, id):
        """Get information about a specific download
        id is the HeyWatch identifier of the job (int or str)
        """
        assert(str(id).isdigit())
        value = self._get('download/%s.xml' % str(id), 10)
        return objectify.parse(StringIO(value)).getroot()

    def upload(self, data, title='', max_length=None):
        raise NotImplementedError
        #value = self._post('upload.xml', data)
        #return value



