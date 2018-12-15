def sudokutest(s,i,j,z):
    # z is the number
    isiValid = numpy.logical_or((i+1<1),(i+1>9));
    isjValid = numpy.logical_or((j+1<1),(j+1>9));
    iszValid = numpy.logical_or((z<1),(z>9));
    if s.shape!=(9,9):
        raise(Exception("Sudokumatrix not valid"));
    if isiValid:
        raise(Exception("i not valid"));
    if isjValid:
        raise(Exception("j not valid"));
    if iszValid:
        raise(Exception("z not valid"));

    if(s[i,j]!=0):
        return False;

    for ii in range(0,9):
        if(s[ii,j]==z):
            return False;

    for jj in range(0,9):
        if(s[i,jj]==z):
            return False;

    row = int(i/3) * 3;
    col = int(j/3) * 3;
    for ii in range(0,3):
        for jj in range(0,3):
            if(s[ii+row,jj+col]==z):
                return False;

    return True;

def possibleNums(s , i ,j):
    l = [];
    ind = 0;
    for k in range(1,10):
        if sudokutest(s,i,j,k):
            l.insert(ind,k);
            ind+=1;
    return l;

def sudokusolver(S):
    zeroFound = 0;
    for i in range(0,9):
        for j in range(0,9):
            if(S[i,j]==0):
                zeroFound=1;
                break;
        if(zeroFound==1):
            break;
    if(zeroFound==0):
        print("REALLY The end")
        z = numpy.zeros(shape=(9,9))
        for x in range(0,9):
            for y in range(0,9):
                z[x,y] = S[x,y]
        print(z)
        return z


    x = possibleNums(S,i,j);

    for k in range(len(x)):
        S[i,j]=x[k];
        sudokusolver(S);
    S[i,j] = 0;


if __name__ == "__main__":
    import numpy 
    #s = numpy.zeros(shape=(9,9))

    k = numpy.matrix([0,0,0,0,0,9,0,7,8,5,1,0,0,0,0,0,6,9,9,0,8,0,2,5,0,0,0,0,3,2,0,0,0,0,0,0,0,0,9,3,0,0,0,1,0,0,0,0,4,0,0,0,8,0,8,0,0,0,9,0,7,0,0,6,0,1,0,0,0,0,0,0,0,0,0,0,7,0,8,0,1]).reshape(9,9)
    print(k)
    print('*'*80)
    sudokusolver(k)
