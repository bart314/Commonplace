import markdown
from bs4 import BeautifulSoup
from . import loaded_data

def create_index(week, index_contents):
    with open('framework/templates/week/index.tpl.html', 'r') as f:
        page = f.read()
    index_tiles = ''.join([create_index_tile(x) for x in index_contents])
    page = page.replace('{{index_tiles}}', index_tiles)
    
    with open(f'src/week-{week}/index.md', 'r') as md:
        html = markdown.markdown(md.read())
    
    page = page.replace('{{weeknummer}}', str(week))
    page = page.replace('{{titel}}', loaded_data['weken'][f'week{week}']['titel'])
    page = page.replace('{{content}}', html)
    return page

def create_index_tile(contents, in_week=True):
    page_type, page_link, page_title, page_intro = contents
    assets_link = '../../' if in_week else ''
    with open('framework/templates/tile.tpl.html', 'r') as f:
        tile = f.read()

    # Dit zou toch makkelijker moeten kunnen met een loopje en
    # string-interpolation, maar ik gebruik accolades voor de 
    # templates en ik heb nu geen zin om uit te zoeken hoe ik
    # dat kan escapen. Dus maar even zo.
    tile = tile.replace('{{assets_link}}', assets_link)
    tile = tile.replace('{{page_link}}', page_link)
    tile = tile.replace('{{page_type}}', page_type)
    tile = tile.replace('{{page_title}}', page_title)
    tile = tile.replace('{{page_intro}}', page_intro)
    return tile

def create_main_index():
    with open('framework/templates/index.tpl.html', 'r') as f:
        template = f.read()
    with open('src/index.md') as md:
        html = markdown.markdown(md.read())
    
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find("h1", recursive=False)
    intro = title.find_next_sibling("p") if title else None

    items = soup.find_all('h2', recursive=False)
    contents = []
    for idx in range(len(items)):
        contents.append([f'week-{idx+1}', f'weeks/week-{idx+1}/index', items[idx].get_text(), items[idx].find_next_sibling("p").get_text()])

    index_tiles = ''.join(create_index_tile(x, in_week=False) for x in contents)

    template = template.replace('{{page_title}}', title.get_text())
    template = template.replace('{{page_intro}}', intro.get_text())
    template = template.replace('{{index_tiles}}', index_tiles)
    return template


def create_page(week_number, template_source, page_source):
    with open(f'framework/templates/week/{template_source}.tpl.html', 'r') as f:
        page = f.read()
    
    with open(f'src/week-{week_number}/{page_source}.md', 'r') as md:
        html = markdown.markdown(md.read())

    soup = BeautifulSoup(html, "html.parser")
    title = soup.find("h1", recursive=False)
    intro = title.find_next_sibling("p") if title else None

    if title is None or intro is None:
        raise ValueError("Document must start with an H1 followed by a paragraph")
        
    title_content = title.get_text()
    intro_content = intro.get_text()
    page = page.replace('{{title}}', title_content)
    page = page.replace('{{intro}}', intro_content)
    title.decompose()
    intro.decompose()
    page = page.replace('{{content}}', soup.prettify())
    
    return page, title_content, intro_content