**How to connect a CSS**

1. First, create a folder in the project called static that is separate from the template folder.
2. When a css file is created, put it inside the static folder, also name it the same as the html file so we would know.
3. In the head of the HTML file, put this code -> <link rel= "stylesheet" type= "text/css" href= "{{ url_for('static',filename='userProfile.css') }}">
4. Where it says filename='userProfile.css' , change the userProfile.css to whatever css file that is used for the HTML page, the rest stays the same.

An example of the code in 3 is in index.html, which the css file that is connected to it is welcome.css in this static folder!
