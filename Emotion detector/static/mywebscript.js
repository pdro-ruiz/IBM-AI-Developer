let RunSentimentAnalysis = () => {
    const textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                const response = JSON.parse(xhttp.responseText);
                document.getElementById("system_response").innerHTML = `
                    <pre>${JSON.stringify(response, null, 2)}</pre>`;
            } else {
                document.getElementById("system_response").innerHTML = `
                    <p style="color: red;">Error: ¡Texto inválido! ¡Por favor, inténtalo de nuevo!</p>`;
            }
        }
    };

    xhttp.open("GET", `/emotionDetector?textToAnalyze=${encodeURIComponent(textToAnalyze)}`, true);
    xhttp.send();
};
