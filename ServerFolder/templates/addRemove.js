function addBook(){
  var ul = document.getElementById("bookList");
  var book = document.getElementById("book");
  var li = document.createElement("li");
  li.setAttribute('id', book.value);
  li.appendChild(document.createTextNode(book.value));
  ul.appendChild(li);
}

function removeBook(){
  var ul = document.getElementById("bookList");
  var book = document.getElementById("book");
  var li = document.getElementById(book.value);
  ul.removeChild(li);
}

function addAuthor(){
  var ul = document.getElementById("authorList");
  var author = document.getElementById("author");
  var li = document.createElement("li");
  li.setAttribute('id', author.value);
  li.appendChild(document.createTextNode(author.value));
  ul.appendChild(li);
}

function removeAuthor(){
  var ul = document.getElementById("authorList");
  var author = document.getElementById("author");
  var li = document.getElementById(author.value);
  ul.removeChild(li);
}

function addGenre(){
  var ul = document.getElementById("genList");
  var genre = document.getElementById("genre");
  var li = document.createElement("li");
  li.setAttribute('id', genre.value);
  li.appendChild(document.createTextNode(genre.value));
  ul.appendChild(li);
}

function removeGenre(){
  var ul = document.getElementById("genList");
  var genre = document.getElementById("genre");
  var li = document.getElementById(genre.value);
  ul.removeChild(li);
}