import os
import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user} telah online dan siap menerima perintah slash!")

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='selamat-datang')
    if channel:
        await channel.send(f"Selamat datang {member.mention} di server Sejarah SMAN 12 Semarang! 🎉")
    else:
        print("Channel 'selamat-datang' tidak ditemukan.")

@bot.tree.command(name="hello", description="Menyapa pengguna")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Halo, {interaction.user.name}! Selamat datang!")

@bot.tree.command(name="pengumuman", description="Lihat channel pengumuman")
async def pengumuman(interaction: discord.Interaction):
    await interaction.response.send_message("Cek channel #📢pengumuman", ephemeral=True)

@bot.tree.command(name="materi", description="Lihat materi pelajaran")
async def materi(interaction: discord.Interaction):
    await interaction.response.send_message("Materi ada di channel #📚materi", ephemeral=True)

@bot.tree.command(name="bertanya_paknastain", description="Mention Pak Nastain untuk bertanya")
async def tanya(interaction: discord.Interaction):
    pak_nastain_id = 123456789012345678  # Ganti ID-nya
    await interaction.response.send_message(f"Silakan bertanya ke <@{pak_nastain_id}>")

@bot.tree.command(name="motivasi", description="Dapatkan motivasi hari ini")
async def motivasi(interaction: discord.Interaction):
    await interaction.response.send_message("Tetap semangat! Kamu hebat!")

@bot.tree.command(name="pantun", description="Dapatkan pantun menarik")
async def pantun(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Jalan-jalan ke kota Blora,\nBeli sate di pinggir jalan.\nBelajar sejarah janganlah lara,\nKarena ilmu menuntun masa depan.")

TOKEN = os.environ.get("DISCORD_TOKEN")
if not TOKEN:
    print("Token bot tidak ditemukan! Pastikan DISCORD_TOKEN sudah diatur.")
else:
    bot.run(TOKEN)