from numpy import arange
path_to_folder = '/mmfs1/gscratch/amath/dob1998/emissions_forecasting/code/unzip/'
path_to_zips = '/mmfs1/gscratch/amath/dob1998/emissions_forecasting/data/IOT_ixi/'

f = open(path_to_folder + 'unzip','a')

v = arange(1996,2023)
for el in v:
    f.write('unzip ' + path_to_zips + 'IOT_' + str(el) + '_ixi.zip\n') # unzips to active folder

f.close()
