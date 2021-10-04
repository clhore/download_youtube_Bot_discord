# encoding: utf-8

# library
import discord
from discord.ext import commands
import time
import os

# import custom module
from mymodule import YTdowload as YTd, JSON, customCrono, quickstart, DriveFile, mix

if __name__ == '__main__':
    # login gmail
    quickstart.login()

    # variable
    config = JSON.JSON('config.json')
    conf = config.read()
    TOKEN = conf['token']
    prefix = conf['prefix'] # !
    id_folder = conf['id_folder']
    list_file_id = conf['list_file_id']
    tmpDirectory = 'video'

    # config prefix bot
    bot = commands.Bot(command_prefix=prefix)


    @bot.command(name='commands')
    async def COMMANDS(ctx):
        try:
            command = f"""\n
            Commands:
            **Download video**     >>     !VD [link],[link],[etc]
            **Download audio**     >>     !AU [link],[link],[etc]
            **Delete file drive**     >>     !delete [password]
            """
            await ctx.send(command)
        except Exception as e:
            print(e)

    @bot.command(name='AU')
    async def YTdowloadAudio(ctx, Url: str):
        try:
            tmp = customCrono.CronoTime()
            tmp.start()
            Url = Url.split(',')
            video = YTd.YTdowload(url=Url, conf=config, file=f'{tmpDirectory}//')
            listFile = video.lista(mode='audio')
            tmp = tmp.stop()
            time.sleep(0.5)
            for nameFile in listFile:
                sizeFile = os.stat(nameFile).st_size
                # print(sizeFile)
                if sizeFile < 7500000:
                    await ctx.send(file=discord.File('%s' % nameFile))
                else:
                    nameFile = nameFile.split('//')
                    rutaFile = nameFile[0]
                    nameFile = nameFile[1]

                    # config session
                    drive = DriveFile.DriveFile('credentials_module.json')
                    drive.uploadFile(f'{rutaFile}\\{nameFile}', id_folder)
                    # extract file info
                    infoFile = drive.searchFile(f"title contains '{nameFile}' and trashed = false", mode='link')
                    list_file_id.append(infoFile[0]['id'])
                    # link drive file
                    link = infoFile[0]['link']
                    await ctx.send(f'El achivo sobrepasa los 8M | {link}')
            # send message
            await ctx.send(str(tmp))

        except Exception as e:
            await ctx.send('[*] Error') # send message
            print(e) # print error code

    @bot.command(name='VD')
    async def YTdowloadVideo(ctx, Url: str):
        try:
            tmp = customCrono.CronoTime()
            tmp.start()
            Url = Url.split(',')
            video = YTd.YTdowload(url=Url, conf=config, file=f'{tmpDirectory}//')
            listFile = video.lista(mode='video')
            tmp = tmp.stop()
            time.sleep(0.5)
            for nameFile in listFile:
                sizeFile = os.stat(nameFile).st_size
                # print(sizeFile)
                if sizeFile < 7500000:
                    await ctx.send(file=discord.File('%s' % nameFile))
                else:
                    nameFile = nameFile.split('//')
                    rutaFile = nameFile[0]
                    nameFile = nameFile[1]

                    # config session
                    drive = DriveFile.DriveFile('credentials_module.json')
                    drive.uploadFile(f'{rutaFile}\\{nameFile}', id_folder)
                    # extract file info
                    infoFile = drive.searchFile(f"title contains '{nameFile}' and trashed = false", mode='link')
                    list_file_id.append(infoFile[0]['id'])
                    # link drive file
                    link = infoFile[0]['link']
                    await ctx.send(f'El achivo sobrepasa los 8M | {link}')

            await ctx.send(str(tmp)) # send message
            config.write(conf) # write file
            #mix.fileRemove(listFile)

        except Exception as e:
            await ctx.send('[*] Error')
            print(e)

    @bot.command(name='delete')
    async def deleteFile(ctx, password: str):
        if password == conf["password"]:
            # config session
            drive = DriveFile.DriveFile('credentials_module.json')
            try:
                if list_file_id != list():
                    for file in list_file_id:
                        drive.deleteFile(file) # delete file
                    
                    # reset list_file_id
                    list_file_id.pop()
                    config.write(conf) # write file

                # delete tmpDirectory
                mix.directoryRemove(tmpDirectory)

                # send message
                await ctx.send('file deleted')
            
            except Exception as e:
                print(e) # print error code

                if list_file_id is not list():
                    list_file_id.pop() # reset list_file_id
                    config.write(conf)  # write file

                # send message
                await ctx.send('file not deleted')

        else:
            await ctx.send('user or password not valid')
    # run bot
    bot.run(TOKEN)