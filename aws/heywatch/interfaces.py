from zope.interface import Interface
from zope.annotation.interfaces import IAttributeAnnotatable

class IHeyWatch(Interface):
    """HeyWatch features"""

class IHeyWatchable(IAttributeAnnotatable):
    """HeyWatch marker interface"""
