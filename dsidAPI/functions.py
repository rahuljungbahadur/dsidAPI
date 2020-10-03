import numpy as np


## Mean Estimate 

def labelArrayExtend(label, times):

    labelArray = []
    i = 0
    while i < times:
        labelArray.append(label **i) 
        i = i+1

    return labelArray

def parameterEstimate(params : list, label : float):

    meanParamsList = np.array(params)
    ingredLabelList = np.array(labelArrayExtend(label, times=len(params)))

    return np.dot(np.transpose(meanParamsList), ingredLabelList)

## Standard Error of mean

def stdErrorEstimate(params : list, label : float):

    meanParamsList = np.array(params)

    ingredLabelList = np.array(labelArrayExtend(label, times=len(params)))

    return np.dot(np.transpose(meanParamsList), ingredLabelList)



    