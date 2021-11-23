
import os
import json
import requests
import shutil
import yaml
import time
from bs4 import BeautifulSoup




def get_page_soup(link):
    ''''
    Convert http/https link into BeautifulSoupFormat

    Args:
        link: url , for context of this program, idnes article, for example: https://www.idnes.cz/zpravy/domaci/zeman-zdravi-ovcacek-brifink-mynar.A211014_140358_domaci_remy
    '''
    
    page = ''
    counter = 0
    while page == '':
        if counter < 5:
            try:    
                page = requests.get(link)
                break
            except: 
                counter = counter + 1 
                print("Connection refused by the server... waiting  5 seconds, check if the link is valid")
                time.sleep(5)
        else:
            break

    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def retrieve_page_title(soup):
    '''
    Return idnes article title
    
    Args:
        soup: soup of idnes article
    '''
    page_title = soup.h1.text
    return page_title

def retrieve_page_authors(soup):
    '''
    Return article author
    
    Args:
        soup: soup of idnes article
    '''

    
    try:
        author = soup.findAll(rel='author')[1].span.text
    except IndexError:
        try:  
            author = soup.find(rel='author').span.text
        except:
            author = 'MediaOrganisation'
    return author

def retrieve_references_to(soup):
    '''
    Return article 'Souvisejici' section
    
    Args:
        soup: soup of idnes article
    '''
    
    try: 
        references_to = soup.find(id='related-list').find_all('a')
    except:
        print(soup)
        references_to = []
    references_to_list = []
    for page in references_to:
        if page.text == 'Premium':
            continue

        if 'idnes' not in page['href']:
            continue

        references_to_list.append({
        'page_name': page.text,
        'page_url' : page['href']
        })
    return references_to_list

def retrieve_topics(soup):
    '''
    Return article 'Temata' section
    
    Args:
        soup: soup of idnes article
    '''
    topics = soup.find(id='art-tags').find_all('a')
    topics_list = []
    for topic in topics:
        topics_list.append(topic.text)
    return topics_list


def create_json_page(page_title, page_url, page_author, page_references, page_topics, conf_dir_name):
    ''''
    Convert article information into json file

    Args:
        page_title: title of the article
        page_url: url to the article
        page_author: author of the article
        page_references: list of 'souvisejici'
        page_topics: list of 'Temata' 
    '''
    global page_counter

    site_info = {}
    site_info['pages'] = []
    site_info['pages'].append({
    'page_title': page_title,
    'written_by': page_author,
    'page_url' : page_url,
    'references_to': page_references,
    'topics': page_topics
    })

    with open(f'./{conf_dir_name}/page'+str(page_counter)+'.json', 'w', encoding='utf8') as outfile:
        json.dump(site_info, outfile, ensure_ascii=False)
    
    page_counter = page_counter+1

    return None


def do_everything(page_url, conf_dir_name):
    ''''
    Calls other functions in this file. Retrieve all information, convert and save them into json.
    '''
    soup            = get_page_soup(page_url)
    page_title      = retrieve_page_title(soup)
    page_author     = retrieve_page_authors(soup)
    page_references = retrieve_references_to(soup)
    page_topics     = retrieve_topics(soup)    
    create_json_page(page_title, page_url, page_author, page_references, page_topics, conf_dir_name)
    print(str(page_counter) + '_____' + page_title + '____' + 'succesfuly scraped.')


def main():
    with open('./conf/conf_scrape.yaml') as file:
        conf_yaml            = yaml.safe_load(file)
        conf_url             = conf_yaml['url']
        conf_pages_to_scrape = conf_yaml['pages_to_scrape']
        conf_dir_name        = conf_yaml['dir_name']
        conf_pages_to_scrape = int(conf_pages_to_scrape)

    global page_counter
    page_counter = 0

    # Prepares dir for json files to be saved at, if folder already exists, it is remade
    if (os.path.isdir(conf_dir_name)) : 
        shutil.rmtree(conf_dir_name)
        os.mkdir(f'./{conf_dir_name}')
    else: 
        os.mkdir(f'./{conf_dir_name}')

    # Scrape first article
    do_everything(conf_url, conf_dir_name)

    # Cycle of scraping articles in json files
    for x in range(conf_pages_to_scrape):
        with open(f'./{conf_dir_name}/page{x}.json') as json_file:
            data = json.load(json_file)['pages']
            for i in range(len(data)):
                for j in range(len(data[i]['references_to'])):
                    references = data[i]['references_to'][j]
                    do_everything(references['page_url'], conf_dir_name)

    print('Scraping completed')
if __name__ == '__main__': 
    main()



