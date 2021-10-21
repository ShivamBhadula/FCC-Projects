import numpy as np

def calculate(list):    
    if(len(list)!=9):
        raise ValueError("List must contain nine numbers.")
    calculations = dict()
    tempList = []
    reshapedList = np.reshape(list, (3,3)).tolist()
    functions = {'mean': np.mean, 'variance': np.var, 'standard deviation': np.std,
                 'max': np.max, 'min': np.min, 'sum': np.sum}
    for key in functions:
        tempList.append(functions[key](reshapedList, axis = 0).tolist()) 
        tempList.append(functions[key](reshapedList, axis = 1).tolist())
        tempList.append(functions[key](list).tolist())
        calculations[key] = tempList
        tempList = []

    return calculations