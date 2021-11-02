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

@app.route('/historySug')
def historyGen():
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    record = util.run_and_fetch_sql(cursor, "select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from allbookdata, allbookgenre where allbookdata.best_book_id = allbookgenre.book_id and original_title != '' order by "history, historical fiction, biography" desc;")
    if record == -1:
        print('Something is wrong with the SQL command')
    else:
        col_names = [desc[0] for desc in cursor.description]
        log = record[:10]
    util.disconnect_from_db(connection,cursor)
    return render_template('hisBio.html', sql_table = log, table_title=col_names)

app.route('/fictionSug')
def fictionGen():
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    record = util.run_and_fetch_sql(cursor, "select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from allbookdata, allbookgenre where allbookdata.best_book_id = allbookgenre.book_id and original_title != '' order by allbookgenre.fiction desc;")
    if record == -1:
        print('Something is wrong with the SQL command')
    else:
        col_names = [desc[0] for desc in cursor.description]
        log = record[:10]
    util.disconnect_from_db(connection,cursor)
    return render_template('fic.html', sql_table = log, table_title=col_names)

app.route('/fantasySug')
def fantasyGen():
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    record = util.run_and_fetch_sql(cursor, "select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from allbookdata, allbookgenre where allbookdata.best_book_id = allbookgenre.book_id and original_title != '' order by "fantasy, paranormal" desc;")
    if record == -1:
        print('Something is wrong with the SQL command')
    else:
        col_names = [desc[0] for desc in cursor.description]
        log = record[:10]
    util.disconnect_from_db(connection,cursor)
    return render_template('fantPara.html', sql_table = log, table_title=col_names)

app.route('/mysterySug')
def mysteryGen():
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    record = util.run_and_fetch_sql(cursor, "select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from allbookdata, allbookgenre where allbookdata.best_book_id = allbookgenre.book_id and original_title != '' order by "mystery, thriller, crime" desc;")
    if record == -1:
        print('Something is wrong with the SQL command')
    else:
        col_names = [desc[0] for desc in cursor.description]
        log = record[:10]
    util.disconnect_from_db(connection,cursor)
    return render_template('mysThr.html', sql_table = log, table_title=col_names)

app.route('/poetrySug')
def poetryGen():
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    record = util.run_and_fetch_sql(cursor, "select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from allbookdata, allbookgenre where allbookdata.best_book_id = allbookgenre.book_id and original_title != '' order by allbookgenre.poetry desc;")
    if record == -1:
        print('Something is wrong with the SQL command')
    else:
        col_names = [desc[0] for desc in cursor.description]
        log = record[:10]
    util.disconnect_from_db(connection,cursor)
    return render_template('poetry.html', sql_table = log, table_title=col_names)

app.route('/romanceSug')
def romanceGen():
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    record = util.run_and_fetch_sql(cursor, "select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from allbookdata, allbookgenre where allbookdata.best_book_id = allbookgenre.book_id and original_title != '' order by allbookgenre.romance desc;")
    if record == -1:
        print('Something is wrong with the SQL command')
    else:
        col_names = [desc[0] for desc in cursor.description]
        log = record[:10]
    util.disconnect_from_db(connection,cursor)
    return render_template('romance.html', sql_table = log, table_title=col_names)

app.route('/nonFictionSug')
def nonFictionGen():
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    record = util.run_and_fetch_sql(cursor, "select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from allbookdata, allbookgenre where allbookdata.best_book_id = allbookgenre.book_id and original_title != '' order by "non-fiction" desc;")
    if record == -1:
        print('Something is wrong with the SQL command')
    else:
        col_names = [desc[0] for desc in cursor.description]
        log = record[:10]
    util.disconnect_from_db(connection,cursor)
    return render_template('nonFic.html', sql_table = log, table_title=col_names)

app.route('/childrenSug')
def childrenGen():
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    record = util.run_and_fetch_sql(cursor, "select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from allbookdata, allbookgenre where allbookdata.best_book_id = allbookgenre.book_id and original_title != '' order by allbookgenre.children desc;")
    if record == -1:
        print('Something is wrong with the SQL command')
    else:
        col_names = [desc[0] for desc in cursor.description]
        log = record[:10]
    util.disconnect_from_db(connection,cursor)
    return render_template('child.html', sql_table = log, table_title=col_names)

app.route('/youngAdultSug')
def youngAdultGen():
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    record = util.run_and_fetch_sql(cursor, "select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from allbookdata, allbookgenre where allbookdata.best_book_id = allbookgenre.book_id and original_title != '' order by "young-adult" desc;")
    if record == -1:
        print('Something is wrong with the SQL command')
    else:
        col_names = [desc[0] for desc in cursor.description]
        log = record[:10]
    util.disconnect_from_db(connection,cursor)
    return render_template('youngAdult.html', sql_table = log, table_title=col_names)

app.route('/comicsSug')
def comicsGen():
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    record = util.run_and_fetch_sql(cursor, "select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from allbookdata, allbookgenre where allbookdata.best_book_id = allbookgenre.book_id and original_title != '' order by "comics, graphic" desc;")
    if record == -1:
        print('Something is wrong with the SQL command')
    else:
        col_names = [desc[0] for desc in cursor.description]
        log = record[:10]
    util.disconnect_from_db(connection,cursor)
    return render_template('comicGraph.html', sql_table = log, table_title=col_names)


if __name__ == '__main__':
    # set debug mode
    app.debug = True
    app.secret_key = "banana"
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)
