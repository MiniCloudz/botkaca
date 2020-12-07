
from pyrogram import Client, Message, Filters
from os.path import join as os_path_join
from bot import COMMAND, LOCAL, CONFIG
from bot.plugins import thumbnail_video
 
@Client.on_message(Filters.command("savethumb") & Filters.incoming)
async def set(client, message):
    if message.reply_to_message is not None:
        name = str(message.from_user.id) + "/" + ".jpg"
        thumbnail_path = os_path_join(CONFIG.ROOT, CONFIG.WORKDIR, name)
 
        await message.reply_to_message.download(
            file_name = thumbnail_path
        )
        await thumbnail_video.set(thumbnail_path)
        await message.reply_text("✅ Successfully saved thumbnail", quote=True)
    else:
        await m.reply_text(text="Reply to a photo to set custom thumbnail")
 
@Client.on_message(Filters.command(COMMAND.RESET_THUMBNAIL))
async def reset(client : Client, message: Message):
 
    name = str(message.from_user.id) + "/" + ".jpg"
    thumbnail_path = os_path_join(CONFIG.ROOT, CONFIG.WORKDIR, name)
    if os_path_join.exists(thumbnail_path):
       await thumbnail_video.reset(thumbnail_path)
       await message.reply_text("✅ Thumbnail Deleted successfully", quote=True)
    else:
      await message.reply_text("No thumbnail found 🤷‍♂️")
