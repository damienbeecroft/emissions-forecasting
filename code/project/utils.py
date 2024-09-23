from numpy import empty, tile, repeat, array
import numpy as np
import pandas as pd

def create_aggregator(df, region_names = None, sector_names = None, region_indices = None, sector_indices = None):
    '''
    Creates index vectors to aggregate products/industries and regions in the MRIO tables

    Args:
        df                  : The dataframe that is to be aggregated
        region_names        : Names of the new regions that will be used in the aggregation
        sector_names        : Names of the new sectors that will be used in the aggregation
        region_indices      : A list that specifies in which indices to place the new region names
        sector_indices      : A list that specifies in which indices to place the new sector names

    Returns:
        Multi-index array of length n*m with aggregation names placed in the correct locations
    '''

    # create the new multi-indices
    region_agg = empty(df.index.levels[0].size, dtype = '<U5')
    sector_agg = empty(df.index.levels[1].size, dtype = '<U5')

    if not((region_names == None) and (region_names == None)):
        for element in zip(region_names, region_indices):
            region_agg[element[1]] = element[0]
    else:
        region_agg = df.index.levels[0]

    if not((sector_names == None) and (sector_names == None)):
        for element in zip(sector_names, sector_indices):
            sector_agg[element[1]] = element[0]
    else:
        sector_agg = df.index.levels[1]

    # reset the indices in the dataframe
    multi_index = pd.MultiIndex.from_product([region_agg, sector_agg], names= df.index.names)
    df.columns = multi_index
    df.index = multi_index

    # aggregate the rows and columns based on the new names
    df = df.groupby(level = df.index.names, axis = 1).sum()
    df = df.groupby(level = df.index.names, axis = 0).sum()
    return df






##### FUNCTION TESTING #############################################################################
# if __name__ == "__main__":

#     # Adjusting the DataFrame to be 9x9 with 3 industries and 3 regions

#     # Define 3 region and 3 industry names
#     regions = ['North', 'South', 'West']
#     industries = ['A','B','C','D','E']

#     # Create a MultiIndex for rows and columns with the 3 regions and 3 industries
#     row_index = pd.MultiIndex.from_product([regions, industries], names=['Region', 'Industry'])
#     column_index = pd.MultiIndex.from_product([regions, industries], names=['Region', 'Industry'])

#     # Generate random positive integer data for a 9x9 table
#     data = np.random.randint(1, 100, size=(15,15))

#     # Create the DataFrame
#     df_9x9_corrected = pd.DataFrame(data, index=row_index, columns=column_index)

#     sector_names = ['ABC', 'DE']
#     sector_indices = [[0,1,2],[3,4]]
#     # df2 = create_aggregator(df_9x9_corrected, region_names = region_names, region_indices = region_indices)
#     df2 = create_aggregator(df_9x9_corrected, sector_names = sector_names, sector_indices = sector_indices)

#     print(df2)
