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
               await m.reply_text("š¤­ Sorry Dude, You are **B A N N E D**. If you feel You are not guilty please contact owner")
               return
        except UserNotParticipant:
            await m.reply_text(
                text="**šµļøš”š¢š§ šŖš¢š„ššš”š šš”š¢šŖš\n\nš„³š±ššš š®šššš š©šššš š šŖššššššš šš ššš šš ššš & š¬šššš ššš š­ššš šŗšššššš š**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="š°šššš šššš ššššššš šššš°", url=f"https://t.me/{update_channel}")],
                  [ InlineKeyboardButton(text="š¬š±š¶š°šµ š¶š¼š¹ šØš³š³ šŖšÆšØšµšµš¬š³šŗš¬", url=f"https://t.me/UNI_MOVIES_BOX")]

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
               await m.reply_text("š¤­ Sorry Dude, You are **B A N N E D**. If you feel You are not guilty please contact owner")
               return
        except UserNotParticipant:
            await m.reply_text(
                text="**šµļøš”š¢š§ šŖš¢š„ššš”š šš”š¢šŖš\n\nš„³š±ššš š®šššš š©šššš š šŖššššššš šš ššš šš ššš & š¬šššš ššš š­ššš šŗšššššš š**",

                reply_markup=InlineKeyboardMarkup([

                    [ InlineKeyboardButton(text="š°šššš šššš ššššššš šššš°", url=f"https://t.me/{update_channel}")],

                  [ InlineKeyboardButton(text="š¬š±š¶š°šµ š¶š¼š¹ šØš³š³ šŖšÆšØšµšµš¬š³šŗš¬", url=f"https://t.me/UNI_MOVIES_BOX")]

 ])
            )
            return
    await m.reply_text(Translation.START_TEXT.format(m.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
            [
               [
                InlineKeyboardButton("š¬š¹š¾šøš½ š¾ššš š±š¾šš š²š·š°š½š½š“š»š¬", url=f"https://t.me/DB_ROBOTS")],
                   [ InlineKeyboardButton("š¬š¹š¾šøš½ š¾šš š°š»š» š¼š¾ššøš“š š²š·š»š¬", url=f"https://t.me/UNI_MOVIES_BOX")
                ],
                [
                    InlineKeyboardButton("šØāš¬ š³š“šš“š»š¾šæš“š š”ļø", url=f"https://t.me/Deeks_04_8")
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
