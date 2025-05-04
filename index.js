
document.addEventListener('DOMContentLoaded', () => {
  const statusDiv = document.getElementById('status');
  const resonanceBtn = document.getElementById('resonance-btn');

  resonanceBtn.addEventListener('click', () => {
    const code = document.getElementById('glyph-code').value;
    fetch('/resonance', {
      method: 'POST,
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ glyph: code })
    })
      .then(res => res.json())
      .then(data => statusDiv.textContent = `Resonance: ${data.message}`)
      .catch(err => {
        statusDiv.textContent = 'Error activating resonance.';
        console.error(err);
      });
  });
});
