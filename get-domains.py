import datetime
import os
import pandas as pd
import pytablewriter
import requests
import zipfile as zf

yesterday = str(datetime.date.fromordinal(datetime.date.today().toordinal()-1))
filename = yesterday
zipfile = ''.join([filename, ".zip"])
zipurl = ''.join(["https://whoisds.com/whois-database/newly-registered-domains/", zipfile, "/nrd"])
mdfile = ''.join([filename, ".md"])
mdpath = ''.join(["./domains/", mdfile])

# Download zipfile
file = requests.get(zipurl)
with open(zipfile, 'wb') as f:
  f.write(file.content)

# Unzip
domainfile = zf.ZipFile(zipfile)
# Check for dk domains in the files
for domainlist in domainfile.infolist():
  df = pd.read_csv(domainfile.open(domainlist), names=['domain'])
  danish = df[df['domain'].str.endswith('.dk')]
  
  # Create md file
  md_headers = ['domain']
  writer = pytablewriter.MarkdownTableWriter()
  writer.header_list = list(md_headers)
  writer.value_matrix = danish.values.tolist()
  with open(mdpath, "w") as f:
    writer.stream = f
    writer.write_table()

# Delete zipfile
os.remove(zipfile)
