from aws.heywatch.heywatch import CONFIG
from interfaces import IHeyWatch
from zc.async.interfaces import IQueue
from zope.app.container.interfaces import IContainer
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from zope.component import adapts
from zope.contentprovider.interfaces import IContentProvider
from zope.interface import implements, Interface
from zope.publisher.browser import BrowserView
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class DirectUpload(object):
    implements(IContentProvider)
    adapts(IContainer, IDefaultBrowserLayer, Interface)

    def __init__(self, context, request, view):
        self.__parent__ = self.view = view
        self.context = context
        self.request = request

    def update(self):
        """prepare values for the template
        """
        self.video_id = self.context.__name__
        self.upload_key = CONFIG.get('heywatch', 'upload_key')

    render = ViewPageTemplateFile('direct_upload.pt')


def video_downloader(container, upload_id, video_id):
    """async task that downloads and stores an video
    """
    raise NotImplementedError
    #container['original_video'] = # create the object
    #urllib2.urlopen(

class UploadPingHandler(BrowserView):
    """view that answers to a ping from heywatch,
    and stores the heywatch ids in an annotation
    """
    def __call__(self):
        id = self.request.get('heywatch_video_id')
        upload_id = self.request.form.get('upload_id')
        video_id = self.request.form.get('video_id')
        if id is not None:
            IHeyWatch(self.context).download_id = upload_id
            IHeyWatch(self.context).video_id = video_id

        print 'todo'

            #queue = IQueue(self.context)
            #job = queue.put(Job(video_downloader, self, upload_id, video_id))

            # we don't download now otherwise the ids won't be stored if
            # download fails

            # launch the download job

            #return self.request.response.redirect(
            #                        '@@download?video_id=%s' % str(video_id))

class Download(BrowserView):
    """view that download and stores a video from HeyWatch
    """




