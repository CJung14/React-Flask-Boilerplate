from flask import Flask
import psycopg2

# Initializing flask app
app = Flask(__name__)

import os
from dotenv import load_dotenv

load_dotenv()

# Initializing database
conn = psycopg2.connect(database=os.getenv('DATABASE'), user=os.getenv('USER'), password=os.getenv('PASSWORD'), host=os.getenv('HOST'), port=os.getenv('PORT'))
cur = conn.cursor()

# if you already have any table or not id doesnt matter this 
# will create a products table for you.
cur.execute(
    '''CREATE TABLE IF NOT EXISTS products (id serial \
     PRIMARY KEY, name varchar(100), price float);''')
  
# Insert some data into the table
cur.execute(
    '''INSERT INTO products (name, price) VALUES \
     ('Apple', 1.99), ('Orange', 0.99), ('Banana', 0.59);''')
  
# commit the changes
conn.commit()
  
# close the cursor and connection
cur.close()
conn.close()

# Route for seeing a data
@app.route('/data')
def get_time():

	# Returning an api for showing in reactjs
	return {
		'Name':"geek",
		"Age":"22",
		"Date":"x",
		"programming":"python"
		}

	
# Running app
if __name__ == '__main__':
	app.run(debug=True)

