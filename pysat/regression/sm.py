# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 20:15:46 2016

@author: rbanderson
"""
import numpy as np
import pysat.spectral.within_range as within_range
from pysat.spectral.meancenter import meancenter
import scipy.optimize as opt
from pysat.regression.regression import regression 
class sm:
    def __init__(self,labels,ycol,ranges,method,ransac=False):
        self.labels=labels
        self.ycol=ycol
        self.method=method 
        self.ranges=ranges
        self.ransac=ransac
        self.outliers=None
        self.inliers=None
    # TODO sm.final(testdata[0]['meta'][el],
    #            blended_test,
    #            color='r',
    #            xcol='Ref Comp Wt. %',
    #            ycol='Predicted Comp Wt. %',
    #            figpath=outpath)

    # TODO rename this function to something better, later on


    #This function does the fitting for each submodel.
    def fit(self,trainsets,figpath=None,**kwargs):
               
        submodels=[]    
        mean_vects=[]

        for i,rangei in enumerate(self.ranges):
            data_tmp=within_range.within_range(trainsets[i],rangei,self.ycol)
            #x=data_tmp.xs(self.labels,axis=1,level=0,drop_level=False)
            x=data_tmp[self.labels]
            y=data_tmp[self.ycol].values
            x_centered,x_mean_vect=meancenter(x) #mean center training data
            kwargs['i']=i
            kwargs['range']=rangei
            reg=regression(self.ycol,self.method,ransac=self.ransac,**kwargs)
            reg.fit(x_centered,y,figpath=figpath)
            submodels.append(reg)
            mean_vects.append(x_mean_vect)
            
            self.submodels=submodels
            self.mean_vects=mean_vects
            
 
    def do_blend(self,predictions,truevals=None):

        #create the array indicating which models to blend for each blend range
        #For three models, this creates an array like: [[0,0],[0,1],[1,1],[1,2],[2,2]]
        #Which indicates that in the first range, just use model 0
        #In the second range, blend models 0 and 1
        #in the third range, use model 1
        #in the fourth range, blend models 1 and 2
        #in the fifth range, use model 2
        
        self.toblend=[]
        for i in range(len(predictions)-1):
            self.toblend.append([i,i])
            if i<len(predictions)-2:
                self.toblend.append([i,i+1])
            
        #If the true compositions are provided, then optimize the ranges over which the results are blended to minimize the RMSEC
        if truevals is not None:
            print('Optimizing blending ranges')
            #get the ranges that are not the reference model (assumed to be the last model)
            ranges_sub=self.ranges[:-1]
            blendranges=np.array(ranges_sub).flatten() #squash them to be a 1d array
            blendranges.sort()  #sort the entries. These will be used by submodels_blend to decide how to combine the predictions
         
            result=opt.minimize(self.get_rmse,blendranges,(predictions,truevals))
            self.blendranges=result.x

            
        #calculate the blended results
        blended=self.submodels_blend(predictions,self.blendranges,overwrite=False,noneg=False)
        return blended
        
    def get_rmse(self,blendranges,predictions,truevals):
        blendranges  #show the blendranges being used for the current calculation
        blended=self.submodels_blend(predictions,blendranges,overwrite=False,noneg=False)
        RMSE=np.sqrt(np.mean((blended-truevals)**2))  #calculate the RMSE
        return RMSE
        
    def submodels_blend(self,predictions,blendranges,overwrite=False,noneg=False):
        blended=np.squeeze(np.zeros_like(predictions[0]))
        
        #format the blending ranges
        blendranges=np.hstack((blendranges,blendranges[1:-1])) #duplicate the middle entries
        blendranges.sort() #re-sort them
        blendranges=np.reshape(blendranges,(len(blendranges)/2,2))  #turn the vector into a 2d array (one pair of values for each submodel)
        
        
        for i in range(len(blendranges)): #loop over each composition range
            for j in range(len(predictions[0])): #loop over each spectrum
                ref_tmp=predictions[-1][j]   #get the reference model predicted value
                #check whether the prediction for the reference spectrum is within the current range            
                inrangecheck=(ref_tmp>blendranges[i][0])&(ref_tmp<blendranges[i][1])
     
                if inrangecheck: 
                    if self.toblend[i][0]==self.toblend[i][1]: #if the results being blended are identical, no blending necessary!
                      
                        blendval=predictions[self.toblend[i][0]][j]
                    else:
                        weight1=1-(ref_tmp-blendranges[i][0])/(blendranges[i][1]-blendranges[i][0]) #define the weight applied to the lower model
                        weight2=(ref_tmp-blendranges[i][0])/(blendranges[i][1]-blendranges[i][0]) #define the weight applied to the higher model
                        blendval=weight1*predictions[self.toblend[i][0]][j]+weight2*predictions[self.toblend[i][1]][j] #calculated the blended value (weighted sum)
                    if overwrite:
                        blended[j]=blendval #If overwrite is true, write the blended result no matter what
                    else:
                        if blended[j]==0:  #If overwrite is false, only write the blended result if there is not already a result there
                            blended[j]=blendval                
        #Set any negative results to zero if noneg is true
        if np.min(blended)<0 and noneg==True:
            blended[blended<0]=0
    
        return blended
    
    def predict(self,x):
        #x is a list of data frames to feed into each submodel. 
        #This allows different normalizations to be used with each submodel
        predictions=[]
        for i,k in enumerate(self.submodels):
            try:
                #xtemp=x[i].xs('wvl',axis=1,level=0,drop_level=False)
                xtemp=x[i][self.labels]
            except:
                pass
            xtemp,mean_vect=meancenter(xtemp,previous_mean=self.mean_vects[i])
            
            if self.method is 'GP':
                 #for gaussian processes, the input data dimensionality needs to be reduced
                #Default to using ICA to do this
                xtemp=self.do_ica.transform(xtemp)
            else:
                pass
            predictions.append(k.predict(xtemp))
        return predictions