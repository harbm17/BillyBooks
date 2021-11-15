# Billy Books
Billy Books is a webpage application that interacts with a database that holds information about 2 million books. The user is able to search a book by title, personalize their profile based on their author, genre, and book interests.

# Getting started:
/*Quick note all this command work on windows future editing
might be required for mac usage*/
1.) Make sure you have the latest Python version installed.

2.)Create a vitrual environment using "python3 -m venv ./venv".

3.) Enter this command "./venv/Scripts/activate" to enter the venv on your terminal 

4.) use the command "pip install -r requirements.txt" to install all required libraries.

/* quick note we do this so we do not have to install all these packages globaly but rather just have 
them on the virtual environment so we do not run into issues of having different versions of certain libraries*/

5.)after you have your virtual environment setup go to the .env and in this file User, PASS, and DATABASE should be blank.
  you wil need to add the sample USER name you created to equal user, the password given for that user to PASS, and add 
  the database name you given for this project too DATABASE. (Go down to pgadmin setup if you don't have these) 

/*For example mine looks like 
USER=BillyAdmin
PASS=123
HOST=127.0.0.1
PORT=5432
DATABASE=BillyBooks

we do this so we do not have to hardcode our preferences to actual code but sidenote we may want a meeting discusing permanent names for these*/
*/

6.)At this point you should be ready to start the website use the command "python server.py" to get launch the site and copy the url given by ther terminal into
your choice of web browser.
/* Currently there isnt an easy way to go between pages through quick links so to traverse the files u will have to go through them declaring the
url.
For example
http://127.0.0.1:5000/searchBook
takes me to the homepage and so forth
*/

7.) Whenever you close out of the virtual environment on your terminal you can reenter using this command "./venv/Scripts/activate"

# Setting up pgAdmin for user testing
1.) You will need to install PostgresSQL https://www.postgresql.org/docs/12/tutorial-install.html 
    and pgAdmin 4 https://www.pgadmin.org/download/
    /*If unfamilair you may need to watch a guide for installation*/
2) Once you have pgadmin 4 open go to Login/Group roles right click and hit create then the role

3) In the general tab name the user what you wish, in the definition tab create a password, and in privelages set "Can login?" to true then hit save

4)Next you will want to create you database if one does not exist. Right click database and hit create then database. 

5) In general name your database what you wish then for owner add the user you created for this role. Once that is done hit save and you have
your database.

6) From this point on if you wish to test the user file you wil need to keep pgadmin on 

# SIDE NOTES 
1.) Make sure to remove unneccesasary files from main github repositories such as _pycache_ and .vscode or send them to a trash folder at least it will help with the cluter.

2.) Lets have more conventional names for files for example call files like server.py not test.py.

3.) Keep venv in your local build not the github build.

4.) Please add to this readme so we can make setup easier in the future. We will also need to add more about how to properly setup pg admin for database usage.
