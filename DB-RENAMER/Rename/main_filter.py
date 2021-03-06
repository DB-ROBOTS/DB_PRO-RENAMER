
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
               await m.reply_text("š¤­ Sorry Dude, You are **B A N N E D**. If you feel You are not guilty please contact owner")
               return
        except UserNotParticipant:
            await text="**šµļøš”š¢š§ šŖš¢š„ššš”š šš”š¢šŖš\n\nš„³š±ššš š®šššš š©šššš š šŖššššššš šš ššš šš ššš & š¬šššš ššš š­ššš šŗšššššš š**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="š°šššš šššš ššššššš šššš°", url=f"https://t.me/{update_channel}")],
                  [ InlineKeyboardButton(text="š¬š±š¶š°šµ š¶š¼š¹ šØš³š³ šŖšÆšØšµšµš¬š³šŗš¬", url=f"https://t.me/UNI_MOVIES_BOX")]
  
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
    text += "š¤š·š°š° š½š¾š,šæš»š“š°šš“ šš“š»š“š²š šš·š“ š³šøššøšš“š³ š¶šøšš“š½ š±š“š»š¾š š¾šæššøš¾š½ š°š½š³ š¼š¾šš“ š¾š½ š°!!\nš½š½š½š½š½š½š½š½š½š½"
    button.append([InlineKeyboardButton("š Źį“É“į“į“į“ į“s ŅÉŖŹį“š", callback_data="rename_file")])
  # Thanks to albert for mime_type suggestion 
    if media.mime_type.startswith("video/"):
    ## how the f the other formats can be uploaded as video 
      button.append([InlineKeyboardButton("šļø Źį“É“į“į“į“ į“s į“ ÉŖį“į“į“ šļø",callback_data="rename_video")])
      button.append([InlineKeyboardButton("šļø į“į“É“į“ į“Źį“ į“į“ ŅÉŖŹį“š",callback_data="convert_file")])
      button.append([InlineKeyboardButton("š į“į“É“į“ į“Źį“ į“į“ į“ ÉŖį“į“į“šļø",callback_data="convert_video")])
    button.append([InlineKeyboardButton("šššššš ššš šššššššš ā",callback_data="cancel")])
 
    markup = InlineKeyboardMarkup(button)
    try:
      await m.reply_text(text,quote=True,reply_markup=markup,parse_mode="markdown",disable_web_page_preview=True)
    except Exception as e:
      log.info(str(e))
