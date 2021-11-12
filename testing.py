from flask import Flask, render_template, request, url_for, session
from werkzeug.utils import redirect

import util

app = Flask(__name__)

username = 'postgres'
password = 'Password'
host = '127.0.0.1'
port = '5432'
database = 'BillyBooks'


@app.route('/')
def index():
    cursor, connection = util.connect_to_db(username, password, host, port, database)
    record = util.run_and_fetch_sql(cursor, "SELECT * from alldata;")
    if record == -1:
        print('Something is wrong with the SQL command')
    else:
        col_names = [desc[0] for desc in cursor.description]
        log = record[:5]
    util.disconnect_from_db(connection, cursor)
    return render_template('index.html', sql_table=log, table_title=col_names)


@app.route('/searchBook', methods=["GET", 'POST'])
def searchBar():
    if request.method == 'POST':
        booksearched = request.form.get("searched")
        print("book being searched for")
        print(booksearched)
        session['testing'] = booksearched
        return redirect(url_for('showBooks'))
    return render_template('searchBook.html')


# Miriam's App Route for clicking on book id
# This isn't complete, I just been having too much happening to me this week but I got this far.
@app.route('/bookDetails', methods=["GET", "POST"])
def bookClickedOn():
    if request.method == 'POST':
        cursor, connection = util.connect_to_db(username, password, host, port, database)
        clickedBook = request.form.get("bookID")
        showClicked = util.run_and_fetch_sql(cursor, "SELECT original_title, original_publication_year from alldata;")
        print("gathering book information")



@app.route('/showBooks')
def showBooks():
    cursor, connection = util.connect_to_db(username, password, host, port, database)
    books = session['testing']
    newTitle = "'%" + books + "%'"
    print(newTitle)
    record = util.run_and_fetch_sql(cursor,
                                    "SELECT * from alldata where original_title like %s order by best_book_id;" % newTitle)
    if record == -1:
        print('Error in showbooks')
    else:
        col_names = [desc[0] for desc in cursor.description]
        log = record[:10]
    util.disconnect_from_db(connection, cursor)
    return render_template('showBooks.html', sql_table=log, table_title=col_names)


@app.route('/signIn', methods=["GET", 'POST'])
def signIn():
    if request.method == 'POST':
        username1 = request.form.get("email")
        password1 = request.form.get("password")
        print("username and password:")
        print(username1 + ' ' + password1)
        # add code to ping the database for the username and password
        cursor, connection = util.connect_to_db(username, password, host, port, database)
        userpass = "username = " + "'" + username1 + "'" + " and password = " + "'" + password1 + "'"
        record = util.run_and_fetch_sql(cursor, "SELECT username from userinfo where %s" % userpass)
        record = len(record)
        #print('size of the list' + record)
        util.disconnect_from_db(connection, cursor)
        if record == 0:
            return redirect(url_for('fail'))
        else:
            return redirect(url_for('userPage'))
    return render_template('signIn.html')

@app.route('/signUp', methods=["GET", 'POST'])
def signUp():
    if request.method == "POST":
        username1 = request.form.get("email")
        password1 = request.form.get("psw")
        print(username1 + ' ' + password1)
        cursor, connection = util.connect_to_db(username, password, host, port, database)
        userpass = "username = " + "'" + username1 + "'"
        record = util.run_and_fetch_sql(cursor, "SELECT username from userinfo where %s" % userpass)
        # print('size of the list' + record)
        username1 = "'" + username1 + "'"
        password1 = "'" + password1 + "'"
        record = len(record)
        if record < 1:
            send = util.runSQL(cursor, "insert into userinfo values ( %s , %s ); Commit;" % (username1 , password1))
            util.disconnect_from_db(connection, cursor)
            return redirect(url_for('userPage'))
        else:
            util.disconnect_from_db(connection, cursor)
            return redirect(url_for('fail'))
    return render_template('signUp.html')

#loads the userpage for the user's profile.
@app.route('/userPage')
def userPage():
    return render_template('userPage.html')

@app.route('/userPageFail')
def fail():
    return render_template('userPageFail.html')

@app.route('/searchGenre', methods = ["GET", 'POST'])
def searchGenre():
    if request.method == 'POST':
        if request.form.get("history"):
            session['bookgenre'] = 'select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from alldata, allbookgenre where allbookdata.best_book_id = allbookgenre.book_id order by "history, historical fiction, biography" desc;'
            return redirect(url_for('showGenre'))
        elif request.form.get("fiction"):
            session['bookgenre'] = 'select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from alldata, allbookgenre where allbookdata.best_book_id = allbookgenre.book_id order by allbookgenre.fiction desc;'
            return redirect(url_for('showGenre'))
        elif request.form.get("fantasy"):
            session['bookgenre'] = 'select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from alldata, allbookgenre where allbookdata.best_book_id = allbookgenre.book_id order by "fantasy, paranormal" desc;'
            return redirect(url_for('showGenre'))
        elif request.form.get("mystery"):
            session['bookgenre'] = 'select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from alldata, allbookgenre where allbookdata.best_book_id = allbookgenre.book_id order by "mystery, thriller, crime" desc;'
            return redirect(url_for('showGenre'))
        elif request.form.get("poetry"):
            session['bookgenre'] = 'select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from alldata, allbookgenre where allbookdata.best_book_id = allbookgenre.book_id order by allbookgenre.poetry desc;'
            return redirect(url_for('showGenre'))
        elif request.form.get("romance"):
            session['bookgenre'] = 'select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from alldata, allbookgenre where allbookdata.best_book_id = allbookgenre.book_id order by allbookgenre.romance desc;'
            return redirect(url_for('showGenre'))
        elif request.form.get("nonfiction"):
            session['bookgenre'] = book_id = 'select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from alldata, allbookgenre where allbookdata.best_book_id = allbookgenre.book_id order by "non-fiction" desc;'
            return redirect(url_for('showGenre'))
        elif request.form.get("children"):
            session['bookgenre'] = 'select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from alldata, allbookgenre where allbookdata.best_book_id = allbookgenre.book_id order by allbookgenre.children desc;'
            return redirect(url_for('showGenre'))
        elif request.form.get("youngadult"):
            session['bookgenre'] = 'select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from alldata, allbookgenre where allbookdata.best_book_id = allbookgenre.book_id order by "young-adult" desc;'
            return redirect(url_for('showGenre'))
        elif request.form.get("comics"):
            session['bookgenre'] = 'select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from alldata, allbookgenre where allbookdata.best_book_id = allbookgenre.book_id order by "comics, graphic" desc;'
            return redirect(url_for('showGenre'))
    return render_template('searchGenre.html')

@app.route('/showGenre')
def showGenre():
    cursor, connection = util.connect_to_db(username, password, host, port, database)
    genres = session['bookgenre']
    record = util.run_and_fetch_sql(cursor, genres)
    if record == -1:
        print('Error in showbooks')
    else:
        col_names = [desc[0] for desc in cursor.description]
        log = record[:10]
    util.disconnect_from_db(connection, cursor)
    return render_template('showGenre.html', sql_table = log, table_title=col_names)

if __name__ == '__main__':
    # set debug mode
    app.debug = True
    app.secret_key = "banana"
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)
