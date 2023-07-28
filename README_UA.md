Створення вашого першого Discord-бота Anti-Spam



![bots-de-economia-discord-768x432](https://user-images.githubusercontent.com/128980327/232897933-38097a7f-e8eb-4b6f-b505-497d4b9508bd.jpg)

*Крок 1: Створення нового Discord-бота і отримання токену бота.*
1. Перейдіть на сайт розробника Discord (https://discord.com/developers/applications).
2. Увійдіть в свій обліковий запис або створіть новий.
3. Натисніть кнопку "New Application" (Нова програма) і введіть назву свого бота.
4. Перейдіть на вкладку "Bot" (Бот) у меню зліва.
5. Натисніть кнопку "Add Bot" (Додати бота) і підтвердьте створення бота.
6. В розділі "Token" (Токен) натисніть кнопку "Copy" (Скопіювати) для збереження токена бота. Зверніть увагу, що цей токен повинен зберігатись у таємниці, і не може бути розміщений у відкритому коді або відправлений комусь іншому.

*Крок 2: Запрошення бота на свій сервер Discord.*
1. Поверніться на вкладку "General Information" (Загальна інформація) вашої програми.
2. Знайдіть ваш Client ID (ідентифікатор клієнта) і скопіюйте його.
3. Увійдіть на свій Discord-сервер і перейдіть до вкладки "OAuth2" у налаштуваннях сервера.
4. У розділі "OAuth2 URL Generator" (Генератор URL для OAuth2) виберіть опцію "bot".
5. Під опцією "Scopes" (Сфери) оберіть "bot".
6. Під опцією "Bot Permissions" (Права бота) виберіть необхідні права для свого бота (наприклад, "Read Messages", "Send Messages", "Manage Messages" тощо, залежно від того, які функції Anti-Spam ви плануєте використовувати).
7. Скопіюйте згенерований URL-адресу OAuth2 і відкрийте його у веб-браузері.
8. Виберіть сервер, на який ви хочете запросити свого бота, і натисніть "Authorize" (Авторизувати).

*Крок 3: Написання коду для бота Anti-Spam.*
Для реалізації бота Anti-Spam вам знадобиться бібліотека, яка надає зручний інтерфейс для роботи з API Discord. Наприклад, ви можете використовувати бібліотеку discord.py для Python.

Ось приклад коду для базового бота Anti-Spam на discord.py:

```python
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Створення словника для зберігання лічильників повідомлень користувачів
spam_counter = {}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author.bot:
        return  # Ігнорувати повідомлення від ботів

    # Перевірка, чи автор повідомлення є в словнику, і збільшення лічильника на 1
    if message.author.id in spam_counter:
        spam_counter[message.author.id] += 1
    else:
        spam_counter[message.author.id] = 1

    # Якщо користувач надіслав більше 5 повідомлень підряд, видалити їх
    if spam_counter[message.author.id] > 5:
        await message.delete()
        await message.channel.send(f'{message.author.mention}, перестаньте спамити!')



    await bot.process_commands(message)

@bot.command(name='очистити')
async def clear_spam_counter(ctx):
    # Команда для очищення лічильників спаму
    spam_counter.clear()
    await ctx.send('Лічильники спаму були очищені.')

bot.run('YOUR_BOT_TOKEN')
```

*Крок 4: Запуск бота Anti-Spam.*
Запустіть свого бота, виконавши файл з кодом з командного рядка або розмістивши його на хостинговому сервері. Коли бот буде запущений, він почне слідкувати за повідомленнями і реагувати на спам.

**Зверніть увагу, що цей приклад лише базовий і не містить додаткових функцій анти-спаму, таких як перевірка на спам повідомлень з однаковим текстом або використання алгоритмів машинного навчання для виявлення спаму. Ви можете розширити цей код залежно від вашої потреби і вимог вашого Discord-сервера.**
