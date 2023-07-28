# Создание вашего первого Discord бота Anti-Spam

_!Заказать Discord бота: (https://t.me/admirall_times)!_

![bots-de-economia-discord-768x432](https://user-images.githubusercontent.com/128980327/232897933-38097a7f-e8eb-4b6f-b505-497d4b9508bd.jpg)

**Шаг 1: Создание нового Discord бота и получение токена бота.**
1. Перейдите на сайт разработчика Discord (https://discord.com/developers/applications).
2. Войдите в свою учетную запись или создайте новую.
3. Нажмите кнопку "New Application" (Новая программа) и введите название вашего бота.
4. Перейдите на вкладку "Bot" (Бот) в меню слева.
5. Нажмите кнопку "Add Bot" (Добавить бота) и подтвердите создание бота.
6. В разделе "Token" (Токен) нажмите кнопку "Copy" (Скопировать) для сохранения токена бота. Обратите внимание, что этот токен должен храниться в секрете и не может быть размещен в открытом коде или передан кому-либо еще.

**Шаг 2: Приглашение бота на ваш сервер Discord.**
1. Вернитесь на вкладку "General Information" (Общая информация) вашей программы.
2. Найдите ваш Client ID (идентификатор клиента) и скопируйте его.
3. Войдите на ваш Discord-сервер и перейдите на вкладку "OAuth2" в настройках сервера.
4. В разделе "OAuth2 URL Generator" (Генератор URL для OAuth2) выберите опцию "bot".
5. Под опцией "Scopes" (Сферы) выберите "bot".
6. Под опцией "Bot Permissions" (Права бота) выберите необходимые права для вашего бота (например, "Read Messages", "Send Messages", "Manage Messages" и т. д., в зависимости от того, какие функции Anti-Spam вы планируете использовать).
7. Скопируйте сгенерированный URL-адрес OAuth2 и откройте его в веб-браузере.
8. Выберите сервер, на который вы хотите пригласить вашего бота, и нажмите "Authorize" (Авторизовать).

**Шаг 3: Написание кода для бота Anti-Spam.**
Для реализации бота Anti-Spam вам понадобится библиотека, которая предоставляет удобный интерфейс для работы с API Discord. Например, вы можете использовать библиотеку discord.py для Python.

Вот пример кода для базового бота Anti-Spam на discord.py:

```python
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Создание словаря для хранения счетчиков сообщений пользователей
spam_counter = {}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author.bot:
        return  # Игнорировать сообщения от ботов

    # Проверка, есть ли автор сообщения в словаре, и увеличение счетчика на 1
    if message.author.id in spam_counter:
        spam_counter[message.author.id] += 1
    else:
        spam_counter[message.author.id] = 1

    # Если пользователь отправляет более 5 сообщений подряд, удалить их
    if spam_counter[message.author.id] > 5:
        await message.delete()
        await message.channel.send(f'{message.author.mention}, перестаньте спамить!')

    await bot.process_commands(message)

@bot.command(name='очистить_спам')
async def clear_spam_counter(ctx):
    # Команда для очистки счетчиков спама
    spam_counter.clear()
    await ctx.send('Счетчики спама были очищены.')

bot.run('YOUR_BOT_TOKEN')
```

**Шаг 4: Запуск бота Anti-Spam.**
Запустите вашего бота, выполнив код из файла через командную строку или разместив его на хостинговом сервере. Когда бот будет работать, он начнет отслеживать сообщения и реагировать на спам.

**Обратите внимание, что этот пример является базовым и не включает дополнительные функции Anti-Spam, такие как проверка сообщений с идентичным текстом или использование алгоритмов машинного обучения для обнаружения спама. Вы можете расширить этот код в зависимости от ваших потребностей и требований вашего Discord-сервера.**
