import zipfile as zf
import pandas as pd
import pytablewriter as ptw

def zipToMarkdown(filepath):
  nrd = zf.ZipFile(filepath)
  for domainlist in nrd.infolist():
    df = pd.read_csv(nrd.open(domainlist), names=['domain'])
    danish = df[df['domain'].str.endswith('.dk')]
    
    md_headers = ['domain']
    writer = ptw.MarkdownTableWriter()
    writer.header_list = list(md_headers)
    writer.value_matrix = danish.values.tolist()

    with open("domain-list.md", "w") as f:
      writer.stream = f
      writer.write_table()

zipToMarkdown('nrd')
