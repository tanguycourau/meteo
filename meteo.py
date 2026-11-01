# -*-coding:utf-8 -*-

from glob import glob
import cfgrib
import subprocess
import meteofetch


# variables des paquets SP1 et SP2 :
# 10u, 10v, si10 = composantes du vent à 10 m, vent à 10m
# gust = intensité des rafales
# prmsl = pression au niveau de la mer
# 2t, tp = temperature à 2 m et précipitations totales
# CAPE_INS : orage dans le paquet SP2


from meteofetch import Arome0025 as source
typefic = 'arome'

from meteofetch import Arpege025 as source
typefic = 'arpege'

# source.get_latest_forecast(paquet='SP1', path=typefic)
# source.get_latest_forecast(paquet='SP2', path=typefic)

fichiers = sorted(glob(f'{typefic}/*.grib2'))


subprocess.run(
    ['grib_copy', *fichiers, f'{typefic}-all.grib2'],
    check=True)

subprocess.run(['wgrib2', f'{typefic}-all.grib2',
                '-match', 'UGRD|VGRD|PRMSL|TMP|TP|GUST|CAPE',
                '-small_grib', '5.0:7.0',  '42.0:43.5',
                f'{typefic}-toulon.grib2'], check=True)
print(f'{typefic}-toulon.grib2 géneré')

#### ATENTION si le grib est trop gros xygrib refuse de l'afficher ####

