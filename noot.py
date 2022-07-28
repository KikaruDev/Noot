import discord
import random
from discord.ext import commands

dogruluk_liste = open("dosyalar/dogruluk.txt", "r", encoding="utf8").read().splitlines()
cesaretlik_liste = open("dosyalar/cesaretlik.txt", "r", encoding="utf8").read().splitlines()
token = open("token.txt", "r", encoding="utf8").read()

client = commands.Bot(command_prefix=',')
embed = discord.Embed()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Ölümlülerin Ruhuyla'))
    print("Noot noot!")

@client.event
async def on_command_error(ctx, hata):
    if isinstance(hata, commands.CommandNotFound):
        await ctx.send("Böyle bir komut yok.")

@client.command()
async def selam(ctx):
    await ctx.send(f"Selam {ctx.message.author.mention}!")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! Gecikme {round(client.latency * 1000)}ms.')

@client.command()
async def soru(ctx, *, soru):
    cevaplar = [
        'Evet.', 'Hayır.',
        'Ölümüne kadar evet.', 'Bu soruyu cevaplamasam daha iyi olur.', 'Kesinlikle!',
        'Sanırsam hayır.', 'Şüphesiz.', 'Tabii ki de hayır.', 'Pek emin değilim.',
    ]

    await ctx.send(f"""**Soru:** "{soru}"\n**Cevap:** {random.choice(cevaplar)}""")

@soru.error
async def soru_hata(ctx, hata):
    if isinstance(hata, commands.MissingRequiredArgument):
        await ctx.send('",soru" yazdıktan sonra sorunu yazman gerek."')

@client.command(aliases=['random', 'roll', 'dice', 'rastgele'])
async def zar(ctx, sayi1: int, sayi2: int):
    if sayi2 > 10000:
        await ctx.send(f"**{random.randint(sayi1, 9999)}**")
    else:
        await ctx.send(f"**{random.randint(sayi1, sayi2)}**")

@zar.error
async def zar_hata(ctx, hata):
    if isinstance(hata, commands.MissingRequiredArgument):
        await ctx.send(f"**{random.randint(1, 6)}**")

@client.command(aliases=['gurup'])
async def group(ctx):
    await ctx.send(f"ATTENTION!!!! Masturbation party is gonna start in 5 minutes! ATTENTION!!!!")

@client.command(aliases=['truth'])
async def doğruluk(ctx):
    await ctx.send(f"{random.choice(dogruluk_liste)}")

@client.command(aliases=['dare', 'cesaretlik'])
async def cesaret(ctx):
    await ctx.send(f"{random.choice(cesaretlik_liste)}")

@client.command(aliases=['yarak'])
async def yarrak(ctx, kisi: str):
    boy = random.randint(0, 31)
    if boy == 31:
        await ctx.send(f"{kisi} kişisinin yarrağı **{boy}cm.** **Tebrik ederim.** :hot_face:")
    elif boy == 0:
        await ctx.send(f"{kisi} kişisinin yarrağı **{boy}cm.** **Tebrik ederim.** İstersen ,am komutunu dene. :pinching_hand:")
    else:
        await ctx.send(f"{kisi} kişisinin yarrağı **{boy}cm.**")

@yarrak.error
async def yarrak_hata(ctx, hata):
    if isinstance(hata, commands.MissingRequiredArgument):
        boy = random.randint(0, 30)
        if boy == 31:
            await ctx.send(f"{ctx.message.author.mention} kişisinin yarrağı **{boy}cm.** **Tebrik ederim.** :hot_face:")
        elif boy == 0:
            await ctx.send(f"{ctx.message.author.mention} kişisinin yarrağı **{boy}cm.** **Tebrik ederim.** İstersen ,am komutunu dene. :pinching_hand:")
        else:
            await ctx.send(f"{ctx.message.author.mention} kişisinin yarrağı **{boy}cm.**")

@client.command()
async def domine(ctx, *, kisi: str):
    dominemi = random.randint(0, 1)
    if dominemi == 1:
        await ctx.send(f'{ctx.message.author.mention}, {kisi} kişisini **domine etmek istiyor.**')
    else:
        await ctx.send(f'{ctx.message.author.mention}, {kisi} tarafından **domine edilmek istiyor.**')

@domine.error
async def domine_hata(ctx, hata):
    if isinstance(hata, commands.MissingRequiredArgument):
        dominemi = random.randint(0, 1)
        if dominemi == 1:
            await ctx.send(f'{ctx.message.author.mention} **domine etmek istiyor.**')
        else:
            await ctx.send(f'{ctx.message.author.mention} **domine edilmek istiyor.**')

client.run(token)