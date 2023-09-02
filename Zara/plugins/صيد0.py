import telethon
from telethon import events
from telethon.sync import functions
from telethon import TelegramClient
StrPython = TelegramClient("c-h-r", 12297551, "9d3fd6a2c52c6b01312e02a3abf9999b") 
StrPython.start()
StrPython.send_message("me","اهلا بك في تشيكرنا 😁.\nلتثبيت على يوزر : حجز + معرف\nمثل : حجز @ASSSS")
@StrPython.on(
events.NewMessage(
outgoing=True, pattern=r"حجز"))
async def StrPy(event):
        clicks = 1
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        
        username = str(msg[0])
        
        await event.reply(f"Done start - @{username}")
        awai = await StrPython.send_message(event.chat_id,f'hi.')
        
        while True:
                clicks += 1
                await awai.edit(f'Clicks The User Now : {clicks}')
                try:
                    await StrPython(GetPeerDialogsRequest(peers=[username]))
                except:
                    try:
                        await StrPython(functions.account.UpdateUsernameRequest(username=username))           
                        await StrPython.send_file(event.chat_id, "https://t.me/hvvhh",caption=f'''
Good evening, chief 🗽
⌯ User ⤷ @{username}
⌯ Save ⤷ Account
⌯ Clicks ⤷ {clicks}
⌯ Program the bot : @HvvHH''')
                        await StrPython.send_message(event.chat_id,"New Username 😁🗽:\n[Hayder](t.me/hvvhh)")
                        break
                    
                    except telethon.errors.rpcerrorlist.UsernameInvalidError:
                    	await StrPython.send_message(event.chat.id,f"User is band 🥴 : {username}")
                    	break
                    except Exception as error:
                    	
                    	if "wait" in str(error):
                    	  	await StrPython.send_message(event.chat.id,f"Flood - 1500 ☠️.")
                    	  	
                    	if "is already taken" in str(error):
                    	    continue
                    	if "The username is not different from the current username" in str(error):
                    		await StrPython.send_message(event.chat_id,f"An error occurred, and because of the error, the scan was stopped ")
                    		
                    		break
                    	else:
                    		await StrPython.send_message(event.chat_id, f'''
Err: {error}
User is Error : {username}''')
                    		break
    
                        
print("Run")
StrPython.run_until_disconnected()
