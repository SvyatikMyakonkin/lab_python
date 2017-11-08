! /usr/bin/env python3
 # -*- coding: utf-8 -*-
import re
 
 def ispalindr(s):
 	s = s.lower()
	s = s.replace(" ", "")
	s = re.sub('\W+', '', s)
	print(s)
 	return True if s == s[::-1] else False
 
 s = input("Enter string: ")s
