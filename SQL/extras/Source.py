import re
import time
from datetime import datetime
from Arab import StartTime, iqthon
from Arab.Config import Config
from Arab.plugins import mention
help1 = ("**🝳 ⦙ كيفيه التنصيب :**")
help2 = ("**🝳 ⦙ قـائمـه الاوامـر :**\n**🝳 ⦙ قنـاه السـورس :** @FTTUTY  ")
TG_BOT = Config.TG_BOT_USERNAME
TM = time.strftime("%I:%M")
Sour = f"**‎✰︎┊ᴍʏ 𖠄 {mention} ٫ **\n‌‎**✰︎┊ʙᴏᴛ 𖠄 {TG_BOT} ٫**\n**‌‎✰︎┊ᴛɪᴍᴇ 𖠄 {TM} ٫**\n**‌‎✰︎┊‌‎ᴠᴇʀsʟᴏɴ 𖠄 (7.7) ,** \n**✰︎┊‌‎ᴅᴇᴠ sᴀᴍɪʀ 𖠄** @DEV_SAMIR"
