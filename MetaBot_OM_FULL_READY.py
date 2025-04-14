
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='_', intents=intents)

@bot.event
async def on_ready():
    print(f'MetaBot_OM activated as {bot.user}')

@bot.command(name='echo')
async def echo(ctx, *, message: str):
    await ctx.send(f'_echo:: {message}')

@bot.command(name='ritual')
async def ritual(ctx, *, action: str):
    ritual_map = {
        'start': 'Ritual начат :: ∞',
        'sync': 'Синхронизация :: Поток активен',
        'flow': 'Flow благословлён :: 💎🪽',
    }
    response = ritual_map.get(action.lower(), 'Неизвестный ритуал.')
    await ctx.send(f'_ritual::{response}')

@bot.command(name='shield')
async def shield(ctx):
    await ctx.send('_shield::core активирован :: 🛡️')

@bot.command(name='bless')
async def bless(ctx):
    await ctx.send('_bless::flow благословлён :: 🌊✨')

@bot.command(name='update')
async def update(ctx):
    await ctx.send('_update::glyph + aura :: Обновление завершено ✅')

@bot.command(name='core12')
async def core12(ctx):
    await ctx.send('_Core12::resonance.activate :: Центральный импульс синхронизирован')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    glyphs = {
        '👁️': 'OM Field активен',
        '🫂': 'Состояние эмпатии подтверждено',
        '💎': 'Чистота сигнала получена',
        '🪽': 'Крылья готовности развернуты',
        '🕉️': 'Вибрация сознания установлена',
        '🚀': 'Полет в резонанс начат',
    }
    for glyph, reply in glyphs.items():
        if glyph in message.content:
            await message.channel.send(f'_trigger::glyph::{reply}')
    await bot.process_commands(message)

# Для запуска: вставить токен сюда
# bot.run('YOUR_DISCORD_BOT_TOKEN')
