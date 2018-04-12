import zipfile as zf
import pandas as pd
import pytablewriter
import datetime
import requests

yesterday = str(datetime.date.fromordinal(datetime.date.today().toordinal()-1))
filename = yesterday
zipfile = ''.join([filename, ".zip"])
zipurl = ''.join(["https://whoisds.com/whois-database/newly-registered-domains/", zipfile, "/nrd"])
mdfile = ''.join([filename, ".md"])
mdpath = ''.join(["./domains/", mdfile])

file = requests.get(zipurl)
with open(zipfile, 'wb') as f:
  f.write(file.content)

domain_file = zf.ZipFile(zipfile)
for domainlist in domain_file.infolist():
  df = pd.read_csv(domain_file.open(domainlist), names=['domain'])
  danish = df[df['domain'].str.endswith('.dk')]
  
  md_headers = ['domain']
  writer = pytablewriter.MarkdownTableWriter()
  writer.header_list = list(md_headers)
  writer.value_matrix = danish.values.tolist()

  with open(mdpath, "w") as f:
    writer.stream = f
    writer.write_table()
