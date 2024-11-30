let recognition;
let micBtn = document.getElementById('micBtn');
let commandStatus = document.getElementById('commandStatus');
let responseArea = document.getElementById('responseArea');

// Initialize the Speech Recognition API
if (window.SpeechRecognition || window.webkitSpeechRecognition) {
    recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'en-US';
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.onstart = function () {
        commandStatus.textContent = "Listening...";
    };

    recognition.onspeechend = function () {
        commandStatus.textContent = "Stopped listening.";
    };

    recognition.onerror = function (event) {
        commandStatus.textContent = "Error occurred. Please try again.";
    };

    recognition.onresult = function (event) {
        let command = event.results[0][0].transcript.toLowerCase();
        commandStatus.textContent = `You said: ${command}`;
        sendCommandToBackend(command);
    };
} else {
    commandStatus.textContent = "Speech recognition is not supported in this browser.";
}

// Start speech recognition when the microphone button is clicked
function startRecognition() {
    recognition.start();
}

// Send the recognized command to Flask server for processing
function sendCommandToBackend(command) {
    fetch(`/process-command/${command}`)
        .then(response => response.json())
        .then(data => {
            let response = data.response || data.error;
            responseArea.textContent = response;
            speak(response);  // Use the speech synthesis to reply
        })
        .catch(error => {
            responseArea.textContent = "Error: " + error;
        });
}

// Speech synthesis to give a voice response
function speak(text) {
    let speech = new SpeechSynthesisUtterance(text);
    speech.lang = 'en-US';
    window.speechSynthesis.speak(speech);
}
