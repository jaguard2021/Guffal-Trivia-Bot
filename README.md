Guffal Trivia Bot
This repository contains a Discord Trivia Bot built using Python and the discord.py library. The bot is designed to engage users with trivia questions about Guffal.

How to Use the Bot
Set Up the Bot:

Prefix: Users can change the bot's prefix by changing command_prefix at the top of the bot.py file. For example, if they want to use ? as the prefix, they need to change it to:
python
Copy code
bot = commands.Bot(command_prefix='?')
Token: Make sure to replace 'YOUR_TOKEN' with a valid bot token in the bottom part of the bot.py code.
If the bot cannot access the token correctly, please check the permissions and token for your Discord.
Running the Bot:

To run the bot, use the following command:
bash
Copy code
bot.run('YOUR_TOKEN')
Interacting with the Bot:

Users can start a trivia game by typing the command !trivia.
To check the current score, users can type !score.
Files in This Repository:

bot.py: Main bot script.
questions.json: Contains trivia questions.
README.md: This file.
Additional Information:
Ensure you have the discord.py library installed by running:

bash
Copy code
pip install discord.py
To set up your bot’s token:

Create a bot on the Discord Developer Portal and obtain a token.
Replace YOUR_TOKEN with the token you receive.
If you encounter any issues, refer to the bot.py code comments or the README.md for guidance.
