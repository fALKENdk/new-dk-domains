import zipfile
import pandas as pd

def read_zip_file(filepath):
  nrd = zipfile.ZipFile(filepath)
  df = pd.read_csv(nrd.open('2018-04-10.txt'), names=['domain'])
  print(df[df['domain'].str.endswith(".dk")])
 
read_zip_file("nrd")