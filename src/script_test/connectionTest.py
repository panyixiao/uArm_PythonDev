import sys, os
from time import sleep

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

# from uf.wrapper.uarm_api import UarmAPI
from uf.wrapper.swift_api import SwiftAPI
from uf.utils.log import *

print('Start Testing')

swiftPro = SwiftAPI()

sleep(2)
print(swiftPro.get_device_info())

while True:
	print('\nset X340 ...')
	swiftPro.set_position(340, 0, 150)
	print('set X320 ...')
	swiftPro.set_position(320, 0, 150)
	print('set X300 ...')
	swiftPro.set_position(300, 0, 150)
	print('set X200 ...')
	swiftPro.set_position(200, 0, 150)
	print('set X190 ...')
	swiftPro.set_position(190, 0, 150)
	swiftPro.flush_cmd()
	swiftPro.set_buzzer()
	print('doneOnce')
	sleep(10)