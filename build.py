import yaml
import os, shutil
from framework.cls.code import *

with open('website.yaml', 'r') as file:
    loaded_data = yaml.safe_load(file)

print("Data read from 'data.yaml':")

try:
    shutil.rmtree('site')
except :
    print('directory site bestaat niet')

os.mkdir('site')
print('directory `site/` gemaakt')
os.mkdir('site/weeks/')
print('directory `site/weeks/` gemaakt')

for w in range(1, len(loaded_data['weken'])+1):
    print(f'werken aan week {w}')
    directory = f'site/weeks/week-{w}'
    os.mkdir(directory)

    index_contents = []
    for onderdeel in loaded_data['weken'][f'week{w}']['nav']:
        (page_type, page_content), = onderdeel.items()
        print(f'  werken aan pagina type {page_type}')
        if page_type not in ['reading','practical']:
            print(f'FOUT: onbekend pagina-type {page_type}')
            next
        
        try: 
            page, title, intro = create_page(w, page_type, page_content)
        except ValueError as e:
            print(f'\nFOUT: {e}')
            print(f'markdown-bestand: {page_content}, pagina-type: {page_type}\n')
            next
    
        file = page_content.replace(' ', '-')
        index_contents.append([page_type, file, title, intro])
        with open(f'{directory}/{file}.html', 'w') as f:
            print(f'  wegschrijven van bestand {file}.html')
            f.write(page)

    with open(f'{directory}/index.html', 'w+') as idx:
        print(f'maken van index van week {w}')
        idx.write(create_index(w, index_contents))
        print('index weggeschreven\n')

print('main index maken')
with open('site/index.html', 'w') as f:
    f.write(create_main_index())

print('kopiëren van assets uit het framework')
shutil.copytree('framework/assets/', 'site/assets/')



