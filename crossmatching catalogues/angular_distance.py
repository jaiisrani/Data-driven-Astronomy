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
