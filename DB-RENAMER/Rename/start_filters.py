import os
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from pyrogram.errors import UserNotParticipant

if bool(os.environ.get("WEBHOOK", False)):
    from mwk.config import Config
else:
    from config import Config

# the Strings used for this "thing"
from mwk.messages import Translation
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(filters.command("help"))
async def help_user(c,m):
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await c.get_chat_member(update_channel, m.chat.id)
            if user.status == "kicked":
               await m.reply_text("🤭 Sorry Dude, You are **B A N N E D**. If you feel You are not guilty please contact owner")
               return
        except UserNotParticipant:
            await m.reply_text(
                text="**🕵️𝗡𝗢𝗧 𝗪𝗢𝗥𝗞𝗜𝗡𝗚 𝗞𝗡𝗢𝗪😂\n\n🥳𝑱𝒐𝒊𝒏 𝑮𝒊𝒗𝒆𝒏 𝑩𝒆𝒍𝒐𝒘 👇 𝑪𝒉𝒂𝒏𝒏𝒆𝒍𝒔 𝒕𝒐 𝒖𝒔𝒆 𝒎𝒆 𝒐𝒌𝒌 & 𝑬𝒏𝒋𝒐𝒚 𝒕𝒉𝒆 𝑭𝒓𝒆𝒆 𝑺𝒆𝒓𝒗𝒊𝒄𝒆 😍**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="🔰𝐉𝐎𝐈𝐍 𝐎𝐔𝐑𝐒 𝐔𝐏𝐃𝐀𝐓𝐄𝐒 𝐂𝐇𝐋🔰", url=f"https://t.me/{update_channel}")],
                  [ InlineKeyboardButton(text="🎬𝑱𝑶𝑰𝑵 𝑶𝑼𝑹 𝑨𝑳𝑳 𝑪𝑯𝑨𝑵𝑵𝑬𝑳𝑺🎬", url=f"https://t.me/UNI_MOVIES_BOX")]

              ]
              ])
            )
            return
    try:
       await m.reply_text(Translation.HELP_USER,quote=True)
    except Exception as e:
        log.info(str(e))
        
@Client.on_message(filters.command("start"))
async def start_msg(c,m):
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await c.get_chat_member(update_channel, m.chat.id)
            if user.status == "kicked":
               await m.reply_text("🤭 Sorry Dude, You are **B A N N E D**. If you feel You are not guilty please contact owner")
               return
        except UserNotParticipant:
            await m.reply_text(
                text="**🕵️𝗡𝗢𝗧 𝗪𝗢𝗥𝗞𝗜𝗡𝗚 𝗞𝗡𝗢𝗪😂\n\n🥳𝑱𝒐𝒊𝒏 𝑮𝒊𝒗𝒆𝒏 𝑩𝒆𝒍𝒐𝒘 👇 𝑪𝒉𝒂𝒏𝒏𝒆𝒍𝒔 𝒕𝒐 𝒖𝒔𝒆 𝒎𝒆 𝒐𝒌𝒌 & 𝑬𝒏𝒋𝒐𝒚 𝒕𝒉𝒆 𝑭𝒓𝒆𝒆 𝑺𝒆𝒓𝒗𝒊𝒄𝒆 😍**",

                reply_markup=InlineKeyboardMarkup([

                    [ InlineKeyboardButton(text="🔰𝐉𝐎𝐈𝐍 𝐎𝐔𝐑𝐒 𝐔𝐏𝐃𝐀𝐓𝐄𝐒 𝐂𝐇𝐋🔰", url=f"https://t.me/{update_channel}")],

                  [ InlineKeyboardButton(text="🎬𝑱𝑶𝑰𝑵 𝑶𝑼𝑹 𝑨𝑳𝑳 𝑪𝑯𝑨𝑵𝑵𝑬𝑳𝑺🎬", url=f"https://t.me/UNI_MOVIES_BOX")]

 ])
            )
            return
    await m.reply_text(Translation.START_TEXT.format(m.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
            [
               [
                InlineKeyboardButton("🔬𝙹𝙾𝙸𝙽 𝙾𝚄𝚁𝚂 𝙱𝙾𝚃𝚂 𝙲𝙷𝙰𝙽𝙽𝙴𝙻🎬", url=f"https://t.me/DB_ROBOTS")],
                   [ InlineKeyboardButton("🎬𝙹𝙾𝙸𝙽 𝙾𝚄𝚁 𝙰𝙻𝙻 𝙼𝙾𝚅𝙸𝙴𝚂 𝙲𝙷𝙻🎬", url=f"https://t.me/UNI_MOVIES_BOX")
                ],
                [
                    InlineKeyboardButton("👨‍🔬 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 🛡️", url=f"https://t.me/Deeks_04_8")
                ]
            ]
        ),
        reply_to_message_id=m.message_id
    )
          #  return
        
@Client.on_message(filters.command("log") & filters.private & filters.user(Config.OWNER_ID))
async def log_msg(c,m):
  z =await m.reply_text("Processing..", True)
  if os.path.exists("Log.txt"):
     await m.reply_document("Log.txt", True)
     await z.delete()
  else:
    await z.edit_text("Log file not found")
