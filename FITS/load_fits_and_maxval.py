def load_fits(filename):
  import numpy as np
  from astropy.io import fits
  import matplotlib.pyplot as plt
  
  hdulist = fits.open(filename)
  data = hdulist[0].data
  ind = np.unravel_index(np.argmax(data, axis=None), data.shape)
  plt.imshow(data, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()
  return ind
