import axios from 'axios';

// Détection dynamique de l'URL pour switcher entre le PC local et PythonAnywhere
const API_BASE_URL = window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1"
    ? "http://127.0.0.1:8000/api/"
    : "https://mooniejeon23.pythonanywhere.com/api/";

const api = axios.create({
    baseURL: API_BASE_URL,
});

export const projectAPI = {
    getAll: () => api.get('projects/'),
};

export const skillAPI = {
    getAll: () => api.get('skills/'),
};

export const experienceAPI = {
    getAll: () => api.get('experience/'),
};

export default api;