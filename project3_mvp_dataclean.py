#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 17:57:12 2019

@author: opasina
"""

import pandas as pd
import numpy as np

#import pycountry

dic = pd.read_csv("DemocracyIndexCountries.csv")

gdp = pd.read_csv("GDP_GROWTH_AlmostClean.csv")

#gdpyeardropped = gdp.drop(columns=['2000', '2001','2002','2003','2004','2005'])

gdpmelted = pd.melt(gdp, id_vars=['Country Name','Country Code'], value_vars=['2006', '2007', '2008', '2009', '2010',
       '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'])

gdpmelted.rename(columns={"value": "gdp"},inplace=True)
gdpmelted.rename(columns={"variable": "year"},inplace=True)
dic.rename(columns={"time":"year"},inplace=True)

gdpmelted.rename(columns={"Country Name": "cnty","Country Code":"geo"},inplace=True)

gdpmelted['cnty'] = gdpmelted['cnty'].str.lower()




gdpmelted["year"] = gdpmelted["year"].astype(np.int64)

gdpmelted['geo'] = gdpmelted['geo'].str.lower()

#gdpmelted.to_csv("CountryGrowth20062018.csv")


# merge on country and year

dic_gdp = pd.merge(dic, gdpmelted,  how='inner', left_on=['geo','year'], right_on = ['geo','year'])

dic_gdp = dic_gdp.drop(columns=['cnty'])

dic_gdp["name"] = dic_gdp.name.str.lower()


total_columns = [x.lower().replace(" (eiu)","").replace(" ","_") for x in dic_gdp.columns.values]

dic_gdp.columns = total_columns

dic_gdp.to_csv("DemocracyIndexGDP20062018.csv")


#dic_g

#diccount = dic['name'].drop_duplicates()

#pycountry.countries.lookup('congo dem rep')