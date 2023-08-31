console.log('Hello it me');
pageLoader();

// Function to load our page and set event listeners
function pageLoader(){
    console.log('Loading the page with functionality...');

    const buttons = document.getElementsByClassName('play-button');
    for (let btn of buttons){
        btn.addEventListener('click', changeView);
    };
    
    const findCardForm = document.querySelector('#find-cards-form');
    findCardForm.addEventListener('submit', (e) => findCards(e, 1));
}

// Create a function to make this a Single Page App (SPA) by swapping visible divs
function changeView(event){
    // Turn off the element(s) that are visible
    const toTurnOff = document.getElementsByClassName('is-visible');
    for (let element of toTurnOff){
        console.log('Turning off', element);
        element.classList.replace('is-visible', 'is-invisible');
    }

    // Turn on the element based on the link that was clicked
    let idToTurnOn = event.target.name;
    const toTurnOn = document.getElementById(idToTurnOn);
    toTurnOn.classList.replace('is-invisible', 'is-visible');
}

function findCards(event, pageNumber){
    event.preventDefault();
    const cardName = document.getElementsByName('card')[0].value;
    console.log(`Looking for countries with ${cardName}...`);
    const url = `https://db.ygoprodeck.com/api/v7/cardinfo.php?name=${cardName.replace(' ', '%20')}`;
    console.log(url)

    fetch(url)
        .then(response => response.json())
        .then(data => {
            if (Object.keys(data).length){
                console.log('moving on')
                displayCards(data)}
            else{
                console.log('No length')
            }
        })
        .catch(err => console.error(err))
}

function displayCards(data){
    let table = document.getElementById('card-table');
    
    let card = data.data[0]
    let newCol = document.createElement('div');
    newCol.classList.add('col-3')
    table.append(newCol);

    let divider = document.createElement('div');
    divider.classList.add('card', 'm-3', 'border-3', 'border-dark');
    newCol.append(divider);

    const td = document.createElement('td');
    td.innerHTML = `<h2>${card.name}</h2>`;
    td.classList.add('text-center', 'display-4')
    divider.append(td);
    
    let divider2 = document.createElement('div');
    divider2.classList.add('card-body', 'm-3');
    divider.append(divider2);
    newDataCell(divider2, 'Description: ' + card.desc);
    
}

// Helper function to create a new data cell for table
function newDataCell(tr, value){
    let td = document.createElement('td');
    td.innerText = value ?? '-';
    tr.append(td);

    
    let b = document.createElement('b');
    tr.append(b);
}

// Helper function to create new data where an image needs to be displayed
function newDataCellImg(tr, value){
    let img = document.createElement('img');
    img.src = value ?? '...'
    if(img.src == "..."){
        img.classList.add('card-img-top')
    }
    img.classList.add('img-fluid', 'p-1', 'width');
    tr.append(img);
}

// Helper function to clear the brewery table
function clearTable(table){
    table.innerHTML = '';
    const buttonsToClear = document.querySelectorAll('.prev-next-btn');
    for (let btn of buttonsToClear){
        btn.remove()
    }
}
