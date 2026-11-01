
Bouts de codes pour meteofetch


## Attention les fichiers ECMWF sont trop gros
## from meteofetch import Ifs as source # ECMWF 
## typefic='oper'
## grib_ls -p shortName 20261031000000-0h-oper-fc.grib2 | grep -E '10u|10v|tp|prmsl|cape'
##datasets=source.get_latest_forecast(paquet='SP1', variables=variables)


##sorted(fichiers, key=lambda stg: int(stg.split('-')[1][:-1]))

#print(f'grib_copy -w shortName=10u/10v/si10/gust/prmsl/2t/tp/CAPE_INS {typefic}-toulon.grib2 {typefic}-toulon-short.grib2')

# datasets = cfgrib.open_datasets(lstfic[0],engine="cfgrib")
# ds = datasets[0]
# print(ds.latitude.min().values)
# print(ds.latitude.max().values)


Travail sur les vagues
MFWAM01 MFWAM0025
# from meteofetch import MFWAM01 as source
#typefic = 'mwfam'
