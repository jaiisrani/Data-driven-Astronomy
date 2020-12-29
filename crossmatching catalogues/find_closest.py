def hms2dec(h, m, s):
  return 15*(h + m/60 + s/3600) 
def dms2dec(d, m, s):
  if d >= 0:
    return (abs(d) + m/60 + s/3600)
  else:
    return -(abs(d) + m/60 + s/3600)

def angular_dist(ra1, dec1, ra2, dec2):
  import numpy as np
  ra1 = np.radians(ra1)
  dec1 = np.radians(dec1)
  ra2 = np.radians(ra2)
  dec2 = np.radians(dec2)
 
  a = (np.sin((dec1 - dec2)/2))**2
  b = np.cos(dec1)*np.cos(dec2)*(np.sin((ra1 - ra2)/2))**2
  
  dist_rad = 2*np.arcsin(np.sqrt(a + b))
  dist_deg = np.degrees(dist_rad)
  return dist_deg

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

def find_closest(cat, ra_given, dec_given):
  closest_ind = 1 
  for i in range(len(cat)):
    ind = cat[i][0]
    ra = cat[i][1]
    dec = cat[i][2]
    closest_ra = cat[closest_ind-1][1]
    closest_dec = cat[closest_ind-1][2]
    if angular_dist(ra_given, dec_given, ra, dec) < angular_dist(ra_given, dec_given, closest_ra, closest_dec):
      closest_ind = ind
  return (closest_ind, angular_dist(ra_given, dec_given, cat[closest_ind-1][1], cat[closest_ind-1][2]))
