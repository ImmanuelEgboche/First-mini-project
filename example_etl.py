from datetime import datetime
import pymysql 
import os 
from dotenv import load_dotenv
import csv 
import pandas as pd
import pprint

# data = pd.read_csv (r'/Users/apple/desktop/de_work/sales_data.csv')
# df = pd.DataFrame(data, columns= ['Customer_id','Purchase_date','Purchase_amount','product_id'])
# print(df)
pp = pprint.PrettyPrinter(indent=2)
#What they want us to work out 
customer_spend = {}
customer_sales = {}
sales_data = [] #clean version 
unfiltered_sales_data = []
date1 = datetime.strptime('2020-12-01','%Y-%m-%d') #Subs for date
date2 = datetime.strptime('2020-12-05','%Y-%m-%d')

def setup_db_connection():
    #establish the connection and return the connectors?
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    Immanuel = os.environ.get("mysql_db")
    return pymysql.connect(
        host,
        user,
        password,
        Immanuel
    )
def create_table():
    connectdb = setup_db_connection()
    cursor = connectdb.cursor()
    create_sales_table = \
        """
        CREATE TABLE IF NOT EXISTS sales_data(
            customer_id int NOT NULL,
            average_spend decimal(19,2),
            product_id varchar(10)
        );
        """
    create_customer_spend_table = \
        """
        CREATE TABLE IF NOT EXISTS customer_spend(
            customer_id int NOT NULL,
            average_spend decimal(19,2),
            total_spend decimal(19,2)
            );
        """
    create_customer_products_table = \
        """
        CREATE TABLE IF NOT EXISTS customer_products(
            customer_id int NOT NULL,
            product_id varchar(10),
            quantity int
            );
        """
    cursor.execute(create_sales_table)
    cursor.execute(create_customer_spend_table)
    cursor.execute(create_customer_products_table)
    connectdb.commit()
    cursor.close()
    connectdb.close()
try:
    with open('sales_data.csv', 'r', newline='')  as f:
        source_file = csv.DictReader(f,fieldnames=['Customer_id','Purchase_date','Purchase_amount','product_id'])
        next(source_file,None)
        for line in source_file:
            print(line)
            # if '' in line.values():
        #         continue
        #     sales_data.append(line)
            
    # print(sales_data)
except FileNotFoundError:
    print('You know the deal')

setup_db_connection()
create_table()