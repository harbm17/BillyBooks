from flask import Flask, render_template, request, url_for, session
from werkzeug.utils import redirect

import util


app = Flask(__name__)


username='postgres'
password='Password'
host='127.0.0.1'
port='5432'
database='BillyBooks'

@app.route('/')
def index():
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    record = util.run_and_fetch_sql(cursor, "SELECT * from alldata;")
    if record == -1:
        print('Something is wrong with the SQL command')
    else:
        col_names = [desc[0] for desc in cursor.description]
        log = record[:10]
    util.disconnect_from_db(connection,cursor)
    return render_template('index.html', sql_table = log, table_title=col_names)

@app.route('/searchBook', methods = ["GET", 'POST'])
def searchBar():
    if request.method == 'POST':
        booksearched = request.form.get("searched")
        print("book being searched for")
        print(booksearched)
        session['testing'] = booksearched
        return redirect(url_for('showBooks'))
    return render_template('searchBook.html')

@app.route('/showBooks')
def showBooks():
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    books = session['testing']
    newTitle = "'%" + books + "%'"
    print(newTitle)
    record = util.run_and_fetch_sql(cursor, "SELECT * from alldata where original_title like %s order by best_book_id;" % newTitle)
    if record == -1:
        print('Error in showbooks')
    else:
        col_names = [desc[0] for desc in cursor.description]
        log = record[:10]
    util.disconnect_from_db(connection,cursor)
    return render_template('showBooks.html', sql_table = log, table_title=col_names)


if __name__ == '__main__':
    # set debug mode
    app.debug = True
    app.secret_key = "banana"
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)