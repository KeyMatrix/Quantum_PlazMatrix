const fs = require('fs');
let core = JSON.parse(fs.readFileSync('OM_Gate_Core_v3.json', 'utf-8'));

function getAIAnswer(query) {
  return `[Resonance] Answer to "${query}" received via Core12.`;
}

function updateCoreState(data) {
  core = { ...core, ...data };
  fs.writeFileSync('OM_Gate_Core_v3.json', JSON.stringify(core, null, 2));
}

module.exports = { getAIAnswer, updateCoreState };
