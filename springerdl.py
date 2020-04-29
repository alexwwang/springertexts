import urllib.request
import os
import pandas as pd
 
df = pd.read_csv('SearchResults.csv')
 
length = len(df)
print_val = int(0.05*length)
counter = 0
 
for index, row in df.iterrows():
    name = row['Item Title']
    name = name.replace('/',' or ')
    url = row['URL']
   
    first = url.split(r'/')[-2]
    second = url.split(r'/')[-1]
    pdf_url = 'https://link.springer.com/content/pdf/{}%2F{}.pdf'.format(first,second)
    epub_url = 'https://link.springer.com/download/epub/{}%2F{}.epub'.format(first,second)
   
    if os.path.isdir(name)==False:
        os.mkdir(name)
   
    path = name+"/"+name+".pdf"
    print("\nDownloading "+name+"...")
    if os.path.isfile(path)==False:
        urllib.request.urlretrieve(pdf_url,path)
        print("   ...pdf done")
    try:
        path = name+"/"+name+".epub"
        if os.path.isfile(path)==False:
            urllib.request.urlretrieve(epub_url,path)
            print("   ...epub done")
    except:
        print("No epub Available")
       
    counter+=1
    if counter%print_val==0:
        print("Retreived {}/{} ({}%)".format(counter,length,round(100*counter/length,2)))
