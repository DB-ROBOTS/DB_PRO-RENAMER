
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from mwk.config import Config

# the Strings used for this "thing"
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

@Client.on_message(filters.document | filters.video | filters.audio | filters.voice | filters.video_note | filters.animation) 
async def rename_filter(c,m):
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await c.get_chat_member(update_channel, m.chat.id)
            if user.status == "kicked":
               await m.reply_text("🤭 Sorry Dude, You are **B A N N E D**. If you feel You are not guilty please contact owner")
               return
        except UserNotParticipant:
            await text="**🕵️𝗡𝗢𝗧 𝗪𝗢𝗥𝗞𝗜𝗡𝗚 𝗞𝗡𝗢𝗪😂\n\n🥳𝑱𝒐𝒊𝒏 𝑮𝒊𝒗𝒆𝒏 𝑩𝒆𝒍𝒐𝒘 👇 𝑪𝒉𝒂𝒏𝒏𝒆𝒍𝒔 𝒕𝒐 𝒖𝒔𝒆 𝒎𝒆 𝒐𝒌𝒌 & 𝑬𝒏𝒋𝒐𝒚 𝒕𝒉𝒆 𝑭𝒓𝒆𝒆 𝑺𝒆𝒓𝒗𝒊𝒄𝒆 😍**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="🔰𝐉𝐎𝐈𝐍 𝐎𝐔𝐑𝐒 𝐔𝐏𝐃𝐀𝐓𝐄𝐒 𝐂𝐇𝐋🔰", url=f"https://t.me/{update_channel}")],
                  [ InlineKeyboardButton(text="🎬𝑱𝑶𝑰𝑵 𝑶𝑼𝑹 𝑨𝑳𝑳 𝑪𝑯𝑨𝑵𝑵𝑬𝑳𝑺🎬", url=f"https://t.me/UNI_MOVIES_BOX")]
  
              ])
            )
            return
    media = m.document or m.video or m.audio or m.voice or m.video_note or m.animation
    text = ""
    button = []
    try:
      filename = media.file_name
      text += f"FileName:\n{filename}\n"
    except:
    # some files dont gib name ..
      filename = None 
    lu
    text += "🤖𝙷𝙰𝙰 𝙽𝙾𝚆,𝙿𝙻𝙴𝙰𝚂𝙴 𝚂𝙴𝙻𝙴𝙲𝚃 𝚃𝙷𝙴 𝙳𝙸𝚂𝙸𝚁𝙴𝙳 𝙶𝙸𝚅𝙴𝙽 𝙱𝙴𝙻𝙾𝚆 𝙾𝙿𝚃𝙸𝙾𝙽 𝙰𝙽𝙳 𝙼𝙾𝚅𝙴 𝙾𝙽 🔰!!\n🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽"
    button.append([InlineKeyboardButton("📂 ʀᴇɴᴀᴍᴇ ᴀs ғɪʟᴇ📂", callback_data="rename_file")])
  # Thanks to albert for mime_type suggestion 
    if media.mime_type.startswith("video/"):
    ## how the f the other formats can be uploaded as video 
      button.append([InlineKeyboardButton("🎞️ ʀᴇɴᴀᴍᴇ ᴀs ᴠɪᴅᴇᴏ 🎞️",callback_data="rename_video")])
      button.append([InlineKeyboardButton("🎞️ ᴄᴏɴᴠᴇʀᴛ ᴛᴏ ғɪʟᴇ📂",callback_data="convert_file")])
      button.append([InlineKeyboardButton("📂 ᴄᴏɴᴠᴇʀᴛ ᴛᴏ ᴠɪᴅᴇᴏ🎞️",callback_data="convert_video")])
    button.append([InlineKeyboardButton("𝐂𝐀𝐍𝐂𝐄𝐋 𝐓𝐇𝐄 𝐏𝐑𝐎𝐆𝐑𝐀𝐒𝐒 ❌",callback_data="cancel")])
 
    markup = InlineKeyboardMarkup(button)
    try:
      await m.reply_text(text,quote=True,reply_markup=markup,parse_mode="markdown",disable_web_page_preview=True)
    except Exception as e:
      log.info(str(e))
