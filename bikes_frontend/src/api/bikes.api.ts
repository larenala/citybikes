import axios from 'axios';

const BIKES_ENDPOINT = 'http://localhost:8000'

export const getBikeData = async () => {
    try {
        return await axios.get(BIKES_ENDPOINT);
      } catch (error) {
        console.error(error);
      }
}