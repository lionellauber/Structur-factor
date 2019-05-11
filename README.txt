This very short code is to calculate rodlike structure factor to fit with light scattering experiment.
It is purposely very simple to be easily adjustable with any code and/or to be used by fairly experienced coders.

You can change the radius (R) and the lenght (L) of the rod within the code (line ~50), so as the limits of the wave vectors (q0 and qn).
The actual example is for light scattering using D:10nm and L:700nm. It will show a graph and save data in autosave.csv ("." as decimal and ";" as separator).

Package needed to run SqRodOnly.py are matplotlib, numpy, csv and scipy.

The equation was taken from "Form and Structure Factors:Modeling and Interactions" of Jan Skov Pedersen, University of Aarhus, Denmark (pdf online). Thanks to him.

Enjoy and comment if you find issue/mistake or want to improve it.