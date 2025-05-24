const { Client, GatewayIntentBits } = require('discord.js');
const { getAIAnswer } = require('./manage_json.js');

const client = new Client({ intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent] });

client.on('messageCreate', (msg) => {
  if (msg.content.startsWith('!ask')) {
    const q = msg.content.replace('!ask', '').trim();
    const answer = getAIAnswer(q);
    msg.reply(answer);
  }
});

client.login('YOUR_DISCORD_TOKEN');
