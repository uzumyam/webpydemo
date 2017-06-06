import web

web.config.db_parameters = dict(dbn='mysql', db='mytest', user='testadmin',pw='123')
web.webapi.internalerror = web.debugerror
middleware = [web.reloader]
cache = False