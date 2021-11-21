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
    return render_template('index.html')


@app.route('/searchBook', methods=["GET", 'POST'])
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
    cursor, connection = util.connect_to_db(username, password, host, port, database)
    books = session['testing']
    newTitle = "'%" + books + "%'"
    print(newTitle)
    record = util.run_and_fetch_sql(cursor, "SELECT * from alldata where original_title like %s order by best_book_id;" % newTitle)
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
            send = util.runSQL(cursor, "insert into userinfo values %s; Commit;" % username1)
            util.disconnect_from_db(connection, cursor)
            return redirect(url_for('userPage'))
        else:
            util.disconnect_from_db(connection, cursor)
            return redirect(url_for('fail'))
    return render_template('signUp.html')

#loads the userpage for the user's profile.
@app.route('/userPage', methods = ["GET", 'POST'])
def userPage():
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    genre = session['bookgenre']
    favGenres = 'select liked_genres as "" from userlists where '
    record = util.run_and_fetch_sql(cursor, favGenres)
    util.disconnect_from_db(connection,cursor)
    if request.method == 'POST':
        if request.form.get("logout"):
            return redirect(url_for('logout'))
        if request.form.get("addGenre"):
            return redirect(url_for('userAddGenre'))
    return render_template('userProfile.html')

@app.route('/logout', methods=["GET", 'POST'])
def logout():
    session['username'] = None
    return redirect(url_for('index'))

@app.route('/userPageFail')
def fail():
    return render_template('userPageFail.html')

@app.route('/searchGenre', methods = ["GET", 'POST'])
def searchGenre():
    if request.method == 'POST':
        if request.form.get("history"):
            session['bookgenre'] = 'select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from alldata, allbookgenre where alldata.best_book_id = allbookgenre.book_id order by "history, historical fiction, biography" desc;'
            return redirect(url_for('showGenre'))
        elif request.form.get("fiction"):
            session['bookgenre'] = 'select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from alldata, allbookgenre where alldata.best_book_id = allbookgenre.book_id order by allbookgenre.fiction desc;'
            return redirect(url_for('showGenre'))
        elif request.form.get("fantasy"):
            session['bookgenre'] = 'select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from alldata, allbookgenre where alldata.best_book_id = allbookgenre.book_id order by "fantasy, paranormal" desc;'
            return redirect(url_for('showGenre'))
        elif request.form.get("mystery"):
            session['bookgenre'] = 'select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from alldata, allbookgenre where alldata.best_book_id = allbookgenre.book_id order by "mystery, thriller, crime" desc;'
            return redirect(url_for('showGenre'))
        elif request.form.get("poetry"):
            session['bookgenre'] = 'select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from alldata, allbookgenre where alldata.best_book_id = allbookgenre.book_id order by allbookgenre.poetry desc;'
            return redirect(url_for('showGenre'))
        elif request.form.get("romance"):
            session['bookgenre'] = 'select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from alldata, allbookgenre where alldata.best_book_id = allbookgenre.book_id order by allbookgenre.romance desc;'
            return redirect(url_for('showGenre'))
        elif request.form.get("nonfiction"):
            session['bookgenre'] = 'select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from alldata, allbookgenre where alldata.best_book_id = allbookgenre.book_id order by "non-fiction" desc;'
            return redirect(url_for('showGenre'))
        elif request.form.get("children"):
            session['bookgenre'] = 'select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from alldata, allbookgenre where alldata.best_book_id = allbookgenre.book_id order by allbookgenre.children desc;'
            return redirect(url_for('showGenre'))
        elif request.form.get("youngadult"):
            session['bookgenre'] = 'select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from alldata, allbookgenre where alldata.best_book_id = allbookgenre.book_id order by "young-adult" desc;'
            return redirect(url_for('showGenre'))
        elif request.form.get("comics"):
            session['bookgenre'] = 'select best_book_id as "ID", original_publication_year as "Year Published", original_title as "Title" from alldata, allbookgenre where alldata.best_book_id = allbookgenre.book_id order by "comics, graphic" desc;'
            return redirect(url_for('showGenre'))
    return render_template('searchGenre.html')

@app.route('/userAddGenre', methods = ["GET", 'POST'])
def userAddGenre():
    if request.method == 'POST':
        if request.form.get("history"):
            session['bookgenre'] =  'History'
            return redirect(url_for('userPage'))
        elif request.form.get("fiction"):
            session['bookgenre'] = 'Fiction'
            return redirect(url_for('userPage'))
        elif request.form.get("fantasy"):
            session['bookgenre'] = 'Fantasy'
            return redirect(url_for('userPage'))
        elif request.form.get("mystery"):
            session['bookgenre'] = 'Mystery'
            return redirect(url_for('userPage'))
        elif request.form.get("poetry"):
            session['bookgenre'] = 'Poetry'
            return redirect(url_for('userPage'))
        elif request.form.get("romance"):
            session['bookgenre'] = 'Romance'
            return redirect(url_for('userPage'))
        elif request.form.get("nonfiction"):
            session['bookgenre'] = 'Non-Fiction'
            return redirect(url_for('userPage'))
        elif request.form.get("children"):
            session['bookgenre'] = 'Children'
            return redirect(url_for('userPage'))
        elif request.form.get("youngadult"):
            session['bookgenre'] = 'Young-Adult'
            return redirect(url_for('userPage'))
        elif request.form.get("comics"):
            session['bookgenre'] = 'Comics'
            return redirect(url_for('userPage'))
    return render_template('searchGenre.html')

@app.route('/showGenre')
def showGenre():
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    genres = session['bookgenre']
    record = util.run_and_fetch_sql(cursor, genres)
    if record == -1:
        print('Error in showbooks')
    else:
        col_names = [desc[0] for desc in cursor.description]
        log = record[:10]
    util.disconnect_from_db(connection,cursor)
    return render_template('showGenre.html', sql_table=log, table_title=col_names)

# The function for calculating the top two genres for a particular book
@app.route('/toptwo')
def topTwo():
    script = "select book_id," + '"history, historical fiction, biography"/total_genre::float as numhis,' + 'fiction/total_genre::float as numfic,' + '"fantasy, paranormal"/total_genre::float as numfan,' +'"mystery, thriller, crime"/total_genre::float as nummys,'+'poetry/total_genre::float as numpoe,'+'romance/total_genre::float as numrom,'+'"non-fiction"/total_genre::float as numnon,'+'children/total_genre::float as numchi,'+'"young-adult"/total_genre::float as numyou,'+'"comics, graphic"/total_genre::float as numcom,'+'total_genre from allbookgenre where total_genre > 0'
    cursor, connection = util.connect_to_db(username, password, host, port, database)
    record = util.run_and_fetch_sql(cursor, script)
    if record == -1:
        print('Something is wrong with the SQL command')
    else:
        col_names = [desc[0] for desc in cursor.description]
        log = record[:10]
    listOfTops = []
    for x in record:
        name = x[0]
        topper = x[1:11]
        topper2 = sorted(topper, reverse=True)
        max1 = topper2[0]
        max2 = topper2[1]
        index = topper.index(max1)
        index2 = topper.index(max2)
        listOfTops.append((name, util.genreAssign(index), util.genreAssign(index2)))
    print(len(listOfTops))
    print(len(record))
    util.disconnect_from_db(connection, cursor)
    print("now evaluating the listofTops stuff")
    cursor, connection = util.connect_to_db(username, password, host, port, database)
    i = 0
    for x in listOfTops:
        id = "'" + x[0] + "'"
        top_gen = "'" + x[1] + "'"
        sec_gen = "'" + x[2] + "'"
        thescript = "update alldata set first_genre = " + top_gen + " , second_genre = " + sec_gen + " where best_book_id = " + id + "; commit;"
        util.runnerSQL(cursor, thescript)
        i += 1
        print(i)
    util.disconnect_from_db(connection, cursor)
    return render_template('showGenre.html', sql_table=log, table_title=col_names)

if __name__ == '__main__':
    # set debug mode
    app.debug = True
    app.secret_key = "banana"
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)
