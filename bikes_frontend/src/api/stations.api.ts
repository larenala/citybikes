import axios from 'axios';

const STATIONS_ENDPOINT = 'http://localhost:8000/stations'

export const getStations = async () => {
    try {
        const res = await axios.get(STATIONS_ENDPOINT);
        return res.data;
      } catch (error) {
        console.error(error);
      }
}