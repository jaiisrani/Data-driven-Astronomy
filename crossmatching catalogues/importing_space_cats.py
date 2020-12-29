def import_bss():
  import numpy as np
  cat = np.loadtxt("bss.dat", usecols = range(1, 7))
  coordinates_list = []
  
  for i in range(len(cat)):
    ind = i+1
    ra = 15*(cat[i][0] + cat[i][1]/60 + cat[i][2]/3600)
    if cat[i][3] >= 0:
      dec = cat[i][3] + cat[i][4]/60 + cat[i][5]/3600
    else:
      dec = -1*(-cat[i][3] + cat[i][4]/60 + cat[i][5]/3600)
    coordinates_list.append((ind, ra, dec))
  return coordinates_list

def import_super():
  import numpy as np
  cat = np.loadtxt("super.csv", delimiter=',', skiprows=1, usecols=[0, 1])
  coordinates_list = []
  
  for i in range(len(cat)):
    ind = i+1
    ra = cat[i][0]
    dec = cat[i][1]
    coordinates_list.append((ind, ra, dec))
  return coordinates_list
