import os
import sys
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, SUDO_USERS

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("Minggu", 60 * 60 * 24 * 7),
    ("Hari", 60 * 60 * 24),
    ("Jam", 60 * 60),
    ("Menit", 60),
    ("Detik", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


#@Client.on_message(filters.command(["ping"], prefixes=f"{HNDLR}"))
#async def ping(client, m: Message):
#    await m.delete()
#    start = time()
#    current_time = datetime.utcnow()
#    m_reply = await m.reply_text("⚡")
#    delta_ping = time() - start
#    uptime_sec = (current_time - START_TIME).total_seconds()
#    uptime = await _human_time_duration(int(uptime_sec))
#    await m_reply.edit(
#        f"<b>🏓 PONG</b> `{delta_ping * 1000:.3f} ms` \n<b>⏳ AKTIF</b> - `{uptime}`"
#    )


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["restart"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("APE LU")
    await loli.edit("TUNGGU BENTAR YA BANGSAT")
    await loli.edit("GUA CUMAN RESTART")
    await loli.edit("BENTARAN DOANG KOK")
    await loli.edit("KALAU GA SABAR")
    await loli.edit("MATI AJA GAPAPA")
    await loli.edit("ANEH BAT LU ")
    await loli.edit("DAH TOD GUA MAU RESTART DLU")
    await loli.edit("BYE")
    await loli.edit("**✅ Userbot Di Mulai Ulang**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>👋 Hallo {m.from_user.mention}!

📝 DAFTAR PERINTAH MUSIC PLAYER 📝
💡 UNTUK SEMUA ANGGOTA GRUP 💡
• {HNDLR}play (judul lagu) - untuk memutar lagu yang anda inginkan 
• {HNDLR}play (balas ke audio file) - untuk memutar lagu yang di minta melalui audio yang dibalas
• {HNDLR}play (link youtube) - untuk memutar lagu yang di minta melalui url youtube
• {HNDLR}song (judul lagu) - untuk mendownload lagu

💡 UNTUK SEMUA ADMIN GRUP 💡
• {HNDLR}pause - untuk menjeda pemutaran
• {HNDLR}resume - untuk melanjutkan pemutaran
• {HNDLR}end - untuk menghentikan pemutaran
• {HNDLR}skip - untuk memutar lagu berikutnya yang ada didalam antrian

📝 DAFTAR PERINTAH VIDEO PLAYER 📝
💡 UNTUK SEMUA ANGGOTA GRUP 💡
• {HNDLR}vplay (judul video) - untuk memutar video yang anda inginkan 
• {HNDLR}vplay (balas ke video file) - untuk memutar video yang di minta melalui audio yang dibalas
• {HNDLR}vplay (link youtube) - untuk memutar video yang di minta melalui url youtube
• {HNDLR}vsong (judul video) - untuk mendownload video

💡 UNTUK SEMUA ADMIN GRUP 💡
• {HNDLR}vpause - untuk menjeda pemutaran
• {HNDLR}vresume - untuk melanjutkan pemutaran
• {HNDLR}vstop - untuk menghentikan pemutaran
• {HNDLR}vskip - untuk memutar video berikutnya yang ada didalam antrian

💡SUDO USERS COMMANDS 💡
Perintah pengguna sudo:
• {HNDLR}clean -> Membersihkan file temp.
• {HNDLR}restartMusic -> Restart musik.
• {HNDLR}block -> blokir pengguna dari menggunakan musik.
• {HNDLR}unblock -> Buka blokir pengguna yang diblokir dari menggunakan musik.
• {HNDLR}eval or /sh -> dapatkan akses utama musik.
• {HNDLR}joinassistant -> Assistant akan bergabung dengan grup obrolan.
• {HNDLR}leavebot -> MusicBot akan meninggalkan grup obrolan yang diberikan.
• {HNDLR}leaveassistant -> assistant akan meninggalkan grup obrolan.
• {HNDLR}blacklistchat -> Daftar hitam Obrolan dari menggunakan musik.
• {HNDLR}whitelistchat -> WhiteList obrolan.
• {HNDLR}karmaon atau /karmaoff -> Mengaktifkan atau menonaktifkan fungsi karma.
• {HNDLR}speedteston atau /speedtestoff -> Mengaktifkan atau menonaktifkan fungsi speedtest.
• {HNDLR}update -> Pembaruan musik.
• {HNDLR}broadcast -> Broadcast pesan di semua obrolan musik yang disajikan.


• Jika Terjadi Kesalahan Silahkan Hubungi Saya @IDnyaKosong Selamat Bermusik</b>
"""
    await m.reply(HELP)



