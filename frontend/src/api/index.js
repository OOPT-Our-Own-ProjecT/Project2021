import axios from 'axios';

function registerUser(userData){
    const url = 'http://localhost:8000/account/signUp/';
    return axios.post(url, userData);
}

function getUserAll(){
    const url = 'http://localhost:8000/account/getUserAll/';
    return axios.get(url);
}

function deleteUser(userData){
    const url = 'http://localhost:8000/account/deleteUser/';
    return axios.post(url, userData);
}

export { registerUser , getUserAll, deleteUser};