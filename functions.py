# non time series
def scale(data):
    numerator = data.subtract(data.min(axis = 1), axis = 0) # x - min(x)
    denominator = data.max(axis = 1).subtract(data.min(axis = 1), axis = 0) # max(x) - min(x)
    result = numerator.div(denominator, axis = 0)
    return result