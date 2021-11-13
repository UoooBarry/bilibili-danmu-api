import axios from 'axios';

const BASE_URL = process.env.VUE_APP_API_BASE_URL || 'http://localhost:6677';

const service = axios.create({
  baseURL: `${BASE_URL}`,
  timeout: 5000
});

const onSuccess = (response) => {
  if (!String(response.headers['content-type']).includes('application/json')) {
    return response;
  }

  return response.data
};

service.interceptors.response.use(onSuccess);


export default service;