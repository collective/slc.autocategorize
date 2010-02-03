from plone.theme.interfaces import IDefaultPloneLayer

try:
    from zope.component.interfaces import IObjectEvent
except ImportError:
    # Legacy Zope 3.2 support
    from zope.app.event.interfaces import IObjectEvent

class IAutocategorizeLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 skin layer bound to a Skin
       Selection in portal_skins.
    """

class ISubjectEditedEvent(IObjectEvent):
    """ Event gets fired when an uploaded file was translated via
        slc.autotranslate 
    """
