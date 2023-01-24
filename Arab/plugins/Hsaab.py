import asyncio
import random
import glob
import re
import shutil
import urllib
import base64
import requests
import time
import shlex
import math
import os
import html
import io
import sys
import traceback
import cv2
from asyncio import sleep
import telethon.password as pwd_mod
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.events import CallbackQuery
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.errors import FloodWaitError
from telethon.tl import functions
from urlextract import URLExtract
from requests import get
from typing import Optional, Tuple
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events
from telethon.utils import pack_bot_file_id, get_input_location
from telethon.tl.custom import Dialog
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.types import Channel, Chat, User
from telethon.errors.rpcerrorlist import UsernameOccupiedError
from asyncio.exceptions import TimeoutError as AsyncTimeout
from telethon.errors.rpcerrorlist import MessageTooLongError, YouBlockedUserError
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantsBots
from telethon.tl.types import DocumentAttributeVideo as video
from telethon.errors.rpcerrorlist import UserAlreadyParticipantError
from telethon.tl.types import InputMessagesFilterMusic
from telethon.tl.functions.messages import SaveDraftRequest
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from ..helpers.progress import humanbytes as hb
from Arab.utils import admin_cmd, sudo_cmd, eor
from telethon.utils import get_display_name
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from telethon.tl.functions.photos import DeletePhotosRequest, GetUserPhotosRequest
from ..helpers.utils import reply_id as rd
from telethon.tl.types import Channel, Chat, InputPhoto, User
from telethon.errors import ChatAdminRequiredError
from ..sql_helper.GrChhelper import Auto_ChGR, deletAutoChGR, getGrChAuto
from telethon.errors import FloodWaitError, ChannelInvalidError
from Arab import iqthon
from Arab.core.logger import logging
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from . import ALIVE_NAME, AUTONAME, BOTLOG, BOTLOG_CHATID, DEFAULT_BIO, get_user_from_event
from ..helpers import get_user_from_event, reply_id
from ..sql_helper.locks_sql import *
from ..helpers.functions import deEmojify, hide_inlinebot, waifutxt
from Arab.utils.decorators import register
from ..helpers.utils import reply_id, _catutils, parse_pre, yaml_format, install_pip, get_user_from_event, _format
from Arab.helpers.functions import convert_toimage,    deEmojify,    phcomment,    threats,    trap,    trash
from Arab.helpers.functions import convert_tosticker,    flip_image,    grayscale,    invert_colors,    mirror_file,    solarize
from ..sql_helper.global_list import add_to_list, get_collection_list, is_in_list, rm_from_list
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..sql_helper.locks_sql import *
from telethon import TelegramClient, client, events
from telethon.tl.functions.contacts import GetBlockedRequest, UnblockRequest
from PIL import Image, ImageDraw, ImageFont
import PIL.ImageOps
from . import AUTONAME, BOTLOG, BOTLOG_CHATID, DEFAULT_BIO, _catutils, edit_delete, iqthon, logging, spamwatch    
def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"{full_name}"
def user_full_name(user):
    names = [user.first_name]
    names = [i for i in list(names) if i]
    return " ".join(names)
STAT_INDICATION = "**🝳 ⦙   جـاري جـمـع الإحصـائيـات ، انتـظـر 🔄**"
CHANNELS_STR = "**🝳 ⦙   قائمة القنوات التي أنت فيها موجودة هنا\n\n"
CHANNELS_ADMINSTR = "**🝳 ⦙  قائمة القنوات التي تديرها هنا **\n\n"
CHANNELS_OWNERSTR = "**🝳 ⦙  قائمة القنوات التي تمتلك فيها هنا **\n\n"
GROUPS_STR = "**🝳 ⦙  قائمة المجموعات التي أنت فيها موجود هنا **\n\n"
GROUPS_ADMINSTR = "**🝳 ⦙  قائمة المجموعات التي تكون مسؤولاً فيها هنا **\n\n"
GROUPS_OWNERSTR = "**🝳 ⦙  قائمة المجموعات التي تمتلك فيها هنا **\n\n"
INVALID_MEDIA = "**🝳 ⦙  إمتداد هذه الصورة غير صالح  ❌**"
PP_CHANGED = "**🝳 ⦙  تم تغير صورة حسابك بنجاح  ✅**"
PP_TOO_SMOL = "**🝳 ⦙  هذه الصورة صغيرة جدًا قم بإختيار صورة أخرى  ⚠️**"
PP_ERROR = "**🝳 ⦙  حدث خطأ أثناء معالجة الصورة  ⚠️**"
BIO_SUCCESS = "**🝳 ⦙  تم تغيير بايو حسابك بنجاح  ✅**"

iqthonfont = gvarstatus("DEFAULT_PIC") or "Arab/sql_helper/IQTHONIMOGE.ttf"
FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
autopic_path = os.path.join(os.getcwd(), "Arab", "original_pic.png")
digitalpic_path = os.path.join(os.getcwd(), "Arab", "digital_pic.png")
autophoto_path = os.path.join(os.getcwd(), "Arab", "photo_pfp.png")
EMOJI_TELETHON = gvarstatus("ALIVE_EMOJI") or " "
OR_FOTOAUTO = gvarstatus("OR_FOTOAUTO") or "صوره وقتية"
plagiarism = gvarstatus("OR_PLAG") or "انتحال"
unplagiarism = gvarstatus("OR_UNPLAG") or "الغاء الانتحال"
idee = gvarstatus("OR_ID") or "اييديي"
OR_NAMEAUTO = gvarstatus("OR_NAMEAUTO") or "اسم وقتي"
OR_AUTOBIO = gvarstatus("OR_AUTOBIO") or "نبذه وقتيه"
AUTOGRCH = ""
FONTGRCH1 = "1234567890"
FONTGRCH2 = gvarstatus("FONTGRCH") or "𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢"
NAME_OK = "**🝳 ⦙  تم تغيير اسم حسابك بنجاح  ✅**"
USERNAME_SUCCESS = "**🝳 ⦙  تم تغيير معرّف حسابك بنجاح  ✅**"
USERNAME_TAKEN = "**🝳 ⦙  هذا المعرّف مستخدم  ❌**"
plugin_category = "tools"
DEFAULTUSER = gvarstatus("FIRST_NAME") or ALIVE_NAME
DEFAULTUSERBIO = gvarstatus("DEFAULT_BIO") or "الحمد الله"
DEFAULTUSER = AUTONAME or Config.ALIVE_NAME
LOGS = logging.getLogger(__name__)

digitalpfp = (gvarstatus("AUTO_PIC") or "https://telegra.ph/file/6629cc2f43156292340a5.jpg")


async def digitalpicloop():
    DIGITALPICSTART = gvarstatus("صوره وقتية") == "true"
    i = 0
    while DIGITALPICSTART:
        if not os.path.exists(digitalpic_path):
            digitalpfp = gvarstatus("AUTO_PIC")
            downloader = SmartDL(digitalpfp, digitalpic_path, progress_bar=False)
            downloader.start(blocking=False)
            while not downloader.isFinished():
                pass
        shutil.copy(digitalpic_path, autophoto_path)
        Image.open(autophoto_path)
        current_time = datetime.now().strftime("%I:%M")
        img = Image.open(autophoto_path)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(f"{iqthonfont}", 200)
        drawn_text.text((300, 400), current_time, font=fnt, fill=(255, 255, 255))
        img.save(autophoto_path)
        file = await iqthon.upload_file(autophoto_path)
        try:
            if i > 0:
                await iqthon(
                    functions.photos.DeletePhotosRequest(
                        await iqthon.get_profile_photos("me", limit=1)
                    )
                )
            i += 1
            await iqthon(functions.photos.UploadProfilePhotoRequest(file))
            os.remove(autophoto_path)
            await asyncio.sleep(60)
        except BaseException:
            return
        DIGITALPICSTART = gvarstatus("صوره وقتية") == "true"






async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE    )
    stdout, stderr = await process.communicate()
    return (        stdout.decode("utf-8", "replace").strip(),        stderr.decode("utf-8", "replace").strip(),        process.returncode,        process.pid,    )    
async def add_frame(imagefile, endname, x, color):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.expand(image, border=x, fill=color)
    inverted_image.save(endname)
async def crop(imagefile, endname, x):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.crop(image, border=x)
    inverted_image.save(endname)
@iqthon.on(admin_cmd(pattern="احصائيات حسابي(?: |$)(.*)"))
async def stats(event):  
    cat = await edit_or_reply(event, STAT_INDICATION)
    start_time = time.time()
    private_chats = 0
    bots = 0
    groups = 0
    broadcast_channels = 0
    admin_in_groups = 0
    creator_in_groups = 0
    admin_in_broadcast_channels = 0
    creator_in_channels = 0
    unread_mentions = 0
    unread = 0
    dialog: Dialog
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            broadcast_channels += 1
            if entity.creator or entity.admin_rights:
                admin_in_broadcast_channels += 1
            if entity.creator:
                creator_in_channels += 1
        elif (
            isinstance(entity, Channel)
            and entity.megagroup
            or not isinstance(entity, Channel)
            and not isinstance(entity, User)
            and isinstance(entity, Chat)
        ):
            groups += 1
            if entity.creator or entity.admin_rights:
                admin_in_groups += 1
            if entity.creator:
                creator_in_groups += 1
        elif not isinstance(entity, Channel) and isinstance(entity, User):
            private_chats += 1
            if entity.bot:
                bots += 1
        unread_mentions += dialog.unread_mentions_count
        unread += dialog.unread_count
    stop_time = time.time() - start_time
    full_name = inline_mention(await event.client.get_me())
    response = f"📌 **• ⚜️ |  احصائيات حسـابك العـامة لـ {full_name} 📊** \n"
    response += f"**🝳 ⦙  الدردشات الخاصة 🏷️  :** {private_chats} \n"
    response += f"**🝳 ⦙   الاشـخاص 🚹 : {private_chats - bots}` \n"
    response += f"**🝳 ⦙   الـبوتـات 🤖 : {bots}` **\n"
    response += f"**🝳 ⦙   عـدد المجـموعـات 🚻 :** `{groups}` \n"
    response += f"**🝳 ⦙   عـدد القنـوات  🚻 :** `{broadcast_channels}` \n"
    response += f"**🝳 ⦙   عـدد المجـموعات التـي تكـون فيها ادمـن  🛂 :** `{admin_in_groups}` \n"
    response += f"**🝳 ⦙   عـدد المجموعات التـي أنـشأتـها  🛃** : `{creator_in_groups}` \n"
    response += f"**🝳 ⦙   عـدد القنوات التـي تكـون فيها ادمـن 📶 : `{admin_in_broadcast_channels}` **\n"
    response += f"**🝳 ⦙   حقوق المسؤول في القنوات  🛂 : `{admin_in_broadcast_channels - creator_in_channels}` **\n"
    response += f"**عـدد المحـادثـات الغيـر مقـروء 📄 :** {unread} \n"
    response += f"**عـدد الـتاكـات الغيـر مقـروء 📌 :** {unread_mentions} \n"
    response += f"**🝳 ⦙   استغرق الأمر  🔍  :** `{stop_time:.02f}` ثانيه \n"
    await cat.edit(response)
@iqthon.on(admin_cmd(outgoing=True, pattern="ص1$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois1:
        await vois.client.send_file(vois.chat_id, iqvois1, reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص2$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois2:
        await vois.client.send_file(vois.chat_id, iqvois2, reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص3$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois3:
        await vois.client.send_file(vois.chat_id, iqvois3, reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="اطار ?(.*)"))
async def memes(mafia):
    reply = await mafia.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mafia, "الرد على الوسائط المدعومة")
        return
    mafiainput = mafia.pattern_match.group(1)
    if not mafiainput:
        mafiainput = 50
    if ";" in str(mafiainput):
        mafiainput, colr = mafiainput.split(";", 1)
    else:
        colr = 0
    mafiainput = int(mafiainput)
    colr = int(colr)
    mafiaid = mafia.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mafia = await edit_or_reply(mafia, "تحليل هذه الوسائط")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    mafiasticker = await reply.download_media(file="./temp/")
    if not mafiasticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mafiasticker)
        await edit_or_reply(mafia, "الوسائط المدعومة غير موجودة")
        return
    import base64

    kraken = None
    if mafiasticker.endswith(".tgs"):
        await mafia.edit(            "تحليل هذه الوسائط!"        )
        mafiafile = os.path.join("./temp/", "meme.png")
        mafiacmd = (            f"lottie_convert.py --frame 0 -if lottie -of png {mafiasticker} {mafiafile}"        )
        stdout, stderr = (await runcmd(mafiacmd))[:2]
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            LOGS.info(stdout + stderr)
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith(".webp"):
        await mafia.edit(            "تحليل هذه الوسائط 🧐!"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        os.rename(mafiasticker, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith((".mp4", ".mov")):
        await mafia.edit(            "تحليل هذه الوسائط 🧐!"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mafiasticker, 0, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
    else:
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        meme_file = mafiasticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mafia.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if kraken else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, mafiainput, colr)
    except Exception as e:
        return await mafia.edit(f"`{e}`")
    try:
        await mafia.client.send_file(            mafia.chat_id, outputfile, force_document=False, reply_to=mafiaid        )
    except Exception as e:
        return await mafia.edit(f"`{e}`")
    await mafia.delete()
    os.remove(outputfile)
    for files in (mafiasticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)
@iqthon.on(admin_cmd(outgoing=True, pattern="ص4$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois4:
        await vois.client.send_file(vois.chat_id, iqvois4, reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="قلب الصوره$"))
async def memes(mafia):
    reply = await mafia.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mafia, "الرد على الوسائط المدعومة")
        return
    mafiaid = mafia.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mafia = await edit_or_reply(mafia, "إحضار بيانات الوسائط")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    mafiasticker = await reply.download_media(file="./temp/")
    if not mafiasticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mafiasticker)
        await edit_or_reply(mafia, "الوسائط المدعومة غير موجودة")
        return
    import base64

    kraken = None
    if mafiasticker.endswith(".tgs"):
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        mafiafile = os.path.join("./temp/", "meme.png")
        mafiacmd = (            f"lottie_convert.py --frame 0 -if lottie -of png {mafiasticker} {mafiafile}"        )
        stdout, stderr = (await runcmd(mafiacmd))[:2]
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            LOGS.info(stdout + stderr)
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith(".webp"):
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        os.rename(mafiasticker, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("`Template not found... `")
            return
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith((".mp4", ".mov")):
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mafiasticker, 0, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
        kraken = True
    else:
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        meme_file = mafiasticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mafia.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if kraken else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await mafia.client.send_file(        mafia.chat_id, outputfile, force_document=False, reply_to=mafiaid    )
    await mafia.delete()
    os.remove(outputfile)
    for files in (mafiasticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@iqthon.on(admin_cmd(outgoing=True, pattern="فلتر رصاصي$"))
async def memes(mafia):
    reply = await mafia.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mafia, "الرد على الوسائط المدعومة")
        return
    mafiaid = mafia.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mafia = await edit_or_reply(mafia, "إحضار بيانات الوسائط")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    mafiasticker = await reply.download_media(file="./temp/")
    if not mafiasticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mafiasticker)
        await edit_or_reply(mafia, "الوسائط المدعومة غير موجودة")
        return
    import base64

    kraken = None
    if mafiasticker.endswith(".tgs"):
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        mafiafile = os.path.join("./temp/", "meme.png")
        mafiacmd = (            f"lottie_convert.py --frame 0 -if lottie -of png {mafiasticker} {mafiafile}"        )
        stdout, stderr = (await runcmd(mafiacmd))[:2]
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            LOGS.info(stdout + stderr)
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith(".webp"):
        await mafia.edit(            "تحليل هذه الوسائط 🧐!"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        os.rename(mafiasticker, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith((".mp4", ".mov")):
        await mafia.edit(            "تحليل هذه الوسائط 🧐!"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mafiasticker, 0, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
        kraken = True
    else:
        await mafia.edit(            "تحليل هذه الوسائط 🧐!"        )
        meme_file = mafiasticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mafia.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if kraken else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await mafia.client.send_file(        mafia.chat_id, outputfile, force_document=False, reply_to=mafiaid    )
    await mafia.delete()
    os.remove(outputfile)
    for files in (mafiasticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)
@iqthon.on(events.NewMessage(outgoing=True, pattern='.فك المحظورين'))
async def UnBlockList(event):

    # GET BLOCKED USERS LIST
    list = await iqthon(GetBlockedRequest(offset=0, limit=1000000))

    if len(list.blocked) == 0 :
        order_reply = await event.edit(f'[ ! ] **لم تقم بحظر أي شخص أصلا**')
    else :

        unblocked_count = 1
        for user in list.blocked :

            # UNBLOCK > USER OR BOT
            UnBlock = await iqthon(UnblockRequest(id=int(user.peer_id.user_id)))
            unblocked_count += 1

            order_reply = await event.edit(f'[ ~ ] **جاري .فك المحظورين من حسابك** {round((unblocked_count * 100) / len(list.blocked), 2)}%')


        unblocked_count = 1
        order_reply = await event.edit(f'[ ! ] **تم .فك المحظورين من حسابك يرجى الأنتظار دقائق في حالة تبقى عدد قليل من المحظورين ويرجى الأنتباة هذا الأمر يسبب تعليق في حسابك في حالة أكثرت في أستعمال الأمر ** : {len(list.blocked)}\n\n[ + ] **فك المحظورين أكتمل.**')
@iqthon.on(admin_cmd(outgoing=True, pattern="زوم ?(.*)"))
async def memes(mafia):
    reply = await mafia.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mafia, "الرد على الوسائط المدعومة")
        return
    mafiainput = mafia.pattern_match.group(1)
    mafiainput = 50 if not mafiainput else int(mafiainput)
    mafiaid = mafia.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mafia = await edit_or_reply(mafia, "تحليل هذه الوسائط")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    mafiasticker = await reply.download_media(file="./temp/")
    if not mafiasticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mafiasticker)
        await edit_or_reply(mafia, "القالب غير موجود")
        return
    import base64

    kraken = None
    if mafiasticker.endswith(".tgs"):
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        mafiafile = os.path.join("./temp/", "meme.png")
        mafiacmd = (            f"lottie_convert.py --frame 0 -if lottie -of png {mafiasticker} {mafiafile}"        )
        stdout, stderr = (await runcmd(mafiacmd))[:2]
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            LOGS.info(stdout + stderr)
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith(".webp"):
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        os.rename(mafiasticker, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith((".mp4", ".mov")):
        await mafia.edit(            "تحليل هذه الوسائط 🧐!"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mafiasticker, 0, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
    else:
        await mafia.edit(            "تحليل هذه الوسائط 🧐!"        )
        meme_file = mafiasticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mafia.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if kraken else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, mafiainput)
    except Exception as e:
        return await mafia.edit(f"`{e}`")
    try:
        await mafia.client.send_file(            mafia.chat_id, outputfile, force_document=False, reply_to=mafiaid        )
    except Exception as e:
        return await mafia.edit(f"`{e}`")
    await mafia.delete()
    os.remove(outputfile)
    for files in (mafiasticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)
@iqthon.on(admin_cmd(outgoing=True, pattern="ص5$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois5:
        await vois.client.send_file(vois.chat_id, iqvois5, reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص6$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois6:
        await vois.client.send_file(vois.chat_id, iqvois6, reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص7$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois7:
        await vois.client.send_file(vois.chat_id, iqvois7, reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص8$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois:
        await vois.client.send_file(vois.chat_id, iqvois, reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص9$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois9 :
        await vois.client.send_file(vois.chat_id, iqvois9 , reply_to=Ti)
        await vois.delete()

@iqthon.on(admin_cmd(outgoing=True, pattern="ص10$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois10:
        await vois.client.send_file(vois.chat_id, iqvois10 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص11$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois11 :
        await vois.client.send_file(vois.chat_id, iqvois11 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص12$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois12:
        await vois.client.send_file(vois.chat_id, iqvois12 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص13$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois13:
        await vois.client.send_file(vois.chat_id, iqvois13 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص14$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois14:
        await vois.client.send_file(vois.chat_id, iqvois14 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص15$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois15:
        await vois.client.send_file(vois.chat_id, iqvois15 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص16$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois16:
        await vois.client.send_file(vois.chat_id, iqvois16 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص17$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois17:
        await vois.client.send_file(vois.chat_id, iqvois17 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص18$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois18:
        await vois.client.send_file(vois.chat_id, iqvois18 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص19$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois19:
        await vois.client.send_file(vois.chat_id, iqvois19 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص20$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois20:
        await vois.client.send_file(vois.chat_id, iqvois20 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص21$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois21:
        await vois.client.send_file(vois.chat_id, iqvois21 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص22$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois22:
        await vois.client.send_file(vois.chat_id, iqvois22 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص23$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois23:
        await vois.client.send_file(vois.chat_id, iqvois23 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص24$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois24:
        await vois.client.send_file(vois.chat_id, iqvois24 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص25$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois25:
        await vois.client.send_file(vois.chat_id, iqvois25 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص26$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois26:
        await vois.client.send_file(vois.chat_id, iqvois26 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص27$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois27:
        await vois.client.send_file(vois.chat_id, iqvois27 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص28$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois28:
        await vois.client.send_file(vois.chat_id, iqvois28 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص29$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois29:
        await vois.client.send_file(vois.chat_id, iqvois29 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص30$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois30:
        await vois.client.send_file(vois.chat_id, iqvois30 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص31$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois31:
        await vois.client.send_file(vois.chat_id, iqvois31 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص32$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois32:
        await vois.client.send_file(vois.chat_id, iqvois32 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص33$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois33:
        await vois.client.send_file(vois.chat_id, iqvois33 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص34$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois34:
        await vois.client.send_file(vois.chat_id, iqvois34 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص35$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois35:
        await vois.client.send_file(vois.chat_id, iqvois35 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص36$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois36:
        await vois.client.send_file(vois.chat_id, iqvois36 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص37$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois37:
        await vois.client.send_file(vois.chat_id, iqvois37 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص38$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois38:
        await vois.client.send_file(vois.chat_id, iqvois38 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص39$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois39:
        await vois.client.send_file(vois.chat_id, iqvois39 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص40$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois40:
        await vois.client.send_file(vois.chat_id, iqvois40 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص41$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois41:
        await vois.client.send_file(vois.chat_id, iqvois41 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص42$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois42:
        await vois.client.send_file(vois.chat_id, iqvois42 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص43$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois43:
        await vois.client.send_file(vois.chat_id, iqvois43 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص44$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois44:
        await vois.client.send_file(vois.chat_id, iqvois44 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص45$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois45:
        await vois.client.send_file(vois.chat_id, iqvois45 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص46$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois46:
        await vois.client.send_file(vois.chat_id, iqvois46 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص47$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois47:
        await vois.client.send_file(vois.chat_id, iqvois47 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص48$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois48:
        await vois.client.send_file(vois.chat_id, iqvois48 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص49$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois49:
        await vois.client.send_file(vois.chat_id, iqvois49 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص50$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois50:
        await vois.client.send_file(vois.chat_id, iqvois50 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(pattern="قائمه (جميع القنوات|قنوات اديرها|قنوات امتلكها)$"))
async def stats(event):  
    catcmd = event.pattern_match.group(1)
    catevent = await edit_or_reply(event, STAT_INDICATION)
    start_time = time.time()
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    hi = []
    hica = []
    hico = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            hi.append([entity.title, entity.id])
            if entity.creator or entity.admin_rights:
                hica.append([entity.title, entity.id])
            if entity.creator:
                hico.append([entity.title, entity.id])
    if catcmd == "جميع القنوات":
        output = CHANNELS_STR
        for k, i in enumerate(hi, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = CHANNELS_STR
    elif catcmd == "قنوات اديرها":
        output = CHANNELS_ADMINSTR
        for k, i in enumerate(hica, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = CHANNELS_ADMINSTR
    elif catcmd == "قنوات امتلكها":
        output = CHANNELS_OWNERSTR
        for k, i in enumerate(hico, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = CHANNELS_OWNERSTR
    stop_time = time.time() - start_time
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    output += f"\n**استغرق حساب القنوات : ** {stop_time:.02f} ثانيه"
    try:
        await catevent.edit(output)
    except Exception:
        await edit_or_reply(            catevent,
            output,
            caption=caption        )
@iqthon.on(admin_cmd(pattern="قائمه (جميع المجموعات|مجموعات اديرها|مجموعات امتلكها)$"))
async def stats(event):  
    catcmd = event.pattern_match.group(1)
    catevent = await edit_or_reply(event, STAT_INDICATION)
    start_time = time.time()
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    hi = []
    higa = []
    higo = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            continue
        elif (
            isinstance(entity, Channel)
            and entity.megagroup
            or not isinstance(entity, Channel)
            and not isinstance(entity, User)
            and isinstance(entity, Chat)        ):
            hi.append([entity.title, entity.id])
            if entity.creator or entity.admin_rights:
                higa.append([entity.title, entity.id])
            if entity.creator:
                higo.append([entity.title, entity.id])
    if catcmd == "جميع المجموعات":
        output = GROUPS_STR
        for k, i in enumerate(hi, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = GROUPS_STR
    elif catcmd == "مجموعات اديرها":
        output = GROUPS_ADMINSTR
        for k, i in enumerate(higa, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = GROUPS_ADMINSTR
    elif catcmd == "مجموعات امتلكها":
        output = GROUPS_OWNERSTR
        for k, i in enumerate(higo, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = GROUPS_OWNERSTR
    stop_time = time.time() - start_time
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    output += f"\n**استغرق حساب المجموعات : ** {stop_time:.02f} ثانيه"
    try:
        await catevent.edit(output)
    except Exception:
        await edit_or_reply(
            catevent,
            output,
            caption=caption        )
@iqthon.iq_cmd(pattern="حفض كتابه$")
async def saf(e):
    x = await e.get_reply_message()
    if not x:
        return await eod(            e, "قم بالرد على أي رسالة لحفظها في رسائلك المحفوظة", time=5        )
    if e.out:
        await e.client.send_message("me", x)
    else:
        await e.client.send_message(e.sender_id, x)
    await eor(e, "تم حفظ الرسالة", time=5)

@iqthon.iq_cmd(pattern="حفض توجيه$")
async def saf(e):
    x = await e.get_reply_message()
    if not x:
        return await eod(            e, "قم بالرد على أي رسالة لحفظها في رسائلك المحفوظة", time=5        )
    if e.out:
        await x.forward_to("me")
    else:
        await x.forward_to(e.sender_id)
    await eor(e, "تم حفظ الرسالة.", time=5)
@iqthon.on(admin_cmd(pattern="(الايدي|id)(?: |$)(.*)"))
async def _(event):
    input_str = event.pattern_match.group(2)
    if input_str:
        try:
            p = await event.client.get_entity(input_str)
        except Exception as e:
            return await edit_delete(event, f"`{str(e)}`", 5)
        try:
            if p.first_name:
                return await edit_or_reply(                    event, f"**🝳 ⦙   آيـدي المُستخدم 💠 :** `{input_str}` هـو `{p.id}`"                )
        except Exception:
            try:
                if p.title:
                    return await edit_or_reply(                        event, f"**🝳 ⦙   آيـدي الدردشــــة 💠 :** `{p.title}` هـو `{p.id}` "                    )
            except Exception as e:
                LOGS.info(str(e))
        await edit_or_reply(event, "**🝳 ⦙   قُم بإدخال أسم مُستخدم أو الرد على المُستخدم ⚜️**")
    elif event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await edit_or_reply(                event,                f"**🝳 ⦙   آيـدي الدردشــــة  💠 : **`{str(event.chat_id)}` \n**🝳 ⦙   آيـدي المُستخدم  💠 : **`{str(r_msg.sender_id)}` \n**🝳 ⦙  آيـدي الميديـا  🆔 : **`{bot_api_file_id}`"            )
        else:
            await edit_or_reply(                event,                f"**🝳 ⦙   آيـدي الدردشــــة  💠 : **`{str(event.chat_id)}` 𖥻\n**🝳 ⦙   آيـدي المُستخدم  💠 : **`{str(r_msg.sender_id)}` "            )

@iqthon.on(admin_cmd(pattern="وضع بايو(?: |$)(.*)"))
async def _(event):
    bio = event.pattern_match.group(1)
    try:
        await event.client(functions.account.UpdateProfileRequest(about=bio))
        await edit_delete(event, "**🝳 ⦙  تم تغيير البايو بنجاح  ✅**")
    except Exception as e:
        await edit_or_reply(event, f"**🝳 ⦙  خطأ  ⚠️ :**\n`{str(e)}`")
@iqthon.on(admin_cmd(pattern="وضع اسم(?: |$)(.*)"))
async def _(event):
    names = event.pattern_match.group(1)
    first_name = names
    last_name = ""
    if ";" in names:
        first_name, last_name = names.split("|", 1)
    try:
        await event.client(
            functions.account.UpdateProfileRequest(                first_name=first_name, last_name=last_name            )        )
        await edit_delete(event, "**🝳 ⦙  تم تغيير الاسم بنجاح  ✅**")
    except Exception as e:
        await edit_or_reply(event, f"**🝳 ⦙  خطأ  ⚠️ :**\n`{str(e)}`")
@iqthon.on(admin_cmd(pattern="وضع صوره(?: |$)(.*)"))
async def _(event):
    reply_message = await event.get_reply_message()
    catevent = await edit_or_reply(        event, "**...**"    )
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    photo = None
    try:
        photo = await event.client.download_media(            reply_message, Config.TMP_DOWNLOAD_DIRECTORY        )
    except Exception as e:
        await catevent.edit(str(e))
    else:
        if photo:
            await catevent.edit("**🝳 ⦙   أشترك @IQTHON **")
            if photo.endswith((".mp4", ".MP4")):
                # https://t.me/tgbetachat/324694
                size = os.stat(photo).st_size
                if size > 2097152:
                    await catevent.edit("**🝳 ⦙   يجب ان يكون الحجم اقل من 2 ميغا ✅**")
                    os.remove(photo)
                    return
                catpic = None
                catvideo = await event.client.upload_file(photo)
            else:
                catpic = await event.client.upload_file(photo)
                catvideo = None
            try:
                await event.client(
                    functions.photos.UploadProfilePhotoRequest(                        file=catpic, video=catvideo, video_start_ts=0.01                   )                )
            except Exception as e:
                await catevent.edit(f"**🝳 ⦙  خطأ  ⚠️ :**\n`{str(e)}`")
            else:
                await edit_or_reply(                    catevent, "**🝳 ⦙   تم تغيير الصورة بنجاح ✅**"                )
    try:
        os.remove(photo)
    except Exception as e:
        LOGS.info(str(e))



@iqthon.on(admin_cmd(pattern="وضع معرف(?: |$)(.*)"))
async def update_username(username):
    newusername = username.pattern_match.group(1)
    try:
        await username.client(UpdateUsernameRequest(newusername))
        await edit_delete(event, USERNAME_SUCCESS)
    except UsernameOccupiedError:
        await edit_or_reply(event, USERNAME_TAKEN)
    except Exception as e:
        await edit_or_reply(event, f"**🝳 ⦙  خطأ  ⚠️ :**\n`{str(e)}`")
@iqthon.on(admin_cmd(pattern=r"شوت ?(.*)", outgoing=True))
async def shout(args):
    if args.fwd_from:
        return
    else:
        msg = "```"
        messagestr = args.text
        messagestr = messagestr[7:]
        text = " ".join(messagestr)
        result = []
        result.append(" ".join([s for s in text]))
        for pos, symbol in enumerate(text[1:]):
            result.append(symbol + " " + "  " * pos + symbol)
        result = list("\n".join(result))
        result[0] = text[0]
        result = "".join(result)
        msg = "\n" + result
        await eor(args, "`" + msg + "`")

if 1 == 1:
    name = "Profile Photos"
    client = borg

    @iqthon.on(admin_cmd(pattern="الصور ?(.*)"))
    async def potocmd(event):
        id = "".join(event.raw_text.split(maxsplit=2)[1:])
        user = await event.get_reply_message()
        chat = event.input_chat
        if user:
            photos = await event.client.get_profile_photos(user.sender)
        else:
            photos = await event.client.get_profile_photos(chat)
        if id.strip() == "":
            try:
                await event.client.send_file(event.chat_id, photos)
            except a:
                photo = await event.client.download_profile_photo(chat)
                await borg.send_file(event.chat_id, photo)
        else:
            try:
                id = int(id)
                if id <= 0:
                    await eor(event, "رقم الهوية الذي أدخلته غير صالح")
                    return
            except BaseException:
                await eor(event, "ضع عدد جانب الامر")
                return
            if int(id) <= (len(photos)):
                send_photos = await event.client.download_media(photos[id - 1])
                await borg.send_file(event.chat_id, send_photos)
            else:
                await eor(event, "ليس لديه صور 🙄")
                return
@iqthon.on(admin_cmd(pattern="معرفاتي(?: |$)(.*)"))
async def _(event):
    result = await event.client(GetAdminedPublicChannelsRequest())
    output_str = "**🝳 ⦙  جميع القنوات والمجموعات التي قمت بإنشائها  💠  :**\n"
    output_str += "".join(f"🝳 ⦙    - {channel_obj.title} @{channel_obj.username} \n"
        for channel_obj in result.chats)
    await edit_or_reply(event, output_str)
@iqthon.on(admin_cmd(pattern="ملكيه ([\s\S]*)"))
async def _(event):
    user_name = event.pattern_match.group(1)
    try:
        pwd = await event.client(functions.account.GetPasswordRequest())
        my_srp_password = pwd_mod.compute_check(pwd, Config.TG_2STEP_VERIFICATION_CODE)
        await event.client(
            functions.channels.EditCreatorRequest(                channel=event.chat_id, user_id=user_name, password=my_srp_password            )        )
    except Exception as e:
        await event.edit(f"**🝳 ⦙  حـدث خـطأ ✕ :**\n`{str(e)}`")
    else:
        await event.edit("**🝳 ⦙  تم نقل ملكيه ✓**")


@iqthon.on(admin_cmd(pattern=f"{plagiarism}(?: |$)(.*)"))
async def _(event):
    replied_user, error_i_a = await get_user_from_event(event)
    if replied_user is None:
        return
    user_id = replied_user.id
    profile_pic = await event.client.download_profile_photo(user_id, Config.TEMP_DIR)
    first_name = html.escape(replied_user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    last_name = replied_user.last_name
    if last_name is not None:
        last_name = html.escape(last_name)
        last_name = last_name.replace("\u2060", "")
    if last_name is None:
        last_name = "⁪⁬⁮⁮⁮⁮ ‌‌‌‌"
    replied_user = (await event.client(GetFullUserRequest(replied_user.id))).full_user
    user_bio = replied_user.about
    if user_bio is not None:
        user_bio = replied_user.about
    await event.client(functions.account.UpdateProfileRequest(first_name=first_name))
    await event.client(functions.account.UpdateProfileRequest(last_name=last_name))
    await event.client(functions.account.UpdateProfileRequest(about=user_bio))
    try:
        pfile = await event.client.upload_file(profile_pic)
    except Exception as e:
        return await edit_delete(event, f"**خطأ :**\n__{e}__")
    await event.client(functions.photos.UploadProfilePhotoRequest(pfile))
    await edit_delete(event, "**تم الانتحال**")
    if BOTLOG:
        await event.client.send_message(            BOTLOG_CHATID,            f"انتحال \nتم انتحال
