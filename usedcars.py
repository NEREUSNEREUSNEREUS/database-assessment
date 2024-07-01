# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'usedcars.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()
menu_choice =''
while menu_choice != '0':
    menu_choice = input('\nWelcome to the Cars database\n\n'
                        'Type the number for the query that you would like to see.:\n\n' 
                        '1: View all data\n'
                        '2: Cars produced after 2010\n'
                        '3: Cars produced before 2010\n'
                        '4: Cars with 7 seats\n'
                        '5: Safest cars\n'
                        '6: Most fuel efficient cars (litre per 100 kilometres)\n'
                        '0: Exit\n\nType option here: ')
    menu_choice = menu_choice.upper()
    if menu_choice == '1':
        print_query('View all data')
    elif menu_choice == '2':
        print_query('Cars produced after 2010')
    elif menu_choice == '3':
        print_query('Cars produced before 2010')
    elif menu_choice == '4':
        print_query('Cars with 7 seats')
    elif menu_choice == '5':
        print_query('Safest Cars')
    elif menu_choice == '6':
        print_query('Most fuel efficient cars')