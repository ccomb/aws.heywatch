from zope.interface import implements
from zope.component import adapts
from interfaces import IHeyWatch, IHeyWatchable


class HeyWatch(object):
    """adapter providing IHeyWatch features for IHeyWatchable objects
    """
    implements(IHeyWatch)
    adapts(IHeyWatchable)

    def __init__(self, context):
        self.context = context


