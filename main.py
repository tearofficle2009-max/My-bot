import os
from pyrogram import Client, filters, enums
import database
import g4f

# Render Environment Variables
api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")
admin_id = int(os.environ.get("ADMIN_ID", 0))

app = Client("family_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
database.init_db()

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    sticker_id = "CAACAgIAAxkBAAELo..." # ကိုယ့် Sticker ID ထည့်ပါ
    await message.reply_sticker(sticker_id)
    await message.reply("မင်္ဂလာပါ! ကျွန်တော်က AI Bot ပါ။")

@app.on_message(filters.command("ask") & filters.private)
async def ai_handler(client, message):
    await client.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    query = message.text.split(None, 1)[1]
    response = g4f.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": query}])
    await message.reply(response)

@app.on_message(filters.command("setwelcome") & filters.group)
async def set_welcome(client, message):
    if message.reply_to_message and message.reply_to_message.video:
        vid_id = message.reply_to_message.video.file_id
        database.save_video(message.chat.id, vid_id)
        await message.reply("✅ Welcome Video သတ်မှတ်ပြီးပါပြီ။")

@app.on_message(filters.new_chat_members)
async def welcome_member(client, message):
    vid_id = database.get_video(message.chat.id)
    if vid_id:
        await message.reply_video(video=vid_id, caption="အဖွဲ့ထဲကို ကြိုဆိုပါတယ်။")

@app.on_message(filters.command("autopost") & filters.user(admin_id))
async def auto_post(client, message):
    channel_id = -100xxxxxxxxxx # Channel ID ထည့်ပါ
    await client.send_message(channel_id, "Channel အတွက် အလိုအလျောက် ပို့စ်တင်ခြင်း!")

app.run()
