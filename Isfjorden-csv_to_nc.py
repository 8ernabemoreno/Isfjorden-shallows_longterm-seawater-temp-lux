# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:19:30 2023

@author: 8erna
"""
import xarray as xr
import pandas as pd
from datetime import datetime as dt
import numpy as np

## Download ('S1s', 'S1d', 'S2s', 'S2d') csv files from FigShare repository "https://doi.org/10.6084/m9.figshare.21881460"
## i'll use S2d.csv as an example, adjust paths as necessary

df = pd.read_csv(r"D:\spyder\logIsfjorden\S2d.csv")
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%dT%H:%M:%S')
np.array(df['Date'])

latitude = sorted(list(set(df['Latitude'])))
longitude = sorted(list(set(df['Longitude'])))
time = sorted(list(set(df['Date'])))

## Create a new data frame by selecting columns. Script lines below are only valuable if the downloaded file has more columns and needs to be trimmed down:
# slct = ['Date','Latitude', 'Longitude', 'Sea water temperature (degC)', 'Light intensity (lux)' ]
# slct_df = df[slct]
# slct_df
# slct_df.to_csv('s1s_.csv', index=False)

## Reshape according to the number of data points (records). In this case i'm using S2d as example, which has 250357 data points
temperature = np.array(df['Sea water temperature (degC)']).reshape(250357,1,1)
light = np.array(df['Light intensity (lux)']).reshape(250357,1,1)
date = np.array(df['Date'])

xrds = xr.Dataset(
    coords = dict(
          longitude = longitude,
          latitude = latitude,
          time = date
          ),
    data_vars = dict(
        sea_water_temperature_at_sea_floor = (["time","latitude","longitude"],temperature),
        light_intensity_at_sea_floor = (["time","latitude","longitude"],light), 
        )
    )

xrds['time'].attrs['standard_name'] = 'time'
xrds['time'].attrs['long_name'] = 'time'
xrds['time'].attrs['comment'] = 'time of sample'
xrds['time'].attrs['coverage_content_type'] = 'coordinate'

xrds = xrds.assign_attrs({
    #'units': 'date time of data point',
    'long_name': 'time',
    'standard_name': 'time',
    'coverage_content_type': 'coordinate'
    })

xrds['latitude'].attrs = {
    'standard_name': 'latitude',
    'long_name': 'decimal latitude in degrees north',
    'units': 'degrees_north',
    'coverage_content_type':'coordinate'
    }

xrds['longitude'].attrs = {
    'standard_name': 'longitude',
    'long_name': 'decimal longitude in degrees east',
    'units': 'degrees_east',
    'coverage_content_type':'coordinate'
    }

xrds['sea_water_temperature_at_sea_floor'].attrs = {
    'standard_name': 'sea_water_temperature_at_sea_floor',
    'long_name': 'Temperature of sea water adjacent to the sea floor',
    'units': 'degC',
    'coverage_content_type':'physicalMeasurement'
    }

xrds['light_intensity_at_sea_floor'].attrs = {
    'standard_name': 'light_intensity_at_sea_floor',
    'long_name': 'Light intensity  adjacent to the sea floor provided in lumen per square metre (lux)',
    'units': 'lux',
    'coverage_content_type':'physicalMeasurement'
    }

## Global attributes need to be imported from .xlsx files. These can be downloaded as "globalAttributes_all.xlsx" (containing s1s, s1d, s2s, s2d in different sheets) from FigShare repository https://doi.org/10.6084/m9.figshare.21881460 
## you will need to save sheets independently for site-depths    
 
global_attributes = pd.read_excel(r'D:\ScientificData\globalAttributes\globalAttributes_s2d.xlsx', index_col = 0)
global_attributes_transposed = global_attributes.transpose()
global_attributes_dict = {}
for col in global_attributes_transposed.columns:
    global_attributes_dict[col] = global_attributes_transposed[col].iloc[0]


xrds.attrs = global_attributes_dict

xrds.attrs['date_created'] = dt.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
xrds.attrs['history']= f'File created at {dt.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")} using xarray in Python'

my_encoding = {
    'time': {
        'dtype': 'int32',
        '_FillValue': None
        },
    'latitude': {
        'dtype': 'float32',
        '_FillValue': None
        },
    'longitude': {
        'dtype': 'float32',
        '_FillValue': None
        },
    'sea_water_temperature_at_sea_floor': {
        'dtype': 'float32',
        '_FillValue': 1e20,
        'zlib': False
        },
    'light_intensity_at_sea_floor': {
        'dtype': 'float32',
        '_FillValue': 1e20,
        'zlib': False
        }
    }

print(xrds)

## Export to NetCDF file, adjust path as necessary
xrds.to_netcdf(r"D:\spyder\logIsfjorden\nc\new\Isfjorden_temp-lux_seafloor_2006-2022_S2_15m-S2d.nc",encoding=my_encoding)