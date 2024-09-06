from numpy import empty, tile, repeat, array

def create_aggregator(names: array, indices: list, n: int, m: int, first_index = True) -> array:
    '''
    Creates index vectors to aggregate products/industries and regions in the MRIO tables

    Args:
        names (array):      Names of the aggregators
        indices (list):     Positions of the aggregators
        n (int):            Length of first multi-index (products/industries by default)
        m (int):            Length of second multi-index (regions by default)
        first_index (bool): True if the names in <names> correspond to the first multi-index
                            and false if the names in <names> correspond to the second multi-index

    Returns:
        Multi-index array of length n*m with aggregation names placed in the correct locations
    '''

    assert len(names) == len(indices)

    agg = empty(n, dtype = '<U5')

    for element in zip(names,indices):
        agg[element[1]] = element[0]

    if first_index:
        agg = tile(agg, m)
    else:
        agg = repeat(agg, m)
    return agg





# if __name__ == "__main__":
#     v1 = array(['A', 'B', 'C'])
#     v2 = [1, 2, [0,3,4]]
#     n = 5
#     m = 3
#     print(create_aggregator(v1,v2,n,m,first_index=False))