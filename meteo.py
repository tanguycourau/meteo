# -*-coding:utf-8 -*-

from glob import glob
import cfgrib
import subprocess
import meteofetch


## Attention les fichiers ECMWF sont trop gros intérêt à travailler sur la requete pour être sélectif
from meteofetch import Ifs as source # ECMWF 
typefic='oper'

# grib_ls -p shortName 20261031000000-0h-oper-fc.grib2 | grep -E '10u|10v|tp|prmsl|cape'

# from meteofetch import Arome0025 as source
# typefic = 'arome'

# from meteofetch import Arpege025 as source
# typefic = 'arpege'

#variables :
# 10u, 10v, si10 = composantes du vent à 10 m, vent à 10m
# gust = intensité des rafales
# prmsl = pression au niveau de la mer
# 2t, tp = temperature à 2 m et précipitations totales
# CAPE : orage dans le paquet SP2

##datasets=source.get_latest_forecast(paquet='SP1', variables=variables)
# source.get_latest_forecast(paquet='SP1', path=typefic)
# source.get_latest_forecast(paquet='SP2', path=typefic)

print(f'fin extraction meteofetch')




fichiers = sorted(glob(f'{typefic}/*.grib2'))
sorted(fichiers, key=lambda stg: int(stg.split('-')[1][:-1]))

subprocess.run(
    ['grib_copy', *fichiers, f'{typefic}-all.grib2'],
    check=True)

subprocess.run(['wgrib2', f'{typefic}-all.grib2',
                '-small_grib', '5.0:7.0',  '42.0:43.5',
                f'{typefic}-toulon.grib2'], check=True)
print(f'{typefic}-toulon.grib2 géneré')

# #### ATENTION si le grib est trop gros xygrib refuse de l'afficher ####
print(f'grib_copy -w shortName=10u/10v/si10/gust/prmsl/2t/tp/CAPE_INS {typefic}-toulon.grib2 {typefic}-toulon-short.grib2')



# datasets = cfgrib.open_datasets(lstfic[0],engine="cfgrib")
# ds = datasets[0]
# print(ds.latitude.min().values)
# print(ds.latitude.max().values)





