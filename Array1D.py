import ctypes
import numpy as np

class Array1D:
    #Creates an element with 'size'
    def __init__(self,size):
        
        assert size > 0 , 'Invalid Size'
        self._size = size
        #Creates an array using ctypes
        arrayType = ctypes.py_object * size
        self._array = arrayType()
        #Initialize the elements
        self.clear(None)
    
    def __len__(self):
        return self._size
  
    #Gets the contents of the idx item
    def __getitem__(self,idx):
        assert idx >=0 and idx < self._size , 'Index out of Range' #U can also use len(self) instead of self._size,
                                                               #Remember to define __len__ to use such len(self)
        return self._array[idx]

    #Replace items based on idx
    def __setitem__(self,idx,value):
        assert idx >= 0 and idx < self._size , 'Index out of Range'
        self._array[idx] = value

    #Clear the array setting all element to None
    def clear(self,value):
        for i in range(self._size):
            self._array[i] = value

    def __iter__(self):
        return _ArrayIterator(self._array)

    #def __str__(self):
        #print (str(self._array))

class _ArrayIterator:
    
    def __init__(self,theArray):
        self._theArray = theArray
        self._cur = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur < len(self._theArray):
            item = self._theArray[self._cur]
            self._cur += 1
            return item
        else:
            raise StopIteration
        
        
#if __name__== "__main__":
    
    #array = Array(6)
    #array[0] = 1
    #array[1] = 2
    #array[3] = 3
    #array[4] = 5
    
    #for i in array:
        #print(i,end = ' ')