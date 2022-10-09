#!/usr/bin/env python3
import re

action = []
with open('route_admin.php') as l:
	for c in l:
		str_num = c.count('/')
		if str_num > 2:
			arr = c.split('=>')
			c_a = arr[0]
			a_arr = c_a.split('/')
			e_str = a_arr[-1]
			r_f = re.findall('^\w+', e_str)
			new_str = r_f[0]
			action.append(new_str)
			
print(action)