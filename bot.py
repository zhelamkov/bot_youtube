from telethon import TelegramClient
from telethon import events, Button
import telethon
import pafy
import re
import os
from time import sleep
##############################################
api_id = <>
api_hash = <>
token = <>
chat = <name>
chat_for_bot=<chat name>
##############################################
client = TelegramClient(<chat name>, api_id, api_hash)
bot = TelegramClient('@<name>', api_id, api_hash).start(bot_token=token)
##############################################










@bot.on(events.NewMessage)
async def handler_new_message(event):
    global chtid
    chtid = event.message.chat_id
    print(chtid)
    if 'youtu' in event.message.text:
        #Добавить проверку ссылки
        await doit(event.message.text)
    else:
        await bot.send_message(chtid, 'What u gonna do?', buttons=[
    [Button.inline('FAQ', b'help'), Button.inline('Connect',b'connect')],
    [Button.inline('Download from Youtube!', b'doit')]])
        @bot.on(events.CallbackQuery(data=re.compile(r'[\w]+')))
        async def callback(event):
            choice=(event.data).decode('utf-8')
            if choice == "doit":

                
                async with bot.conversation(chtid) as conv:
                    await conv.send_message('Send me a youtube link!')

                    try:
                        ssilka =await  conv.get_response()
                        if 'youtu' in ssilka.message:
                            url =ssilka.message
                            await doit(url)
                        else:
                            await conv.send_message('Not a link')


                    except Exception as exx:
                        await bot.send_message(chtid,exx)



            elif choice == "help":
                await event.answer('Help', alert=True)
            elif choice == "connect":
                await event.answer('Connect', alert=True)


async def callback(current, total):
    a = int((current / total) * 100)
    print(a)

async def doit(url):
    try:
        video = pafy.new(url)
        streams = video.streams
        global vibor
        vibor = dict(zip([i + 1 for i in range(len(streams))], streams))
        sp_vibora = 'Filename: ' + video.title + '\n' + '\n' + 'Choose video or audio: '
        Best_a = video.getbestaudio()
        vibor_vid=dict(vibor)
        vibor[len(streams) + 1] = Best_a
        btn=[[Button.inline(f'{vibor[i].resolution}  size:{(vibor[i].get_filesize()/ 1024**2):.1f}Mb',f'{i}')] for i in sorted((vibor_vid.keys()))]
        btn.append([Button.inline(f'Audio    size:{(vibor[len(streams) + 1].get_filesize()/ 1024**2):.1f}Mb',f"{len(streams) + 1}")])
        await bot.send_message(chtid, sp_vibora , buttons=btn)

        @bot.on(events.CallbackQuery(data=re.compile(r'\d')))
        async def handler(event):
            global chs_v
            chs_v= int(event.data.decode('utf-8'))
            best = vibor[chs_v]
            if not os.path.exists('new_tmp'):
                os.mkdir('new_tmp')  # создаем папку для временного хранения файла
            print('nachalo')
            best.download("new_tmp/1." + best.extension)
            print('done')

            ffile = await bot.upload_file("new_tmp/1." + best.extension,part_size_kb=512,progress_callback=callback)
            print('done2')

            await bot.send_file(chat_for_bot, ffile, force_document=True)
            print('done3')

            if os.path.isfile("new_tmp/1." + best.extension):  # Всю папочку удаляем
                hole = os.listdir('new_tmp')
                for i in hole:
                    os.remove(f"new_tmp/{i}")
                os.rmdir("new_tmp")
                print('Удалено')

            else:
                print('Проблемы с удалением         файла')


    except Exception as err:
        await bot.send_message(chtid, err)

            with open("new_tmp/1." + best.extension, 'rb') as sv:
                await client.send_file("@<name>", "new_tmp/1." + best.extension, progress_callback=callback)
                a = bot.get_messages('@<chat name>', limit=1)


                print(a[0].media)

        
                    file_id = telethon.utils.pack_bot_file_id(a[0].media)
            print(file_id)



            await bot.send_file("@<chat name>", file=file_id)

            if os.path.isfile("new_tmp/1." + best.extension):  # Всю папочку удаляем
                hole = os.listdir('new_tmp')
                for i in hole:
                    pass
                    os.remove(f"new_tmp/{i}")
                os.rmdir("new_tmp")
                print('Удалено')







##############################################

if __name__ == '__main__':
    client.start(password='PWD')

    client.run_until_disconnected()
##############################################


