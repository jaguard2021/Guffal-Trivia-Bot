# **Guffal Trivia Bot**

**Guffal Trivia Bot** is a Discord Trivia bot built using Python and the `discord.py` library. This bot is designed to engage users with trivia questions about Guffal.

## **How to Use the Bot**

### **Setting Up the Bot:**
1. **Prefix:**
   - Users can change the bot's prefix by changing `command_prefix` at the top of the `bot.py` file. For example:
     ```python
     bot = commands.Bot(command_prefix='?')
     ```

2. **Token:**
   - Make sure to replace `'YOUR_TOKEN'` with a valid bot token in the bottom part of the `bot.py` code.
   - If the bot cannot access the token correctly, please check the permissions and token for your Discord.

### **Running the Bot:**
- To run the bot, use the following command:
  ```bash
  bot.run('YOUR_TOKEN')

### **Interacting with the Bot:**
Users can start a trivia game by typing the command !trivia.
To check the current score, users can type !score.
