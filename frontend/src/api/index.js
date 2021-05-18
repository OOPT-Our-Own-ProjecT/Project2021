import axios from 'axios';

function registerUser(userData){
    console.log(userData);
    const url = 'http://localhost:8080/account/signUp';
    return axios.post(url, userData);
}

export { registerUser };