# -*-coding:utf-8 -*-
from meteofetch import Arome0025 as source
from glob import glob
import cfgrib
import subprocess


#Variables de vent à 10 m
variables = [
    "UGRD_10m",  # composante U
    "VGRD_10m"   # composante V
]

source.get_latest_forecast(paquet='SP1', path='.')
#datasets=source.get_latest_forecast(paquet='SP1', variables=variables)


fichiers = sorted(glob("arome*.grib2"))

subprocess.run(
    ["grib_copy", *fichiers, "arome-all.grib2"],
    check=True)

subprocess.run(['wgrib2', 'arome-all.grib2',
                '-small_grib', '5.0:6.2',  '41.95:43.28',
                'toulon.grib2'], check=True)

# #### ATENTION si le grib est trop gros xygrib refuse de l'afficher ####
# lstfic = sorted(glob('arome*.grib2'))
# print('grib_copy -w shortName=10u/10v/si10/prmsl/2t/tp '+lstfic[0]+' arome.grib2')
# print('wgrib2 arome.grib2 -small_grib 5.0:6.2 41.95:43.28  toulon.grib2')


# datasets = cfgrib.open_datasets(lstfic[0],engine="cfgrib")
# ds = datasets[0]
# print(ds.latitude.min().values)
# print(ds.latitude.max().values)





