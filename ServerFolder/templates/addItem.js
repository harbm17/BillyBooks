const toggleBtn = document.querySelector('#toggleBtn');
const divList = document.querySelector('.booksLiked');

toggleBtn.addEventListener('click', () => {
    if(divList.style.display == 'none')
    {
        divList.style.display = 'block';
        toggleBtn.innerHTML = 'Hide List';
    }
    else
    {
        divList.style.display = 'none';
        toggleBtn.innerHTML = 'Show List';
    }
});

/*add list item*/
const addBook = document.querySelector('#addBook');
const addBtn = document.querySelector('#addBtn');

function addLists() {
    if (addInput.value === '') {
      alert('Enter the book please!!!');
    } else {
      const ul = divList.querySelector('ul');
      const li = document.createElement('li');
      li.innerHTML = addInput.value;
      addInput.value = '';
      ul.appendChild(li);
      createBtn(li);
    }
  }

addBtn.addEventListener('click', ()=> {
    addLists();
});

addInput.addEventListener('keyup', (event) => {
    if(event.which === 13) {
      addLists();
    }
  });

for (var i = 0; i < lis.length; i++) {
    createBtn(lis[i]);
}