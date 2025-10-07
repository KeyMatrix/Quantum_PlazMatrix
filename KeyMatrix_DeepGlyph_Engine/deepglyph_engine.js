const AudioContext = window.AudioContext || window.webkitAudioContext;
const audioCtx = new AudioContext();

export function activateGlyph(glyph) {
  const { frequency, harmonics } = glyph.resonance;
  const { shape, color, scale } = glyph.geometry;

  // 🎵 Аудио резонанс
  const base = audioCtx.createOscillator();
  base.frequency.value = frequency;
  base.type = 'sine';

  const gain = audioCtx.createGain();
  gain.gain.value = 0.2;

  base.connect(gain).connect(audioCtx.destination);
  base.start();
  setTimeout(() => base.stop(), 1000);

  // 🌀 Визуализация (в консоль, но может быть на canvas)
  console.log(`%c${glyph.glyph} ${glyph.name}`, `color: ${color}; font-size: ${scale}em`);
}
