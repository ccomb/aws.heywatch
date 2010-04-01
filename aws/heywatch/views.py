from zope.app.container.interfaces import IContainer
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from zope.component import adapts
from zope.contentprovider.interfaces import IContentProvider
from zope.interface import implements, Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

class DirectUpload(object):
    implements(IContentProvider)
    adapts(IContainer, IDefaultBrowserLayer, Interface)

    def __init__(self, context, request, view):
        self.__parent__ = self.view = view
        self.context = context
        self.request = request

    def update(self):
        pass

    render = ViewPageTemplateFile('direct_upload.pt')






