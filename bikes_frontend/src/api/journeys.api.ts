import axios from 'axios';

const JOURNEYS_ENDPOINT = 'http://localhost:8000/journeys'

export const getJourneyData = async () => {
    try {
        const res = await axios.get(JOURNEYS_ENDPOINT);
        return res.data;
      } catch (error) {
        console.error(error);
      }
}