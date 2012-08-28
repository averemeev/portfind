# -*- coding: utf-8 -*-
from portfind import portfind

finder = portfind.Finder(True) #  True - показать отладочный лог

print '-' * 10
print finder.get_nets() # можно получить список доступных сетей
print finder.scan_net('192.168.43.*', 8080) # в заданной сети находим хосты с отрктым портом 8080

print '-' * 10
print finder.find_targets(8080) # во всех доступных сетях находит хосты с открытым портом 8080