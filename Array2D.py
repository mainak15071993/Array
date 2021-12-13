from Array1D import Array1D

class Array2D:
    
    def __init__(self,nrows,ncols):
        assert nrows > 0 and ncols > 0 , 'Enter a Valid Number'
        self._nrows = Array1D(nrows)
        for i in range(ncols):
            self._nrows[i] = Array1D(nrows)
            
    def numrows(self):
        return len(self._nrows)
    
    def numcols(self):
        return len(self._nrows[0])
    
    def __getitem__(self, idxTuple):
        assert len(idxTuple) == 2, 'Tuple out of Range'
        row = idxTuple[0]
        col = idxTuple[1]
        assert row >= 0 and row < int(self.numrows()) and col > 0 and col < int(self.numcols()), 'Rows and Columns out of Range'
        the1dArray = self._nrows[row]
        return the1dArray[col]
    
    def __setitem__(self,idxTuple,value):
        assert len(idxTuple) == 2, 'Tuple out of Range'
        row = idxTuple[0]
        col = idxTuple[1]
        assert row >= 0 and row < int(self.numrows) and col > 0 and col < int(self.numcols), 'Rows and Columns out of Range'
        the1DArray = self._rows[row]
        the1DArray[col] = value
        
    def clear(self,value):
        for r in range(self.numrows()):
            self._nrows[r].clear(value)
            

#if __name__ == '__main__':
    
    #array2d = Array2D(2,2)
    #array2d.clear(60)
    #print(array2d[1,1])
            
    