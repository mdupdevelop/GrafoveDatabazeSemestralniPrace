import tkinter as tk
import scraper
import graphtransfer

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

    left_column = tk.Frame(center, width = 250)
    right_column = tk.Frame(center, width = 250)

    left_column.grid(row = 0, column = 0, sticky = "ew")
    right_column.grid(row = 1, column = 0, sticky = "ew")
    
    # Left column buttons
    tk.Label(left_column, text = 'Neo4j server settings').grid(row = 0, column =    0, columnspan = 3, sticky = tk.W + tk.E)

    tk.Label(left_column, text = 'Server:', width= 15).grid(row = 1, column = 0)
    server_entry = tk.Entry(left_column)
    server_entry.insert(0, 'bolt://localhost:7687')
    server_entry.grid(row = 1, column = 1)

    tk.Label(left_column, text = 'Username:').grid(row = 2, column = 0)
    username_entry = tk.Entry(left_column)
    username_entry.insert(0, 'neo4j')
    username_entry.grid(row = 2, column = 1)

    tk.Label(left_column, text = 'Password').grid(row = 3, column = 0)
    password_entry = tk.Entry(left_column)
    password_entry.insert(0, '123')
    password_entry.grid(row = 3, column = 1)

    tk.Button(left_column, text = "Clear DB", command = graphtransfer.clear_db, width= 10).grid(row = 1, column = 2, rowspan = 3, sticky = tk.N + tk.S)


    # Right column buttons
    tk.Label(right_column, text = 'Page settings').grid(row = 0, columnspan = 3, sticky = tk.W + tk.E)

    tk.Label(right_column, text = 'Folder name:', width= 15).grid(row = 1, column = 0)
    tk.Entry(right_column).grid(row = 1, column = 1)

    tk.Label(right_column, text = 'Article URL:').grid(row = 2, column = 0)
    tk.Entry(right_column).grid(row = 2, column = 1)

    tk.Label(right_column, text = 'Pages to scrape:').grid(row = 3, column = 0)
    tk.Entry(right_column).grid(row = 3, column = 1)

    tk.Button(right_column, text = "Scrape", command = scraper.main, width= 10).grid(row = 1, column = 2)
    tk.Button(right_column, text = "Send to graph", command = scraper.main, width= 10).grid(row = 2, column = 2)
    tk.Button(right_column, text = "Both", command = scraper.main, width= 10).grid(row = 3, column = 2)

    root.mainloop()