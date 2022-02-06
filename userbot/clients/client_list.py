# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

import telethon.utils
from telethon.tl.functions.users import GetFullUserRequest


async def clients_list(SUDO_USERS, bot, AVP2, AVP3, AVP4, AVP5):
    user_ids = list(SUDO_USERS) or []
    main_id = await bot.get_me()
    user_ids.append(main_id.id)

    try:
        if AVP2 is not None:
            id2 = await AVP2.get_me()
            user_ids.append(id2.id)
    except BaseException:
        pass

    try:
        if AVP3 is not None:
            id3 = await AVP3.get_me()
            user_ids.append(id3.id)
    except BaseException:
        pass

    try:
        if AVP4 is not None:
            id4 = await AVP4.get_me()
            user_ids.append(id4.id)
    except BaseException:
        pass

    try:
        if AVP5 is not None:
            id5 = await AVP5.get_me()
            user_ids.append(id5.id)
    except BaseException:
        pass

    return user_ids


async def client_id(event, botid=None):
    if botid is not None:
        uid = await event.client(GetFullUserRequest(botid))
        OWNER_ID = uid.user.id
        AVP_USER = uid.user.first_name
    else:
        client = await event.client.get_me()
        uid = telethon.utils.get_peer_id(client)
        OWNER_ID = uid
        AVP_USER = client.first_name
    AVP_mention = f"[{AVP_USER}](tg://user?id={OWNER_ID})"
    return OWNER_ID, AVP_USER, AVP_mention
