from math import sqrt

def check_square_and_cube(list):
  print('in check')
  root = sqrt(list[0])
  cube = root ** 3
  if cube == list[1]:
  	return 'true'
  else:
  	return 'false'
      
print(check_square_and_cube([4, 8]))