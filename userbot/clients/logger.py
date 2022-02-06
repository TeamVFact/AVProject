# Man - UserBot
# Copyright (c) 2022 AVProject
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/AVProject/ >
# t.me/SharingUserbot & t.me/Lunatic0de

from telethon.tl.functions.channels import InviteToChannelRequest

from userbot import AVP2, AVP3, AVP4, AVP5, BOT_USERNAME
from userbot import BOT_VER as version
from userbot import BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import bot, branch

MSG_ON = """
🔥 **AVProject Berhasil Di Aktifkan**
━━
➠ **Userbot Version -** `{}@{}`
➠ **Ketik** `{}alive` **untuk Mengecheck Bot**
➠ **Managed By** {}
━━
"""
try:
    user = bot.get_me()
    mention = f"[{user.first_name}](tg://user?id={user.id})"
except BaseException:
    pass


async def man_userbot_on():
    try:
        if bot:
            if BOTLOG_CHATID != 0:
                await bot.send_message(
                    BOTLOG_CHATID,
                    f"🔥 **AVProject Berhasil Di Aktifkan**\n━━\n➠ **Userbot Version -** `{version}@{branch}`\n➠ **Ketik** `{cmd}alive` **untuk Mengecheck Bot**\n━━",
                )
    except BaseException:
        pass
    try:
        if AVP2:
            if BOTLOG_CHATID != 0:
                await AVP2.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd, mention),
                )
    except BaseException:
        pass
    try:
        if AVP3:
            if BOTLOG_CHATID != 0:
                await AVP3.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd, mention),
                )
    except BaseException:
        pass
    try:
        if AVP4:
            if BOTLOG_CHATID != 0:
                await AVP4.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd, mention),
                )
    except BaseException:
        pass
    try:
        if AVP5:
            if BOTLOG_CHATID != 0:
                await AVP5.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd, mention),
                )
    except BaseException:
        pass
    try:
        await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass
