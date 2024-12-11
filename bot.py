import discord
from discord.ext import commands
import json
import random

# Mengatur prefix untuk perintah bot
bot = commands.Bot(command_prefix='!')

# Muat file questions.json
with open('questions.json') as f:
    questions = json.load(f)

# Variable untuk menyimpan skor
scores = {}

# Memulai permainan trivia
@bot.event
async def on_ready():
    print(f'Bot {bot.user} sudah siap!')

# Menjalankan perintah !trivia untuk memulai permainan
@bot.command()
async def trivia(ctx):
    global questions
    # Pilih pertanyaan secara acak
    question_data = random.choice(questions)
    question_text = question_data['question']
    options = "\n".join(question_data['options'])
    
    # Kirim pertanyaan ke saluran Discord
    await ctx.send(f"**Trivia:**\n{question_text}\n{options}")

    # Menunggu jawaban pengguna
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.upper() in ['A', 'B', 'C']
    
    try:
        # Tunggu sampai pengguna menjawab
        msg = await bot.wait_for('message', timeout=30.0, check=check)
        answer = question_data['answer']

        # Memeriksa jawaban pengguna
        if msg.content.upper() == answer:
            await ctx.send("Benar! 🎉")
            # Menambah skor jika benar
            scores[ctx.author] = scores.get(ctx.author, 0) + 1
        else:
            await ctx.send(f"Salah! Jawaban yang benar adalah {answer}.")

    except asyncio.TimeoutError:
        await ctx.send("Waktu habis! Jangan khawatir, ini masih belajar!")

# Menjalankan perintah !score untuk melihat skor
@bot.command()
async def score(ctx):
    user_score = scores.get(ctx.author, 0)
    await ctx.send(f"{ctx.author.display_name}, skor saat ini: {user_score}")

# Menjalankan bot dengan token
bot.run('YOUR_TOKEN')

