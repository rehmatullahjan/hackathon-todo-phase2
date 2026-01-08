import axios from 'axios';

const api = axios.create({
    baseURL: '/api', // Works for both local (via proxy/rewrites) and deployed
    headers: {
        'Content-Type': 'application/json',
    },
});

export default api;
