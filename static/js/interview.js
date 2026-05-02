const container = document.getElementById('q-list');
const questions = JSON.parse(container.dataset.questions || '[]');

questions.forEach((q, idx) => {
  const wrap = document.createElement('div');
  wrap.innerHTML = `<p><b>Q${idx+1}:</b> ${q}</p>
    <textarea rows="4" id="a_${idx}" placeholder="Your answer..."></textarea>
    <button type="button" onclick="startVoice(${idx})">🎤 Voice Input</button><hr>`;
  container.appendChild(wrap);
});

window.startVoice = (idx) => {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) return alert('Speech API not supported in this browser.');
  const rec = new SpeechRecognition();
  rec.lang = 'en-US';
  rec.onresult = (e) => {
    document.getElementById(`a_${idx}`).value += ' ' + e.results[0][0].transcript;
  };
  rec.start();
};

document.getElementById('submit-btn').onclick = async () => {
  const answers = questions.map((_, idx) => document.getElementById(`a_${idx}`).value);
  const res = await fetch('/interview/submit', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({answers})
  });
  const data = await res.json();
  document.getElementById('result').textContent = JSON.stringify(data, null, 2);
  setTimeout(() => window.location.href = '/dashboard/', 1300);
};
