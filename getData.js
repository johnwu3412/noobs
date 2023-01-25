/*creating buttons used to get and post whatever data is put in
const getBtn = document.getElementById('get-btn');
const postBtn = document.getElementById('post-btn');

const sendHttpRequest = () => (method, url, data) => {
    const promise = new Promise((resolve, reject) => {

        const xhr = new XMLHttpRequest();
        xhr.open(method, url);
        xhr.responseType = 'json';
        xhr.onload = () => {
            resolve(xhr.response);
        };
        xhr.send(JSON.stringify(data));
    });
    return promise;
};

//function to get summoner name information
const getData = () => {
    sendHttpRequest('GET', 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/').then(responseData => {
        console.log(responseData);
    });
};

//function to send mastery information based on summoner id
const sendData = () => {
    sendHttpRequest('POST', 'https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/').then(responseData => {
        console.log(responseData);
    });
};

//creates physical website buttons that activate on click action
getBtn.addEventListener('click', getData);
postBtn.addEventListener('click', sendData);
*/

let btnGet = document.querySelector('button');
let myTable = document.querySelector('#table');
let summonerInformation = [

]
let headers = ['Champion', 'Mastery'];
btnGet.addEventListener('click', () => {
    let table = document.createElement('table');
    let headerRow = document.createElement('tr');
    headers.forEach(headerText => {
        let header = document.createElement('th');
        let textNode = document.createTextNode(headerText);
        header.appendChild(textNode);
        headerRow.appendChild(header);
    });
    table.appendChild(headerRow);
    summonerInformation.forEach(emp => {
        let row = document.createElement('tr');
        Object.values(emp).forEach(text => {
            let cell = document.createElement('td');
            let textNode = document.createTextNode(text);
            cell.appendChild(textNode);
            row.appendChild(cell);
        })
        table.appendChild(row);
    });
    myTable.appendChild(table);
});