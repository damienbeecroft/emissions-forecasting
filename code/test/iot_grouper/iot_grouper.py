from pandas import read_csv
from numpy import arange
import os 
path_to_data = '/mmfs1/gscratch/amath/dob1998/emissions_forecasting/data/IOT_pxp/'
path_to_save = '/mmfs1/gscratch/amath/dob1998/emissions_forecasting/data/grouped_data/'

years = arange(1995,2023)

# Create the index
unit = read_csv(path_to_data + 'IOT_1995_pxp/unit.txt',index_col = [0,1], sep='\t')
idx = []
for i in arange(200):
    idx.append(unit.index[i][1])

for year in years:
    # Create the directory if it does not already exist
    if not os.path.exists(path_to_save + 'IOT_' + str(year) + '_pxp/'):
	    os.makedirs(path_to_save + 'IOT_' + str(year) + '_pxp/')

    # # Z
    # Z = read_csv(path_to_data + 'IOT_' + str(year) + '_pxp/Z.txt', header = [0,1], index_col = [0,1], sep='\t')
    # grouped_Z = Z.groupby(level = 'sector', axis = 1).sum()
    # grouped_Z = grouped_Z.groupby(level = 'sector', axis = 0).sum()
    # grouped_Z = grouped_Z.reindex(index = idx, columns = idx)

    # # x
    # x = read_csv(path_to_data + 'IOT_' + str(year) + '_pxp/x.txt', index_col = [0,1], sep='\t')
    # grouped_x = x.groupby(level = 'sector').sum()
    # grouped_x = grouped_x.reindex(index = idx)

    # # Y
    # Y = read_csv(path_to_data + 'IOT_' + str(year) + '_pxp/Y.txt', header = [0,1], index_col = [0,1], sep='\t')
    # grouped_Y = Y.groupby(level = 'category', axis = 1).sum()
    # grouped_Y = grouped_Y.groupby(level = 'sector', axis = 0).sum()
    # grouped_Y = grouped_Y.reindex(index = idx)

    # # F
    # F = read_csv(path_to_data + 'IOT_' + str(year) + '_pxp/satellite/F.txt', header = [0,1], index_col = 0, sep='\t')
    # grouped_F = F.groupby(level = 'sector', axis = 1).sum()
    # grouped_F = grouped_F.reindex(columns = idx)

    # # F_Y
    # F_Y = read_csv(path_to_data + 'IOT_' + str(year) + '_pxp/satellite/F_Y.txt', header = [0,1], index_col = 0, sep='\t')
    # grouped_F_Y = F_Y.groupby(level = 'category', axis = 1).sum()

    # # D_cba
    # D_cba = read_csv(path_to_data + 'IOT_' + str(year) + '_pxp/satellite/D_cba.txt', header = [0,1], index_col = 0, sep='\t')
    # grouped_D_cba = D_cba.groupby(level = 'sector', axis = 1).sum()
    # grouped_D_cba = grouped_D_cba.reindex(columns = idx)

    # # D_pba
    # D_pba = read_csv(path_to_data + 'IOT_' + str(year) + '_pxp/satellite/D_pba.txt', header = [0,1], index_col = 0, sep='\t')
    # grouped_D_pba = D_pba.groupby(level = 'sector', axis = 1).sum()
    # grouped_D_pba = grouped_D_pba.reindex(columns = idx)

    # # MAKE SURE THESE ARE CORRECT BEFORE RUNNING THEM!!!!
    # grouped_Z.to_csv(path_to_save + 'IOT_' + str(year) + '_pxp/' + 'Z.csv')
    # grouped_x.to_csv(path_to_save + 'IOT_' + str(year) + '_pxp/' + 'x.csv')
    # grouped_Y.to_csv(path_to_save + 'IOT_' + str(year) + '_pxp/' + 'Y.csv')
    # grouped_F.to_csv(path_to_save + 'IOT_' + str(year) + '_pxp/' + 'F.csv')
    # grouped_F_Y.to_csv(path_to_save + 'IOT_' + str(year) + '_pxp/' + 'F_Y.csv')
    # grouped_D_cba.to_csv(path_to_save + 'IOT_' + str(year) + '_pxp/' + 'D_cba.csv')
    # grouped_D_pba.to_csv(path_to_save + 'IOT_' + str(year) + '_pxp/' + 'D_pba.csv')
