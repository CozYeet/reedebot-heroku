import discord

client = discord.Client()

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
	
await client.change_status(game=discord.Game(name='REEDE © SERVERS '))

client.run('NDEyNjI5OTI5Mzc3NzkyMDIw.DWNDLA.0Goz2hh3TaWvW2t5hC4Z561WUlA')
