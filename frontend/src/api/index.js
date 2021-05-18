import axios from 'axios';

function registerUser(userData){
    const url = 'http://localhost:8081/signUp';
    return axios.post(url, userData);
}

export { registerUser };