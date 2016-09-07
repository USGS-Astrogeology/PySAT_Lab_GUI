# -*- coding: utf-8 -*-
"""
Created on Tue May 10 12:09:29 2016

@author: rbanderson
"""
import pandas as pd
import numpy as np
from pysat.spectral.spectral_data import spectral_data
from pysat.spectral.within_range import within_range
from pysat.spectral.meancenter import meancenter
from pysat.regression.sm import sm
from sklearn.decomposition import PCA, FastICA
from sklearn import linear_model
from sklearn.cross_decomposition.pls_ import PLSRegression
from pysat.plotting import plots
import time
from pysat.regression.cv import cv

import matplotlib.pyplot as plot
import warnings

warnings.filterwarnings('ignore')

print('Read training database')
db=r"C:\Users\rbanderson\Documents\Projects\LIBS PDART\Sample_Data\full_db_mars_corrected_dopedTiO2_pandas_format.csv"
data=pd.read_csv(db,header=[0,1])

data=spectral_data(data)


print('read unknown data from the combined csv file (much faster)')
unknowndatacsv=r"C:\Users\rbanderson\Documents\Projects\MSL\ChemCam\Lab Data\lab_data_averages_pandas_format.csv"
unknown_data=pd.read_csv(unknowndatacsv,header=[0,1])
unknown_data=spectral_data(unknown_data)

print('Interpolate unknown data onto the same exact wavelengths as the training data')
unknown_data.interp(data.df['wvl'].columns)

print('Mask out unwanted portions of the data')
maskfile=r"C:\Users\rbanderson\Documents\Projects\LIBS PDART\Input\mask_minors_noise.csv"
data.mask(maskfile)
unknown_data.mask(maskfile)

print('Normalize spectra by specifying the wavelength ranges over which to normalize')
ranges3=[(0,350),(350,470),(470,1000)] #this is equivalent to "norm3"

print('Norm3 data')
data3=data
data3.norm(ranges3)
unknown_data3=unknown_data
unknown_data3.norm(ranges3)


print('set up for cross validation')
el='SiO2'
nfolds=6 #number of folds to divide data into to extract an overall test set
testfold=4 #which fold to use as the overall test set

nc=10  #max number of components
outpath=r'C:\Users\rbanderson\Documents\Projects\LIBS PDART\Output'

print('remove a test set to be completely excluded from CV and used to assess the final model')
data3.stratified_folds(nfolds=nfolds,sortby=('meta',el))
data3_train=data3.rows_match(('meta','Folds'),[testfold],invert=True)
data3_test=data3.rows_match(('meta','Folds'),[testfold])
 

figfile='PLS_CV_0-100_norm3.png'
params={'n_components':list(range(1,nc+1)),'scale':[False]}
rmsec,rmsecv,rmsecv_folds,paramgrid=cv(data3_train.df,params,xcols='wvl',ycol=('meta',el),method='PLS',ransac=False)

plotx=[list(range(1,nc+1)),list(range(1,nc+1))]
ploty=[rmsecv,rmsec]
alphas=[1.0,1.0]
colors=['r','g']
lbls=['RMSECV','RMSEC']
#for i in list(range(nfolds-1)):
#    plotx.append(list(range(1,nc+1)))
#    ploty.append(rmsecv_folds[i])
#    alphas.append(0.25)
#    lbls.append(None)
#    colors.append('r')
#

plots.lineplot(plotx,ploty,lbls=lbls,figpath=outpath,figname=figfile,colors=colors,alphas=alphas,xtitle='# of Components',ytitle='RMSE (wt.%)')

print(foo)
    




