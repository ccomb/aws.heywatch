from zope.interface import implements
from zope.component import adapts
from interfaces import IHeyWatch, IHeyWatchable
from persistent import Persistent
import zope.annotation
from zope.annotation.interfaces import IAttributeAnnotatable

class HeyWatch(Persistent):
    """adapter providing IHeyWatch features for IHeyWatchable objects
    """
    implements(IHeyWatch)
    adapts(IHeyWatchable)

    def __init__(self):
        pass

heywatchfactory = zope.annotation.factory(HeyWatch)


