###
# Copyright (c) 2013-2014, spline
# All rights reserved.
#
#
###

from supybot.test import *

class GitPullTestCase(PluginTestCase):
    plugins = ('GitPull',)
    
    def testGitPull(self):
        self.assertNotError('updateplugin GitPull')
    
    def testGitPullError(self):
        self.assertRegexp('updateplugin HELLO2U', "ERROR:.*?is an invalid plugin")
    


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
