import engine

commanager = engine.Commanager()
textmanager = engine.TextManager()

commanager.addcom('test', ('mmmmmmmm', 'yum'))

textmanager.printslow(commanager.procinput('test mmmmmmmmm yum'))
