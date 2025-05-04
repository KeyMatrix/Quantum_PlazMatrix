
const express = require('express');
const fs = require('fs');
const Discord = require('discord.js');
const app = express();
const PORT = 8080;

const coreData = JSON.parse(fs.readFileSync('OM_Gate_Core_v3.json'));

app.use(express.json());
app.use(express.static('.'));

// Resonance activation by glyph
app.post('/resonance', (req, res) => {
  const glyph = req.body.glyph;
  if (coreData.glyphs[glyph]) {
    res.json({ message: `${glyph} → ${coreData.glyphs[glyph]}` });
  } else {
    res.json({ message: 'Unknown Glyph Code' });
  }
});

// Discord Bot
const client = new Discord.Client();
const TOKEN = 'YOUR_DISCORD_BOT_TOKEN';

client.on('ready', () => {
  console.log(`Discord Bot Logged in as ${client.user.tag}`);
});

client.on('message', (msg) => {
  if (msg.content.startsWith('!resonance')) {
    const parts = msg.content.split(' ');
    const glyph = parts[1];
    if (coreData.glyphs[glyph]) {
      msg.channel.send(`Resonance: ${glyph} → ${coreData.glyphs[glyph]}`);
    } else {
      msg.channel.send('Unknown Glyph Code');
    }
  }
});

client.login(TOKEN);

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
