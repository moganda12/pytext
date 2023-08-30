import engine

commanager = engine.Commanager()

commanager.addcom('test', ('mmmmmmmm', 'yum'))

print(commanager.procinput(input('command:')))
