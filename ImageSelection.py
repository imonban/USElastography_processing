import pydicom
import pandas as pd
from shutil import copyfile


folder = '/media/Datacenter_storage/US_elasto/Arizona_PNG/'
metadata = pd.read_csv(folder+'metadata.csv')
#mapping = pd.read_csv(folder+'mapping.csv')

metadata_filter = metadata[(metadata['ViewName']=='LIVER SURFACE RT')|(metadata['ViewName']=='LIVER SURFACE LT')]
not_view = set(metadata['AccessionNumber']) - set(metadata_filter['AccessionNumber'])
##If we are missing cases with view name
for i in not_view:
    temp = metadata[metadata['AccessionNumber']==i]
    temp.sort_values(by = ['file'], axis=0, ascending=True, inplace=True)
    metadata_filter = metadata_filter.append(temp.iloc[-2:])
    
    
metadata_filter.to_csv(folder+'metadata_filter.csv')
    
    