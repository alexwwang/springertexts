from urllib import request
import os
from pathlib import Path
import pandas as pd

df = pd.read_csv('SearchResults.csv')

length = df.shape[0]
print_val = int(0.05*length)
counter = 0

proxies = {'http': 'http://127.0.0.1:1080'}
use_proxies = True

if use_proxies:
    proxy_handle = request.ProxyHandler(proxies)
    opener = request.build_opener(proxy_handle)
    # request.install_opener(opener)

for index, row in df.iterrows():
    name = row['Item Title']
    name = name.replace('/',' or ')
    url = row['URL']

    first = url.split(r'/')[-2]
    second = url.split(r'/')[-1]
    pdf_url = 'https://link.springer.com/content/pdf/{}%2F{}.pdf'.format(first,second)
    epub_url = 'https://link.springer.com/download/epub/{}%2F{}.epub'.format(first,second)

    # if os.path.isdir(name)==False:
    #     os.mkdir(name)
    p = Path('.') / 'springertexts' / name
    if not p.exists():
        p.mkdir(parents=True, exist_ok=True)
    pdf_path = p / f"{name}.pdf"
    # path = name+"/"+name+".pdf"
    print("\nDownloading "+name+"...")
    if not pdf_path.is_file():
    # if os.path.isfile(path)==False:
        request.urlretrieve(pdf_url, pdf_path)
        print("   ...pdf done")
    try:
        # path = name+"/"+name+".epub"
        epub_path = p / f"{name}.epub"
        # if os.path.isfile(path)==False:
        if not epub_path.is_file():
            urllib.request.urlretrieve(epub_url, epub_path)
            print("   ...epub done")
    except:
        print("No epub Available")

    counter += 1
    if counter % print_val == 0:
        print("Retreived {}/{} ({}%)".format(counter, length,
            round(100 * counter / length, 2)))
