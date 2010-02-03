import logging
from zope import interface

try:
    from zope.component.interfaces import ObjectEvent
except ImportError:
    # Legacy Zope 3.2 support
    from zope.app.event.objectevent import ObjectEvent

from interfaces import ISubjectEditedEvent

log = logging.getLogger('slc.autocategorize/events.py')

class SubjectEditedEvent(ObjectEvent):
    interface.implements(ISubjectEditedEvent)
 
def autocategorize(obj, event):
    """ Event handler registered for object adding
    """
    autocategorize = False
    folders = []
    parent = obj.aq_parent
    while parent.meta_type != 'Plone Site':
        if parent.Schema().get('autoCategorizeContent').get(parent):
            autocategorize = True
            folders.append(parent)
        parent = parent.aq_parent

    if autocategorize:
        ocats = list(obj.Subject())
        for parent in folders:
            pcats = parent.Subject()
            if pcats:
                ocats = ocats + [c for c in pcats if c not in ocats]

        obj.setSubject(ocats)

