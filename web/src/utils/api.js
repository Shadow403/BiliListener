import axios from 'axios'


export const get_hub = async () => {
  try {
    const ret = await axios.get('/api/web/hub')
    return ret.data
  } catch (error) {
    console.error('[Fetch HUB Error]: ', error)
    throw error
  }
}

export const get_uids = async () => {
  try {
    const ret = await axios.get('/api/v1/info/uids')
    return ret.data
  } catch (error) {
    console.error('[Fetch UIDS Error]: ', error)
    throw error
  }
}

export const get_time = async () => {
  try {
    const ret = await axios.get('/api')
    return ret.data
  } catch (error) {
    console.error('[Fetch TIME Error]: ', error)
    throw error
  }
}


export const get_listening = async () => {
  try {
    const ret = await axios.get('/api/v1/info/listening')
    return ret.data
  } catch (error) {
    console.error('[Fetch LISTENING Error]: ', error)
    throw error
  }
}

export const get_total = async () => {
  try {
    const ret = await axios.get('/api/v1/stats/total')
    return ret.data
  } catch (error) {
    console.error('[Fetch TOTAL Error]: ', error)
    throw error
  }
}

export const get_config_by_uid = async (uid) => {
  try {
    const ret = await axios.get(`/api/v2/live/config/${uid}`);
    return ret.data;
  } catch (error) {
    console.error('[Fetch CONFIG_UID Error]: ', error);
    throw error;
  }
}

export const get_stats_main = async (type) => {
  try {
    const ret = await axios.get(`/api/v1/stats/main?type=${type}`);
    return ret.data;
  } catch (error) {
    console.error('[Fetch STATS_MAIN Error]: ', error);
    throw error;
  }
}
