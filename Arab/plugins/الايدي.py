import html
import os
import base64
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.types import MessageEntityMentionName
from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from Arab import iqthon
from Arab.core.logger import logging
from ..Config import Config
from ..core.managers import edit_or_reply, edit_delete
from ..helpers import reply_id
from ..sql_helper.globals import gvarstatus
from . import spamwatch
plugin_category = "@pp_g3"
LOGS = logging.getLogger(__name__)
iqthon_TEXT = gvarstatus("CUSTOM_ALIVE_TEXT") or "•❃╎مـعلومات الـشخص من بوت سـيـمـو"
iqthonM = gvarstatus("CUSTOM_ALIVE_EMOJI") or "•❃"
iqthonF = gvarstatus("CUSTOM_ALIVE_FONT") or "╔━⊶❃• [𝚂𝙾𝚄𝚁𝙲𝙴 𝚂𝙴𝙼𝙾]•❃⊷━╗"



async def get_user_from_event(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_object = await event.client.get_entity(previous_message.sender_id)
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)
        if not user:
            self_user = await event.client.get_me()
            user = self_user.id
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        if isinstance(user, int) or user.startswith("@"):
            user_obj = await event.client.get_entity(user)
            return user_obj
        try:
            user_object = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_object


async def fetch_info(replied_user, event):
    """Get details from the User object."""
    FullUser = (await event.client(GetFullUserRequest(replied_user.id))).full_user
    replied_user_profile_photos = await event.client(
        GetUserPhotosRequest(user_id=replied_user.id, offset=42, max_id=0, limit=80)    )
    replied_user_profile_photos_count = "لايـوجـد بروفـايـل"
    dc_id = "Can't get dc id"
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
        dc_id = replied_user.photo.dc_id
    except AttributeError:
        pass
    user_id = replied_user.id
    first_name = replied_user.first_name
    full_name = FullUser.private_forward_name
    common_chat = FullUser.common_chats_count
    username = replied_user.username
    user_bio = FullUser.about
    is_bot = replied_user.bot
    restricted = replied_user.restricted
    verified = replied_user.verified
    photo = await event.client.download_profile_photo(     user_id,     Config.TMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg",    download_big=True  )
    first_name = (      first_name.replace("\u2060", "")
        if first_name
        else ("هذا المستخدم ليس له اسم أول")  )
    full_name = full_name or first_name
    username = "@{}".format(username) if username else ("لايـوجـد معـرف")
    user_bio = "لاتـوجـد نبـذة" if not user_bio else user_bio
    rotbat = "صـاحـب سـورس سـيـمـو 𓄂𓆃" if user_id == 5809739881 or user_id == 5680297831 or user_id == 5957205447 else ("⌁ عضو عادي 𓅫 ⌁")
    rotbat = "⌁ مـالك الحساب 𓀫 ⌁" if user_id == (await event.client.get_me()).id and user_id != 5809739881 and user_id != 5680297831 and user_id != 5957205447  else rotbat
    caption = f"<b> {iqthon_TEXT} </b>\n"
    caption += f"ٴ{iqthonF} \n"
    caption += f"<b> {iqthonM}╎الاسـم    ☆╮ </b> {full_name}\n"
    caption += f"<b> {iqthonM}╎المعـرف  ☆╮ </b> {username}\n"
    caption += f"<b> {iqthonM}╎الايـدي   ☆╮ </b> <code>{user_id}</code>\n"
    caption += f"<b> {iqthonM}╎الرتبــهہ  ☆╮ {rotbat} </b>\n"
    caption += f"<b> {iqthonM}╎الصـور   ☆╮ </b> {replied_user_profile_photos_count}\n"
    caption += f"<b> {iqthonM}╎الحساب ☆╮ </b> "
    caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'
    caption += f"\n<b> {iqthonM}╎البايـو    ⇠ </b> {user_bio} \n\n"
    caption += f"ٴ{iqthonF} "
    return photo, caption

@iqthon.iq_cmd(pattern="ايدي(?: |$)(.*)",
    command=("ايدي", plugin_category),
    info={
        "header": "لـ عـرض معلومـات الشخـص",
        "الاستـخـدام": " {tr}ايدي بالـرد او {tr}ايدي + معـرف/ايـدي الشخص",
    },
)
async def who(event):
    "Gets info of an user"
    iqthon = await edit_or_reply(event, "⇆")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    replied_user = await get_user_from_event(event)
    try:
        photo, caption = await fetch_info(replied_user, event)
    except AttributeError:
        return await edit_or_reply(iqthon, "**- لـم استطـع العثــور ع الشخــص**")
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await event.client.send_file(            event.chat_id,            photo,            caption=caption,            link_preview=False,            force_document=False,            reply_to=message_id_to_reply,            parse_mode="html",        )
        if not photo.startswith("http"):
            os.remove(photo)
        await iqthon.delete()
    except TypeError:
        await iqthon.edit(caption, parse_mode="html")


