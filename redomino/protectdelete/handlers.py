from zExceptions import Redirect

from zope.component import getMultiAdapter

from Products.CMFCore.utils import getToolByName

from redomino.protectdelete.interfaces import IProtectDelete
from redomino.protectdelete.config import PROJECTNAME

def protect_delete(obj, event):
    """ Reindex the revision folder item """
    if IProtectDelete.providedBy(obj):
        portal_quickinstaller = getToolByName(obj, 'portal_quickinstaller')
        if portal_quickinstaller.isProductInstalled(PROJECTNAME):
            membership = getMultiAdapter((obj, obj.REQUEST), name=u'plone_tools').membership()
            if not membership.checkPermission('Manage portal', obj):
                raise Redirect

