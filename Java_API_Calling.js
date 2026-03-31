  const apiEndpoint = 'https://ogsmke4g5c3wfizbunogvrkgyi0kzdwa.lambda-url.eu-north-1.on.aws/';

    async function updateCounter() {
        try {
            let response = await fetch(apiEndpoint);
            let data = await response.json();
            document.getElementById('counter').innerText = `Views: ${data.count}`;
        } catch (error) {
            console.error("Oops! Couldn't fetch the visitor count:", error);
            document.getElementById('counter').innerText = "View count unavailable";
        }
    }

    updateCounter();