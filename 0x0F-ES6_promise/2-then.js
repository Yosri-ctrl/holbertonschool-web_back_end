export default function handleResponseFromAPI(promise) {
	promise.then(() => ({
		status: 200,
      	body: 'success',
	}));
	promise.catch(() => Error());
	promise.finally(() => console.warn('Got a response from the API'));
	return promise;
}
