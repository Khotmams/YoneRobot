# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from DaisyXMusic.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = "**⚛️ hello [{}](tg://user?id={})! selamat datang di 𝙎𝙋𝙔 𝙈𝙐𝙎𝙄𝘾 𝘽𝙍𝙊𝙒࿐.**\n\n⚛️ aku spy music bot, aku bisa memutar lagu di dalam voice chat group dan channel kamu.\n\n⚛️ ketik /help untuk bantuan dan informasi lengkap yah."
      HELP_MSG = [
        ".",
f"""
**🌹 hai, welcome back to {PROJECT_NAME}

🌹 {PROJECT_NAME} dapat memutar musik di voice chat group dan channel kamu.

🌹 asisstant bot ➠ @{ASSISTANT_NAME}\n\ntekan next dibawah untuk langkah selanjutnya.**
""",

f"""
**🍂 pengaturan untuk grup:**

1) bot harus jadi admin dan diberi izin manage voice chat.
2) nyalakan vcg atau voice chat nya sebelum req music.
3) lalu ketik /play [judul lagu] untuk memutar music.
4) jika asisstant bergabung ke vcg silahkan menikmati music nya, jika tidak, tambahkan @{ASSISTANT_NAME} ke dalam grup lalu coba lagi.

**🍂 pengaturan untuk channel:**

1) jadikan saya admin di channel.
2) ketik /userbotjoinchannel di grup yang dihubungkan dengan channel.
3) lalu ketikkan perintah dibawah ini di dalam grup yang dihubungkan ke channel.

**🌻 commands.**

**🍂 perintah memutar lagu:**

- /play: putar lagu dengan judul/nama lagu.
- /play [link youtube] : putar lagu melalui link youtube.
- /play [balas ke audio]: putar lagu melalui audio.
- /dplay: putar lagu via deezer.
- /splay: putar lagu via jio saavn.
- /ytplay: putar lagu via youtube music.

**🍂 playback:**

- /player: buka pengaturan pemutar musik.
- /skip: lewati lagu saat ini ke lagu berikutnya.
- /pause: jeda pemutaran music.
- /resume: lanjutkan pemutaran lagu yang di jeda.
- /end: hentikan pemutaran musik.
- /current: tampilkan trek pemutaran.
- /playlist: tampilkan daftar lagu yang diputar.

*semua perintah dapat digunakan member grup kecuali /skip, /end, /pause, /resume hanya untuk admin.
""",
        
f"""
**🌻 Channel Music Play**

🍂 hanya untuk admin grup & channel:

- /cplay [nama lagu] - play song you requested
- /cdplay [nama lagu] - play song you requested via deezer
- /csplay [nama lagu] - play song you requested via jio saavn
- /cplaylist - Show now playing list
- /cccurrent - Show now playing
- /cplayer - open music player settings panel
- /cpause - pause song play
- /cresume - resume song play
- /cskip - play next song
- /cend - stop music play
- /userbotjoinchannel - invite assistant to your chat

channel juga dapat digunakan sebagai pengganti c ( /cplay = /channelplay )

🍂 Jika anda tidak ingin memutar musik di grup channel lakukan ini:

1) ambil id channel mu.
2) buat grup dengan nama: Channel Music: your_channel_id
3) jadikan bot admin di channel dengan izin penuh.
4) tambahkan @{ASSISTANT_NAME} ke dalam channel dan jadikan admin.
5) cukup kirim perintah di grup anda.
""",

f"""
**🍂 more tools:**

- /musicplayer [on/off]: enable/disable music player.
- /admincache: perbarui informasi admin di grup anda. lakukan jika bot tidak merespon perintah admin.
- /userbotjoin: undang @{ASSISTANT_NAME} userbot ke dalam grup anda.

**⚔️ perintah untuk sudo users:**

 - /userbotleaveall - keluarkan userbot dari semua grup.
 - /gcast <balas ke pesan> - kirim pesan broadcast secara global.
 - /pmpermit [on/off] - enable/disable pesan pmpermit.
 
➠ sudo users dapat menjalankan perintah apa pun di grup mana pun.

"""
      ]
