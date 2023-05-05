import axios from 'axios';

export const getApi = () => {
    return axios.get('http://127.0.0.1:8000/')
};