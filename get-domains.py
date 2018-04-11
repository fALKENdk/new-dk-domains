import zipfile
import pandas as pd

def read_zip_file(filepath):
  nrd = zipfile.ZipFile(filepath)
  for domainlist in nrd.infolist():
    df = pd.read_csv(nrd.open(domainlist), names=['domain'])
    print(df[df['domain'].str.endswith('.dk')])

read_zip_file('nrd')