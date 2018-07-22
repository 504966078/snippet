# density
Comparing observed and Gaussian distributions

The input csv file contains a raw observation data in the following format: Value \t Quantity

The default algorithm disperses the mass of the empirical distribution function over a regular grid of at least 512 points and then uses the fast Fourier transform to convolve this approximation with a discretized version of the kernel and then uses linear approximation to evaluate the density at the specified points.

The output file contains graphs of the observed and corresponding Gaussian distributions.

How to use: 
* Install R
* R --no-save  < ./main.R 