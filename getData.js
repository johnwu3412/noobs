//creating buttons used to get and post whatever data is put in
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