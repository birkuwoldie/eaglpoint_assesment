
const mockApi = async () => {
  return new Promise((resolve, reject) => {
    const succeed = Math.random() > 0.5; 
    setTimeout(() => {
      if (succeed) {
        resolve({ success: true, data: 'Mock API data' });
      } else {
        reject(new Error('Mock API failed'));
      }
    }, 500);
  });
};


const fetchWithRetry = async (apiFunction, retries = 5, delayMs = 1000) => {
  for (let attempt = 1; attempt <= retries; attempt++) {
    try {
      console.log(`Attempt ${attempt}...`);
      const result = await apiFunction();
      console.log('Success!');
      return result;
    } catch (err) {
      console.log(`Attempt ${attempt} failed: ${err.message}`);
      if (attempt < retries) {
        console.log(`Retrying in ${delayMs}ms...`);
        await new Promise((res) => setTimeout(res, delayMs));
      } else {
        throw new Error(`Failed after ${retries} retries: ${err.message}`);
      }
    }
  }
};

// Test the fetcher
(async () => {
  try {
    const data = await fetchWithRetry(mockApi, 5, 1000);
    console.log('Fetched data:', data);
  } catch (error) {
    console.error('All retries failed:', error.message);
  }
})();
