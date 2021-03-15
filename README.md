# Data-driven-Astronomy
This repo contains all the data-analysis techniques used in Astronomy that I have learnt. 

## Activity 1: Detecting Quasars 
Some useful links: \
https://docs.astropy.org/en/stable/index.html# \
https://matplotlib.org \
https://en.wikipedia.org/wiki/FITS 

One of the most widely used formats for astronomical images is the Flexible Image Transport System. In a FITS file, the image is stored in a numerical array, which we can load into a NumPy array. FITS files also have headers which store metadata about the image. FITS files are a standard format and astronomers have developed many libraries (in many programming languages) that can read and write FITS files. We're going to use the Astropy module.\
Here's the code to read a FITS file and find the brightest pixel in the image: \
https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/FITS/load_fits_and_maxval.py \
The following code computes the mean pixel value of the brightest pixels in each FITS image: \
https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/FITS/mean_FITS/mean_fits.py 

Now we're going to look at a different statistical measure — the median, which in many cases is considered to be a better measure than the mean due to its robustness to outliers. However, a naïve implementation of the median algorithm can be very inefficient when dealing with large datasets. Luckily, computer scientists have spent a lot of time thinking about this problem and have found some good solutions, such as the Binapprox Algorithm. Visit the following link to read more about it:\
https://www.datasciencecentral.com/profiles/blogs/some-analysis-with-astronomy-data-in-python \
Here's the code for implementing Binapprox: \
https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/FITS/median_FITS/Binapprox_algo.py 

Here's a time_stat function to time our statistic implementations. time_stat should take three arguments: the func function we're timing, the size of the random array to test, and the number of experiments to perform. It should return the average running time for the func function.

Write a median_fits function which takes a list of FITS filenames, loads them into a NumPy array, and calculates the median image (where each pixel is the median of that pixel over every FITS file). Your function should return a tuple of the median NumPy array, the time it took the function to run, and the amount of memory (in kB) used to store all the FITS files in the NumPy array in memory. The running time should include loading the FITS files and calculating the median.

## Activity 2: Inter-galactic distances
When investigating astronomical objects, like active galactic nuclei (AGN), astronomers compare data about those objects from different telescopes at different wavelengths. This requires positional cross-matching to find the closest counterpart within a given radius on the sky. In this activity you'll cross-match two catalogues: one from a radio survey, the AT20G Bright Source Sample (BSS) catalogue and one from an optical survey, the SuperCOSMOS all-sky galaxy catalogue.
The BSS catalogue lists the brightest sources from the AT20G radio survey while the SuperCOSMOS catalogue lists galaxies observed by visible light surveys. If we can find an optical match for our radio source, we are one step closer to working out what kind of object it is, e.g. a galaxy in the local Universe or a distant quasar.\
BSS: http://cdsarc.u-strasbg.fr/viz-bin/Cat?J/MNRAS/384/775 \
SuperCOSMOS: http://ssa.roe.ac.uk/allSky \
This is how the BSS data looks like: \
https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/crossmatching%20catalogues/bss.dat \
https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/crossmatching%20catalogues/bss.png \
This is how the SuperCOSMOS data looks like: \
https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/crossmatching%20catalogues/super.csv \
https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/crossmatching%20catalogues/super.png 

A point on the celestial sphere is given by two coordinates:\
-Right ascension: the angle from the vernal equinox to the point, going east along the celestial equator;\
-Declination: the angle from the celestial equator to the point, going north (negative values indicate going south).\
The vernal equinox is the intersection of the celestial equator and the ecliptic where the ecliptic rises above the celestial equator going further east.\
Right ascension is often given in hours-minutes-seconds (HMS) notation, because it was convenient to calculate when a star would appear over the horizon. A full circle in HMS notation is 24 hours, which means 1 hour in HMS notation is equal to 15 degrees. Each hour is split into 60 minutes and each minute into 60 seconds.\
Declination, on the other hand, is traditionally recorded in degrees-minutes-seconds (DMS) notation. A full circle is 360 degrees, each degree has 60 arcminutes and each arcminute has 60 arcseconds.\
Here's how to convert both to decimal degrees:\
https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/crossmatching%20catalogues/decimal_angle.py 

To crossmatch two catalogues we need to compare the angular distance between objects on the celestial sphere. People loosely call this a "distance", but technically its an angular distance: the projected angle between objects as seen from Earth. For this purpose we use the Haversine formula https://en.wikipedia.org/wiki/Haversine_formula .\
Following is the code to find the angular distance between 2 heavely bodies:\
https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/crossmatching%20catalogues/angular_distance.py 

Now we will see how to load space catalogues:\
https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/crossmatching%20catalogues/importing_space_cats.py 

Write a find_closest function that takes a catalogue and the position of a target source (a right ascension and declination) and finds the closest match for the target source in the catalogue. Your function should return the ID of the closest object and the distance to that object. The right ascension and declination are in degrees:\
https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/crossmatching%20catalogues/find_closest.py 

Write a crossmatch function that crossmatches two catalogues within a maximum distance. It should return a list of matches and non-matches for the first catalogue against the second. The list of matches contains tuples of the first and second catalogue object IDs and their distance. The list of non-matches contains the unmatched object IDs from the first catalogue only. Both lists should be ordered by the first catalogue's IDs. The BSS and SuperCOSMOS catalogues will be given as input arguments, each in the format you’ve seen previously. The maximum distance is given in decimal degrees.\ https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/crossmatching%20catalogues/crossmatching_algo.py

## Activity 3: Estimating Galaxy-Redshifts
In this activity, we're going to use decision trees to determine the redshifts of galaxies from their photometric colours. We'll use galaxies where accurate spectroscopic redshifts have been calculated as our gold standard. We will learn how to assess the accuracy of the decision trees predictions and have a look at validation of our model.\
You can download the full NumPy dataset for this activity here: \
https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/ML%20for%20galaxy%20distance%20estimation%20from%20redshifts%20using%20regression/redhift%20dataset/sdss_galaxy_colors.npy?raw=true

We will be using flux magnitudes from the Sloan Digital Sky Survey (SDSS) catalogue to create colour indices. Flux magnitudes are the total flux (or light) received in five frequency bands (u, g, r, i and z). The astronomical colour (or colour index) is the difference between the magnitudes of two filters, i.e. u - g or i - z. This index is one way to characterise the colours of galaxies. For example, if the u-g index is high then the object is brighter in ultra violet frequencies than it is in visible green frequencies. Colour indices act as an approximation for the spectrum of the object and are useful for classifying stars into different types.\
To calculate the redshift of a distant galaxy, the most accurate method is to observe the optical emission lines and measure the shift in wavelength. However, this process can be time consuming and is thus infeasible for large samples. For many galaxies we simply don't have spectroscopic observations.
Instead, we can calculate the redshift by measuring the flux using a number of different filters and comparing this to models of what we expect galaxies to look like at different redshifts. In this activity, we will use machine learning to obtain photometric redshifts for a large sample of galaxies. We will use the colour indices (u-g, g-i, r-i and i-z) as our input and a subset of sources with spectroscopic redshifts as the training dataset.

Here is our predictions: \
https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/ML%20for%20galaxy%20distance%20estimation%20from%20redshifts%20using%20regression/DecisionTreeRegressor.py \
Validating our model using median-difference error: \
https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/ML%20for%20galaxy%20distance%20estimation%20from%20redshifts%20using%20regression/dtr%20Validation.py \
Colour-Colour-Redshift scatter plot:\
https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/ML%20for%20galaxy%20distance%20estimation%20from%20redshifts%20using%20regression/color-color_redshift_plot.py

## Activity 4: Galaxy Classification
Some useful links: \
http://skyserver.sdss.org/dr7/en/help/docs/algorithm.asp \
http://spiff.rit.edu/classes/phys443/lectures/gal_1/petro/petro.html \
In this activity, we will be using machine learning to classify galaxies into three types (ellipticals, spirals or galactic mergers) based on their observed properties. For our machine learning experiments, we are using the crowd-classified classes from Galaxy Zoo as the training data for our automatic decision tree classifier. We'll start by looking at how classification differs from regression. We will then implement some of the new features and parameters that we will use to reduce the dimensionality of the problem. We will also show you how to measure accuracy for classification problems, before extending our classifier to use random forests. \
Here's the dataset: \
https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/ML%20for%20identifying%20galaxy-type%20using%20classification/galaxy-type%20dataset/galaxy_catalogue.npy?raw=true \
In classification, the predictions are from a fixed set of classes, whereas in regression the prediction typically corresponds to a continuum of possible values. In regression, we measure accuracy by looking at the size of the differences between the predicted values and the actual values. In contrast, in classification problems a prediction can either be correct or incorrect. This makes measuring the accuracy of our model a lot simpler.

The features that we will be using to do our galaxy classification are colour index, adaptive moments, eccentricities and concentrations. These features are provided as part of the SDSS catalogue.\
-Colour indices are the same colours (u-g, g-r, r-i, and i-z) we used for regression. Studies of galaxy evolution tell us that spiral galaxies have younger star populations and therefore are 'bluer' (brighter at lower wavelengths). Elliptical galaxies have an older star population and are brighter at higher wavelengths ('redder').\
-Eccentricity approximates the shape of the galaxy by fitting an ellipse to its profile. Eccentricity is the ratio of the two axis (semi-major and semi-minor). The De Vaucouleurs model was used to attain these two axis. To simplify our experiments, we will use the median eccentricity across the 5 filters.\
-Adaptive moments also describe the shape of a galaxy. They are used in image analysis to detect similar objects at different sizes and orientations. We use the fourth moment here for each band.\
-Concentration is similar to the luminosity profile of the galaxy, which measures what proportion of a galaxy's total light is emitted within what radius. A simplified way to represent this is to take the ratio of the radii containing 50% and 90% of the Petrosian flux. The Petrosian method allows us to compare the radial profiles of galaxies at different distances.\
For these experiments, we will define concentration as petro(R50)/petro(R90) .

Training a Decision-Tree Classifier:\
https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/ML%20for%20identifying%20galaxy-type%20using%20classification/DecisionTreeClassifier.py \
Computing accuracy i.e. fraction of predictions that are correct:\
https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/ML%20for%20identifying%20galaxy-type%20using%20classification/accuracy_and_confusion_matrix.py 

So far we have used a single decision tree model. However, we can improve the accuracy of our classification by using a collection (or ensemble) of trees as known as a random forest. A random forest is a collection of decision trees that have each been independently trained using different subsets of the training data and/or different combinations of features in those subsets. When making a prediction, every tree in the forest gives its own prediction and the most common classification is taken as the overall forest prediction (in regression the mean prediction is used).

Random forests help to mitigate overfitting in decision trees.\
-Training data is spread across decision trees. The subsets are created by taking random samples with replacement. This means that a given data point can be used in several subsets. (This is different from the subsets used in cross validation where each data point belongs to one subset).\
-Individual trees are trained with different subsets of features. So in our current problem, one tree might be trained using eccentricity and another using concentration and the 4th adaptive moment. By using different combinations of input features you create expert trees that are can better identify classes by a given feature.\
The sklearn random forest only uses the first form of sampling.

Your task here is to complete the rf_predict_actual function. It returns the predicted and actual classes for our galaxies using a random forest 10-fold with cross validation:\
https://github.com/jaiisrani/Data-driven-Astronomy/blob/main/ML%20for%20identifying%20galaxy-type%20using%20classification/RandomForestClassifier.py

## Activity 5: SQL
This activity is about handling databases and learning basic SQL commands.\
This has umpteen applications, one of that I have demonstrated being exoplanet-classification.\
https://github.com/jaiisrani/Data-driven-Astronomy/tree/main/SQL












