# -*- coding: utf-8 -*- def isEmail(s):
return re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)',s) == None
