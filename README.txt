redomino.protectdelete
======================

If you want to protect your Plone contents from unnecessary or harmful deletions, you may have a look
at this Plone plugin. With redomino.protectdelete Manager users are the only one who are allowed to 
remove protected objects.

How to tag an object as "protected":

1. Install redomino.protectdelete
2. go to the ZMI (Interfaces tab) to the object you want to protect 
3. apply the redomino.protectdelete.interfaces.IProtectDelete marker interface
4. as long as this plugin is installed, Managers will be the only one able to delete that object.

navigation

Authors
-------

* Davide Moro <davide.moro@redomino.com>

