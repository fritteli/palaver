# Copyright (c) 2005-2008 Christopher Zorn, OGG, LLC 
# See LICENSE.txt for details

from distutils.core import setup
from distutils.sysconfig import get_python_lib
import os


setup(name='palaver',
      version='0.7',
      description='Palaver, a twisted multi-user chat jabber component.',
      author='Christopher Zorn',
      author_email='tofu@thetofu.com',
      url='http://code.stanziq.com/palaver',
      packages=['palaver', 'twisted.plugins', 'palaver.xmpp','palaver.test'],
      package_data={'twisted.plugins': ['twisted/plugins/palaver.py']}
   
      )