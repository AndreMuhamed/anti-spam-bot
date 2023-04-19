import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!') # задаємо префікс для команд

@bot.event
async def on_ready():
    print(f'{bot.user.name} з\'явився в Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user: # перевірка на те, щоб бот не видаляв свої власні повідомлення
        return

    if message.content.startswith('!'): # перевірка на те, щоб бот не видаляв команди
        return

    if len(message.content) > 10: # перевірка на довжину повідомлення (можна змінити це значення)
        await message.delete()
        await message.channel.send(f'{message.author.mention}, ваше повідомлення було видалено через підозру на спам або флуд.')

bot.run('TOKEN') # тут потрібно вставити токен вашого бота
пекркпртип
