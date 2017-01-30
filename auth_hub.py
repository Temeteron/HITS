# import networkx as nx
import numpy as np

if __name__=='__main__':

    arrayL = [(0, 1, 1),
                   (0, 0, 1),
                   (0, 1, 0)]

    arrayLt = zip(*arrayL)

    a = np.array(arrayL)
    b = np.array(arrayLt)
    c = np.dot(a, b)
    d = np.dot(b, a)

    print 'Hubs matrix: L * Lt'
    print c
    eigenvalues, eigenvectors = np.linalg.eig(c)
    print 'Eigenvector of hubs matrix: '
    print eigenvectors.shape

    print 'Authorities matrix: Lt * L'
    print d
    eigenvalues, eigenvectors = np.linalg.eig(d)
    print 'Eigenvector of authorities matrix: '
    print eigenvectors.shape
