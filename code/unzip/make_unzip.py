from numpy import arange
datatype = 'IOT_pxp'
path_to_folder = '/mmfs1/gscratch/amath/dob1998/emissions_forecasting/code/unzip/' # path to this file
path_to_zips = '/mmfs1/gscratch/amath/dob1998/emissions_forecasting/data/zip/' + datatype + '/' # path to zipped files
path_to_save = '/mmfs1/gscratch/amath/dob1998/emissions_forecasting/data/' + datatype + '/' # path to saved files

f = open(path_to_folder + 'unzip.sh','a')

v = arange(1995,2023)
for el in v:
    # f.write('unzip ' + path_to_zips + 'IOT_' + str(el) + '_ixi.zip -d ' + path_to_save + '\n') 
    f.write('unzip ' + path_to_zips + 'IOT_' + str(el) + '_pxp.zip -d ' + path_to_save + '\n') 
    # f.write('unzip ' + path_to_zips + 'MRSUT_' + str(el) + '.zip -d ' + path_to_save + '\n')

f.close()

exit()