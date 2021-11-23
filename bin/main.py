import tkinter as tk

from lib import scraper
from lib import graphtransfer
from lib import yaml_editor


if __name__ == '__main__':
    
    root = tk.Tk()
    root.title('iDnes graph scraper')



    # Create main containers
    header = tk.Frame(root, width=450, height=50)
    center = tk.Frame(root, width=50, height=40, padx=3, pady=3)
    
    # layout all of the main containers
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    header.grid(row = 0, sticky='ew')
    center.grid(row = 1, sticky='nsew') 


    # Widgets for header frame
    header_label = tk.Label(header, text = 'iDnes Scraper to graph - dupm01')
    header_label.pack(fill="both")


    # create the center widgets
    center.grid_rowconfigure(0, weight=1)
    center.grid_columnconfigure(1, weight=1)

    top_row = tk.Frame(center, width = 250)
    bottom_row = tk.Frame(center, width = 250)

    top_row.grid(row = 0, column = 0, sticky = "ew")
    bottom_row.grid(row = 1, column = 0, sticky = "ew")
    
    # Left column buttons
    tk.Label(top_row, text = 'Neo4j server settings').grid(row = 0, column =    0, columnspan = 3, sticky = tk.W + tk.E)

    tk.Label(top_row, text = 'Server:', width= 15).grid(row = 1, column = 0)
    server_entry = tk.Entry(top_row)
    server_entry.insert(0, 'bolt://localhost:7687')
    server_entry.grid(row = 1, column = 1)

    tk.Label(top_row, text = 'Username:').grid(row = 2, column = 0)
    username_entry = tk.Entry(top_row)
    username_entry.insert(0, 'neo4j')
    username_entry.grid(row = 2, column = 1)

    tk.Label(top_row, text = 'Password').grid(row = 3, column = 0)
    password_entry = tk.Entry(top_row)
    password_entry.insert(0, '123')
    password_entry.grid(row = 3, column = 1)

    tk.Button(top_row, text = "Clear DB", command = lambda: [yaml_editor.edit_conf_graph(server_entry.get(), username_entry.get(), password_entry.get()), graphtransfer.clear_db()], width= 10).grid(row = 1, column = 2, rowspan = 3, sticky = tk.N + tk.S)


    # Right column buttons
    tk.Label(bottom_row, text = 'Page settings').grid(row = 0, columnspan = 3, sticky = tk.W + tk.E)

    tk.Label(bottom_row, text = 'Folder name:', width= 15).grid(row = 1, column = 0)
    folder_entry = tk.Entry(bottom_row)
    folder_entry.grid(row = 1, column = 1)

    tk.Label(bottom_row, text = 'Article URL:').grid(row = 2, column = 0)
    url_entry = tk.Entry(bottom_row)
    url_entry.grid(row = 2, column = 1)

    tk.Label(bottom_row, text = 'Pages to scrape:').grid(row = 3, column = 0)
    scrapenumber_entry = tk.Entry(bottom_row)
    scrapenumber_entry.grid(row = 3, column = 1)

    tk.Button(bottom_row, text = "Scrape", command = lambda: [yaml_editor.edit_conf_files(folder_entry.get(), url_entry.get(), scrapenumber_entry.get(), server_entry.get(), username_entry.get(), password_entry.get()), scraper.main()], width= 10).grid(row = 1, column = 2)
    tk.Button(bottom_row, text = "Send to graph", command = lambda: [yaml_editor.edit_conf_files(folder_entry.get(), url_entry.get(), scrapenumber_entry.get(), server_entry.get(), username_entry.get(), password_entry.get()), graphtransfer.main()], width= 10).grid(row = 2, column = 2)
    tk.Button(bottom_row, text = "Both", command = lambda: [yaml_editor.edit_conf_files(folder_entry.get(), url_entry.get(), scrapenumber_entry.get(), server_entry.get(), username_entry.get(), password_entry.get()), scraper.main(), graphtransfer.main()], width= 10).grid(row = 3, column = 2)

    root.mainloop()