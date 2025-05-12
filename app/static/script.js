async function sendPrompt() {
    const prompt = document.getElementById('prompt').value;
    const responseDiv = document.getElementById('response');
    responseDiv.innerText = "Consulting the spirits...";

    const res = await fetch('/chat/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: prompt })
    });

    const data = await res.json();
    responseDiv.innerText = data.reply || "No response.";
}
