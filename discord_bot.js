const { Client, GatewayIntentBits } = require('discord.js');
const client = new Client({ intents: [GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent] });

client.on('messageCreate', (message) => {
  if (message.author.bot) return;
  if (message.content.startsWith('!ask')) {
    const query = message.content.slice(4).trim();
    const answer = aiAnswer(query);
    message.reply(`AI: ${answer}`);
  }
});

client.login('YOUR_DISCORD_BOT_TOKEN');