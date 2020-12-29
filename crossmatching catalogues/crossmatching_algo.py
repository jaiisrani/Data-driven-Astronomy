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

def crossmatch(cat1, cat2, max_dist):
  import numpy as np
  matches_list = []
  no_matches_list = []
  for index_coordinate in cat1:
    ind = index_coordinate[0]
    ra = index_coordinate[1]
    dec = index_coordinate[2]
    
    no_matches_bool = True
    for index_coordinate__ in cat2:
      ind__ = index_coordinate__[0]
      ra__ = index_coordinate__[1]
      dec__ = index_coordinate__[2]
      if angular_dist(ra, dec, ra__, dec__) < max_dist:
        matches_list.append((ind, ind__, angular_dist(ra, dec, ra__, dec__)))
        no_matches_bool = False
     
    if no_matches_bool:
      no_matches_list.append(ind)
  for i in range(len(matches_list)):
    for j in range(len(matches_list)):
      if j != i:
        if not(matches_list[i]=='na' or matches_list[j]=='na'):
          if (matches_list[i][0] == matches_list[j][0]):
            if matches_list[i][2] <= matches_list[j][2]:
              matches_list[j] = 'na'
  na_count = matches_list.count('na')
  for l in range(na_count):
    matches_list.remove('na')
  return matches_list, no_matches_list
