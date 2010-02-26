from zope.interface import implements

from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender
from archetypes.schemaextender.field import ExtensionField

from Products.Archetypes import atapi
from Products.CMFPlone import PloneMessageFactory as _

from interfaces import IAutocategorizeLayer

class ExtendedBooleanField(ExtensionField, atapi.BooleanField):
    """ """

class SchemaExtender(object):
    """ Extend a folder to add the 'Auto-categorize checkbox' """
    implements(IOrderableSchemaExtender, IBrowserLayerAwareExtender)

    layer = IAutocategorizeLayer

    def __init__(self, context):
        self.context = context

    _fields = [
            ExtendedBooleanField('autoCategorizeContent',
                schemata='categorization',
                languageIndependent=True,
                accessor='getAutoCategorizeContent',
                widget=atapi.BooleanWidget(
                    visible={'edit': 'visible', 'view': 'invisible'},
                    label = _(
                        u'label_auto_categorize_content', 
                        default=u'Automatically categorize content newly '
                        'created inside this folder?',
                    ),
                    description=_(
                        u'description_auto_categorize_content', 
                        default=u"Select this option if you want  "
                        "content created inside this folder to automatically "
                        "acquire the same categories. "
                    ),
                ),
            ),
            ]

    def getFields(self):
        return self._fields

    def getOrder(self, original):
        for fieldset in original.keys():
            if "subject" in original[fieldset]:
                ls = original[fieldset]

                if 'categorization' in ls:
                    ls.remove('autoCategorizeContent')
                else:
                    for fs in original.keys():
                        if "autoCategorizeContent" in original[fs]:
                            original[fs].remove("autoCategorizeContent")

                ls.insert(ls.index('subject')+1, 'autoCategorizeContent')
                original[fieldset] = ls
                return original

