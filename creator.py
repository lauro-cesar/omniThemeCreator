#-*- encoding: utf-8 -*-
__author__ = 'olarva'
__company__ = 'HostCERT'
#User: olarva
#Date: 7/10/15
#Time: 10:12 AM


import os
import sys



from setup.themedirs import themeTree



class Creator():
	def __init__(self,themeName,version=2015.06):
		self.themeName=themeName
		self.version = version

	def CreateManifest(self):
		pass


	def CreateTree(self):
		for line in themeTree.split():
			print line




