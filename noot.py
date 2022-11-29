from ast import alias
from time import time
import discord
import random
import time
import re
import requests
import wikipedia
from discord import FFmpegPCMAudio
from discord.ext import commands

dogruluk_liste = open("dosyalar/dogruluk.txt", "r", encoding="utf8").read().splitlines()
cesaretlik_liste = open("dosyalar/cesaretlik.txt", "r", encoding="utf8").read().splitlines()
fetis_liste = open("dosyalar/fetis.txt", "r", encoding="utf8").read().splitlines()
neyim_liste = open("dosyalar/neyim.txt", "r", encoding="utf8").read().splitlines()
ustunler_liste = open("dosyalar/ustunler.txt", "r", encoding="utf8").read().splitlines()
olumler_liste = open("dosyalar/olumler.txt", "r", encoding="utf8").read().splitlines()

api_key     = "9b0863c85435de3d00128b8b8177a357"
base_url    = "http://api.openweathermap.org/data/2.5/weather?"

token = open("token.txt", "r", encoding="utf8").read()
intents = discord.Intents.all()
client = commands.Bot(command_prefix=',', intents=intents)

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
        await ctx.send('",soru" yazdıktan sonra sorunu yazman gerek.')

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

@client.command(aliases=['truth', 'd'])
async def doğruluk(ctx):
    await ctx.send(f"{random.choice(dogruluk_liste)}")

@client.command(aliases=['dare', 'cesaretlik', 'c'])
async def cesaret(ctx):
    await ctx.send(f"{random.choice(cesaretlik_liste)}")

@client.command(aliases=['pipi'])
async def çük(ctx, kisi: str):
    boy = random.randint(0, 31)
    if boy == 31:
        await ctx.send(f"{kisi} kişisinin çükü **{boy}cm.** **Tebrik ederim.** :hot_face:")
    elif boy == 0:
        await ctx.send(f"{kisi} kişisinin çükü **{boy}cm.** :regional_indicator_l:")
    else:
        await ctx.send(f"{kisi} kişisinin çükü **{boy}cm.**")

@çük.error
async def çük_hata(ctx, hata):
    if isinstance(hata, commands.MissingRequiredArgument):
        boy = random.randint(0, 30)
        if boy == 31:
            await ctx.send(f"{ctx.message.author.mention} kişisinin çükü **{boy}cm.** **Tebrik ederim.** :hot_face:")
        elif boy == 0:
            await ctx.send(f"{ctx.message.author.mention} kişisinin çükü **{boy}cm.** :regional_indicator_l:")
        else:
            await ctx.send(f"{ctx.message.author.mention} kişisinin çükü **{boy}cm.**")

@client.command(aliases=['boob'])
async def meme(ctx, kisi: str):
    cup = ['A', 'B', 'C', 'D']
    width = random.randint(40, 90)
    boob_size = f"{random.choice(cup)}{width}"
    if boob_size == 'D90':
        await ctx.send(f"{kisi} kişisinin memesi **{boob_size}** **Tebrik ederim.** :hot_face:")
    elif boob_size == 'A40':
        await ctx.send(f"{kisi} kişisinin memesi **{boob_size}** :regional_indicator_l:")
    else:
        await ctx.send(f"{kisi} kişisinin memesi **{boob_size}**")

@meme.error
async def meme_hata(ctx, hata):
    if isinstance(hata, commands.MissingRequiredArgument):
        cup = ['A', 'B', 'C', 'D']
        width = random.randint(40, 90)
        boob_size = f"{random.choice(cup)}{width}"
        if boob_size == 'D90':
            await ctx.send(f"{ctx.message.author.mention} kişisinin memesi **{boob_size}** **Tebrik ederim.** :hot_face:")
        elif boob_size == 'A40':
            await ctx.send(f"{ctx.message.author.mention} kişisinin memesi **{boob_size}** :regional_indicator_l:")
        else:
            await ctx.send(f"{ctx.message.author.mention} kişisinin memesi **{boob_size}**")


@client.command()
async def domine(ctx, *, kisi: str):
    dominemi = random.randint(0, 1)
    if dominemi == 1:
        await ctx.send(f'{ctx.message.author.mention}, {kisi} kişisini **domine etmek** istiyor.')
    else:
        await ctx.send(f'{ctx.message.author.mention}, {kisi} tarafından **domine edilmek** istiyor.')

@domine.error
async def domine_hata(ctx, hata):
    if isinstance(hata, commands.MissingRequiredArgument):
        dominemi = random.randint(0, 1)
        if dominemi == 1:
            await ctx.send(f'{ctx.message.author.mention} **domine etmek** istiyor.')
        else:
            await ctx.send(f'{ctx.message.author.mention} **domine edilmek** istiyor.')

@client.command()
async def fetiş(ctx, kisi: str):
    await ctx.send(f"{kisi} adlı kullanıcının {random.choice(fetis_liste)} fetişi var.")

@fetiş.error
async def fetiş_hata(ctx, hata):
    if isinstance(hata, commands.MissingRequiredArgument):
        await ctx.send(f"{ctx.message.author.mention} adlı kullanıcının {random.choice(fetis_liste)} fetişi var.")

@client.command(aliases=['dg', 'birthday', 'doğum'])
async def doğumgünü(ctx, kisi: str):
    try:
        temiz_kisi = re.sub('\W+','', kisi)
        tarih = open(f"dosyalar/dogum_gunleri/{temiz_kisi}.txt", "r", encoding="utf8").read()
        await ctx.send(f"{kisi} adlı kullanıcının doğum günü: **{tarih}**")
    except IOError:
        await ctx.send("Doğum günü bulunamadı. Kendi doğum gününüzü eklemek istiyorsanız **,dge** komudunu kullanın.")

@doğumgünü.error
async def doğumgünü_hata(ctx, hata):
    if isinstance(hata, commands.MissingRequiredArgument):
        await ctx.send('Doğum gününü öğrenmek istediğiniz kişiyi **etiketleyin**.')

@client.command(aliases=['dge'])
async def doğumgünüekle(ctx, tarih: str):
    kisi = ctx.message.author.mention
    temiz_kisi = re.sub('\W+','', kisi)

    with open(f"dosyalar/dogum_gunleri/{temiz_kisi}.txt", "w") as file:
        file.write(tarih)
        await ctx.send("Doğum günün eklendi!")

@doğumgünüekle.error
async def doğumgünüekle_hata(ctx, hata):
    if isinstance(hata, commands.MissingRequiredArgument):
        await ctx.send('Doğum gününüzü yazın. (Örnek: 01/01/2001)')

@client.command()
async def ne(ctx, kisi: str):
    yuzdelik = random.randint(0, 100)
    if (yuzdelik == 100) or (yuzdelik == 0):
        await ctx.send(f"{kisi} **%{yuzdelik} {random.choice(neyim_liste)}.** **Tebrik ederim.**")
    else:
        await ctx.send(f"{kisi} **%{yuzdelik} {random.choice(neyim_liste)}.**")

@ne.error
async def ne_hata(ctx, hata):
    if isinstance(hata, commands.MissingRequiredArgument):
        yuzdelik = random.randint(0, 100)
        if (yuzdelik == 100) or (yuzdelik == 0):
            await ctx.send(f"{ctx.message.author.mention} **%{yuzdelik} {random.choice(neyim_liste)}.** **Tebrik ederim.**")
        else:
            await ctx.send(f"{ctx.message.author.mention} **%{yuzdelik} {random.choice(neyim_liste)}.**")

@client.command()
async def dr(ctx, kisi: str):
    await ctx.send(f"{kisi} - **Üstün {random.choice(ustunler_liste)}**")

@dr.error
async def dr_hata(ctx, hata):
    if isinstance(hata, commands.MissingRequiredArgument):
        await ctx.send(f"{ctx.message.author.mention} - **Üstün {random.choice(ustunler_liste)}**")

@client.command()
async def rulet(ctx):
    dead_channel = ctx.guild.get_channel(1013527760410509402)

    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        id_list = list(channel.voice_states.keys())

        victim_id = id_list[random.randint(0, len(channel.voice_states.keys())-1)]
        victim = await ctx.guild.fetch_member(victim_id)
    
        await ctx.send(f'**{victim.name}** vuruldu! :skull:')
        time.sleep(1.5)
        await victim.move_to(dead_channel)

        id_list = list(channel.voice_states.keys())
        if(len(channel.members) == 1):
            #await ctx.guild.voice_client.disconnect()
            for member in channel.members:
                await ctx.send(f"Ruleti kazanan **{member.name}**! :tada:")
    else:
        await ctx.send("Rulet oynamak için bir sesli kanalda olman gerek.")

@client.command()
async def reset(ctx):
    if(ctx.author.voice):
        await ctx.send("Rulet sıfırlanıyor...")

        reset_channel = client.get_channel(980089520982741032)
        current_channel = ctx.message.author.voice.channel

        for member in current_channel.members:
            await member.move_to(reset_channel)
    else:
        await ctx.send("Ruleti sıfırlamak için bir sesli kanalda olman gerek.")

@client.command(aliases=['ölüm'])
async def öl(ctx, kisi: str):
    await ctx.send(f"{kisi} {random.choice(olumler_liste)}")

@öl.error
async def öl_hata(ctx, hata):
    if isinstance(hata, commands.MissingRequiredArgument):
        await ctx.send(f"{ctx.message.author.mention} {random.choice(olumler_liste)}")

@client.command()
async def viki(ctx, *, arama: str):
    wikipedia.set_lang("tr")
    try:
        await ctx.send(f"**{wikipedia.page(arama).title}**\n{wikipedia.summary(arama, sentences=4)}\n<{wikipedia.page(arama).url}>")
    except:
        try:
            wikipedia.set_lang("en")
            await ctx.send(f"**{wikipedia.page(arama).title}**\n{wikipedia.summary(arama, sentences=4)}\n<{wikipedia.page(arama).url}>")
        except:
            await ctx.send("Aradığınız makale bulunmamakta.")

@client.command()
async def wiki(ctx, *, arama: str):
    wikipedia.set_lang("en")
    try:
        await ctx.send(f"**{wikipedia.page(arama).title}**\n{wikipedia.summary(arama, sentences=4)}\n<{wikipedia.page(arama).url}>")
    except:
        await ctx.send("Aradığınız makale bulunmamakta.")

@viki.error
async def viki_hata(ctx, hata):
    if isinstance(hata, commands.MissingRequiredArgument):
        await ctx.send("Aramak istediğin şeyi yazmayı unuttun.")

@wiki.error
async def wiki_hata(ctx, hata):
    if isinstance(hata, commands.MissingRequiredArgument):
        await ctx.send("Aramak istediğin şeyi yazmayı unuttun.")

@client.command()
async def ship(ctx):
    guild = client.get_guild(980089520521371689)

    uyeler = []
    for member in guild.members:
        if not member.bot:
            uyeler.append(member.name)

    await ctx.send(f"**{ctx.message.author.name}** :revolving_hearts: **{random.choice(uyeler)}**")

@client.command(aliases=['rship'])
async def randomship(ctx):
    guild = client.get_guild(980089520521371689)

    uyeler = []
    for member in guild.members:
        if not member.bot:
            uyeler.append(member.name)

    await ctx.send(f"**{random.choice(uyeler)}** :revolving_hearts: **{random.choice(uyeler)}**")

@client.command()
async def hava(ctx, *, sehir_adi: str):
    weather_data = requests.get(base_url + "appid=" + api_key + "&q=" + sehir_adi + "&lang=tr&units=metric").json()
    if weather_data["cod"] != "404": 

        main_data = weather_data["main"] 
        current_temperature = main_data["temp"]
        current_pressure = main_data["pressure"] 
        current_humidiy = main_data["humidity"] 

        curren_state_data = weather_data["weather"] 
        curren_state_description = curren_state_data[0]["description"] 

        wind_data = weather_data["wind"]
        wind_speed = wind_data["speed"]

        await ctx.send(f"**{sehir_adi.capitalize()} Hava Durumu**\n**Sıcaklık:** {round(current_temperature)}°C\n**Nem:** %{round(current_humidiy)}\n**Rüzgar Hızı:** {round(wind_speed)} km/s\n**Durum:** {curren_state_description}")

    else: 
        await ctx.send("Şehir bulunamadı.")

@client.command()
async def reaktör(ctx):
    await ctx.send("""Bir nükleer reaktör atomların bölünmesiyle çalışır. Genellikle bu işlemde bir izotop olan Uranyum-235 kullanılır. Bunun nedeni U-235'in belirli koşullar altında kolayca bölünebilir olmasıdır. Bir nötron, U-235'e ateşlenir böylelikle çarptığı U-235 iki küçük atoma ve iki ila üç ek nötrona bölünür. Bu bölünen nötronlar bir kısmı diğer U-235'lere çarparak daha fazla fisyona neden olur bu işleme zincirleme nükleer reaksiyon denir. Bu süreç ile yakılan U-235 sayesinde ısı ortaya çıkar. Reaktörde sirkülasyonda olan bir sıvı, ki genellikle bu sıvı bol ve ucuz olduğundan sudur, Bu ısı sayesinde buharlaşarak türbinleri çalıştırarak elektrik üretilir. Nükleer reaksiyonun doğru hızda gerçekleşmesini sağlamak için; reaktörler nükleer reaksiyonu hızlandıran, yavaşlatan veya kapatan sistemlere sahiptir. Bu sistemler genellikle Kadmiyum ve Boron gibi nötron emici malzemelerden yapılmış kontrol çubukları ile yapılır. İşte bu kontrol çubukları senin boşaltım sisteminin önemli bir elamanı olan götüne girsin. Bu solda bulunan cümle gözüne direkt batmasın diye şimdi birazcık saçmalayacağım. Dünyanın etrafında bulunan Van Allen kuşağı nedeniyle astronotların bir yılda aldıkları radyasyonun sıradan bir sigara kullanıcısının aldığı radyasyondan daha az olduğunu biliyor muydun?""")

@client.command()
async def osman(ctx):
    await ctx.send("OSMAN ANNENİ WISHLISTIME EKLEDİM BİR DAHA BU GRUPTA SİKİK SOKUK GÖNDERİLER PAYLAŞIRSAN SATIN ALIRIM ÖKSÜZ KALIRSIN OROSPU ÇOCU")

@client.command()
async def vibe(ctx, kisi: str):
    if random.randint(0, 1) > 0:
        await ctx.send("https://pbs.twimg.com/media/EJ1rhm9X0AQJmFg.jpg")
    else:
        await ctx.send("https://i3.sndcdn.com/avatars-l6jJJKIriREve9oW-zoUbDg-t500x500.jpg")

@vibe.error
async def vibe_hata(ctx, hata):
    if isinstance(hata, commands.MissingRequiredArgument):
        if random.randint(0, 1) > 0:
            await ctx.send("https://i.redd.it/rm04m34vr9x31.jpg")
        else:
            await ctx.send("https://i3.sndcdn.com/avatars-l6jJJKIriREve9oW-zoUbDg-t500x500.jpg")

@client.command()
async def horny(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/589444279148085259/703779922107433090/EWF4vdYUwAQaiV3.png")

@client.command()
async def hornyno(ctx):
    await ctx.send('https://i.kym-cdn.com/photos/images/facebook/001/845/064/685')

@client.command()
async def simp(ctx):
    await ctx.send("https://i.redd.it/xdz4luu84n841.jpg")

@client.command()
async def mehter(ctx):
    await ctx.send("Ceddin deden neslin baban\nHep kahraman Türk milleti\nOrduları pek çok zaman\nVermiştiler dünya'ya şan\n\n<@451230172553936897>")

@client.command(aliases=['varyok'])
async def vy(ctx, *, soru):
    if random.randint(0, 1) > 0:
        embed = discord.Embed(title='VAR MI YOK MU?', description=f'{soru}', color=0xff7b00)
        embed.set_image(url='https://media.discordapp.net/stickers/1034931166622519296.webp?size=240')
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title='VAR MI YOK MU?', description=f'{soru}', color=0x2913cf)
        embed.set_image(url='https://media.discordapp.net/stickers/1041693517774340186.webp?size=240')
        await ctx.send(embed=embed)

@vy.error
async def vy_hata(ctx, hata):
    if isinstance(hata, commands.MissingRequiredArgument):
        await ctx.send('",vy" yazdıktan sonra sorunu yazman gerek.')



client.run(token)