import yaml


def edit_conf_files(folder_name, url, pages_to_scrape, server, username, password):
    with open('./conf/conf_scrape.yaml') as f:
        scrape_file = yaml.safe_load(f)

        scrape_file['dir_name'] = folder_name     
        scrape_file['url'] = url
        scrape_file['pages_to_scrape'] = pages_to_scrape

    with open('./conf/conf_scrape.yaml', 'w') as f:
        yaml.dump(scrape_file, f)

    with open('./conf/conf_graph.yaml') as f:
        graph_file = yaml.safe_load(f)

        graph_file['server'] = server     
        graph_file['username'] = username
        graph_file['password'] = password
        graph_file['dir_name'] = folder_name

    with open('./conf/conf_graph.yaml', 'w') as f:
        yaml.dump(graph_file, f)



if __name__ == '__main__': 
    edit_conf_files('asd', 'sda', 'dsa', '1', '1', '3')