from zExceptions import Redirect

from zope.component import getMultiAdapter

from plone.app.layout.navigation.interfaces import INavigationRoot 

from Products.statusmessages.interfaces import IStatusMessage
from Products.CMFCore.utils import getToolByName

from redomino.protectdelete.interfaces import IProtectDelete
from redomino.protectdelete.config import PROJECTNAME
from redomino.protectdelete import protectdeleteMessageFactory as _


def protect_delete(obj, event):
    """ Reindex the revision folder item.
        
        Protected contents are marked with the following marker interfaces:
            * IProtectDelete, the marker interface provided by this plugin
            * INavigationRoot (for example language folders like it, fr, en, ecc)

        IMPORTANT: managers are not affected by these rules.
    """
    if IProtectDelete.providedBy(obj) or INavigationRoot.providedBy(obj):
        portal_quickinstaller = getToolByName(obj, 'portal_quickinstaller')
        if portal_quickinstaller.isProductInstalled(PROJECTNAME):
            membership = getMultiAdapter((obj, obj.REQUEST), name=u'plone_tools').membership()
            if not membership.checkPermission('Manage portal', obj):
                IStatusMessage(obj.REQUEST).addStatusMessage(_('label_cannotdelete', default='You cannot delete this item'), type='warning')

                view_url = getMultiAdapter((obj, obj.REQUEST), name=u'plone_context_state').view_url()
                raise Redirect, view_url

