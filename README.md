# Data-driven-Astronomy
This repo contains all the data-analysis techniques used in Astronomy that I have learnt. 

## Activity 1
Some useful links: \
https://docs.astropy.org/en/stable/index.html# \
https://matplotlib.org \
https://en.wikipedia.org/wiki/FITS 

One of the most widely used formats for astronomical images is the Flexible Image Transport System. In a FITS file, the image is stored in a numerical array, which we can load into a NumPy array. FITS files also have headers which store metadata about the image. FITS files are a standard format and astronomers have developed many libraries (in many programming languages) that can read and write FITS files. We're going to use the Astropy module.\
Here's the code to read a FITS file and find the brightest pixel in the image: https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/FITS/load_fits_and_maxval.py \
The following code computes the mean pixel value of the brightest pixels in each FITS image: https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/FITS/mean_FITS/mean_fits.py 

Now we're going to look at a different statistical measure — the median, which in many cases is considered to be a better measure than the mean due to its robustness to outliers. However, a naïve implementation of the median algorithm can be very inefficient when dealing with large datasets. Luckily, computer scientists have spent a lot of time thinking about this problem and have found some good solutions, such as the Binapprox Algorithm. Visit the following link to read more about it: https://www.datasciencecentral.com/profiles/blogs/some-analysis-with-astronomy-data-in-python \
Here's the code for implementing Binapprox: https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/FITS/median_FITS/Binapprox_algo.py 

Here's a time_stat function to time our statistic implementations. time_stat should take three arguments: the func function we're timing, the size of the random array to test, and the number of experiments to perform. It should return the average running time for the func function.

Write a median_fits function which takes a list of FITS filenames, loads them into a NumPy array, and calculates the median image (where each pixel is the median of that pixel over every FITS file). Your function should return a tuple of the median NumPy array, the time it took the function to run, and the amount of memory (in kB) used to store all the FITS files in the NumPy array in memory. The running time should include loading the FITS files and calculating the median.

## Activity 2
When investigating astronomical objects, like active galactic nuclei (AGN), astronomers compare data about those objects from different telescopes at different wavelengths. This requires positional cross-matching to find the closest counterpart within a given radius on the sky. In this activity you'll cross-match two catalogues: one from a radio survey, the AT20G Bright Source Sample (BSS) catalogue and one from an optical survey, the SuperCOSMOS all-sky galaxy catalogue.
The BSS catalogue lists the brightest sources from the AT20G radio survey while the SuperCOSMOS catalogue lists galaxies observed by visible light surveys. If we can find an optical match for our radio source, we are one step closer to working out what kind of object it is, e.g. a galaxy in the local Universe or a distant quasar.\
BSS: http://cdsarc.u-strasbg.fr/viz-bin/Cat?J/MNRAS/384/775 \
SuperCOSMOS: http://ssa.roe.ac.uk/allSky \
This is how the BSS data looks like: \
https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/crossmatching%20catalogues/bss.dat \
https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/crossmatching%20catalogues/bss.png
This is how the SuperCOSMOS data looks like: \
https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/crossmatching%20catalogues/super.csv \
https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/crossmatching%20catalogues/super.png 

A point on the celestial sphere is given by two coordinates:\
Right ascension: the angle from the vernal equinox to the point, going east along the celestial equator;\
Declination: the angle from the celestial equator to the point, going north (negative values indicate going south).\
The vernal equinox is the intersection of the celestial equator and the ecliptic where the ecliptic rises above the celestial equator going further east.\
Right ascension is often given in hours-minutes-seconds (HMS) notation, because it was convenient to calculate when a star would appear over the horizon. A full circle in HMS notation is 24 hours, which means 1 hour in HMS notation is equal to 15 degrees. Each hour is split into 60 minutes and each minute into 60 seconds.\
Declination, on the other hand, is traditionally recorded in degrees-minutes-seconds (DMS) notation. A full circle is 360 degrees, each degree has 60 arcminutes and each arcminute has 60 arcseconds.\
Here's how to convert both to decimal degrees: https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/crossmatching%20catalogues/decimal_angle.py 

To crossmatch two catalogues we need to compare the angular distance between objects on the celestial sphere. People loosely call this a "distance", but technically its an angular distance: the projected angle between objects as seen from Earth. For this purpose we use the Haversine formula https://en.wikipedia.org/wiki/Haversine_formula .\
Following is the code to find the angular distance between 2 heavely bodies: https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/crossmatching%20catalogues/angular_distance.py 

Now we will see how to load space catalogues: https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/crossmatching%20catalogues/importing_space_cats.py 

Write a find_closest function that takes a catalogue and the position of a target source (a right ascension and declination) and finds the closest match for the target source in the catalogue. Your function should return the ID of the closest object and the distance to that object. The right ascension and declination are in degrees. https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/crossmatching%20catalogues/find_closest.py 

Write a crossmatch function that crossmatches two catalogues within a maximum distance. It should return a list of matches and non-matches for the first catalogue against the second. The list of matches contains tuples of the first and second catalogue object IDs and their distance. The list of non-matches contains the unmatched object IDs from the first catalogue only. Both lists should be ordered by the first catalogue's IDs. The BSS and SuperCOSMOS catalogues will be given as input arguments, each in the format you’ve seen previously. The maximum distance is given in decimal degrees. https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/crossmatching%20catalogues/crossmatching_algo.py






