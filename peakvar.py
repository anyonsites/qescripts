#! /usr/bin/env python3

import sys
import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
from spectrum import Spectrum

class PeakVar:
    '''
    Peak variations manipulation:
    * Load data
    * Gaussian fit
    * Interpolation
    '''

    def __init__(self, inpfname, taglist):
        self.inpfname = inpfname
        self.taglist = taglist
        self.spectra = {}
        self.loaddata()

    def loaddata(self):
        '''
        Load all data from file:
        * prepared as CSV format
        * comment the tag row with '#'

        build the db with:
        self.spectra = { 
                         taglist[0] : Spectrum instance for taglist[0],
                         taglist[1] : Spectrum instance for taglist[1],
                         ...
                       }

        '''
        cols = np.genfromtxt(self.inpfname, delimiter=",", unpack=True) 
        if cols.shape[0] != 2*len(self.taglist):
            print("ERROR! mismatch of taglist and column!")
            sys.exit()
        for i in range(len(self.taglist)):
            colxy = cols[2*i:2*i+2]
            # delete rows containing 'NaN'
            colxy = colxy.transpose()
            colxy = colxy[~np.isnan(colxy).any(axis=1)]
            colxy = colxy.transpose()
            # add i-th spectra instance to self.spectra{}
            self.spectra[self.taglist[i]] = Spectrum(colxy[0], colxy[1])

    def fitgauss(self, gaus_guess):
        for key in gaus_guess:
            self.spectra[key].gausfit(gaus_guess[key])






