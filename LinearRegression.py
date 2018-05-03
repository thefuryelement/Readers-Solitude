

class statistics():

    def mean(self, values):        
        return (sum(values))/float(len(values))

    def variance(self, mean, values):
        return sum([(x-mean)**2 for x in values])

    def covariance(self, xmean, xval, ymean, yval):
        return sum([(x-xmean)*(y-ymean) for x,y in zip(xval, yval)])

    def coefficiants(self, covar, xmean, ymean):
        b1 = covar/xvariance
        b0 = ymean - xmean*b1
        return b1, b0


if __name__ == "__main__":
    print("hello" )

    statsobj = statistics()
    dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
    
    xlist = [row[0] for row in dataset]
    ylist = [row[1] for row in dataset]
    
    xmean = statsobj.mean(xlist)
    print("mean = ", xmean)
    
    xvariance = statsobj.variance(xmean, xlist)
    print("Variance = ", xvariance)
    
    ymean = statsobj.mean(ylist)
    print("mean = ", ymean)
    
    yvariance = statsobj.variance(ymean, ylist)
    print("Variance = ", yvariance)
    
    
    covar = statsobj.covariance(xmean, xlist, ymean, ylist)
    print("covariance = ", covar)
    
    print(statsobj.coefficiants(covar, xmean, ymean))