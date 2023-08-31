console.log('Hello it me');
pageLoader();

// Function to load our page and set event listeners
function pageLoader(){
    console.log('Loading the page with functionality...');

    const buttons = document.getElementsByClassName('play-button');
    for (let btn of buttons){
        btn.addEventListener('click', changeView);
    };
   
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