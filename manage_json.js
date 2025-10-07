const fs = require('fs');
let coreState = JSON.parse(fs.readFileSync('OM_Gate_Core_v3.json', 'utf-8'));

function updateCoreState(newData) {
  coreState = { ...coreState, ...newData };
  fs.writeFileSync('OM_Gate_Core_v3.json', JSON.stringify(coreState, null, 2));
}