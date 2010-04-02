from zope.app.container.interfaces import IContainer
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from zope.component import adapts
from zope.contentprovider.interfaces import IContentProvider
from zope.interface import implements, Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.publisher.browser import BrowserView
from interfaces import IHeyWatch
from aws.heywatch.heywatch import CONFIG

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
        print 'ok'



