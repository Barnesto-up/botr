import discord
import datetime
import typing
import random
from discord.ext import commands

# Префикс

bot = commands.Bot(command_prefix = '!')
bot.remove_command('help')
token = 'NjU1NDc2NjQxMDQ0MzY1MzMx.Xiwc5Q.os9KNgyazuLlz30XGBjtt7aUDyw'

@bot.event

async def on_ready():
    await bot.change_presence(status= discord.Status.idle, activity=discord.Game('В разработке'))
    print( 'Бот подключен...' )

#ВЫДАЧА РОЛИ
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(670768628815364123)

    role = discord.utils.get(member.guild.roles, id=668902007515381772)
    await member.add_roles(role)
    await channel.send(embed= discord.Embed(description= f'```Пользователь {member. mention} получил свою первую роль на сервере. ```', color=0x0c0c0c))


# Логи

# Изменения сообщения
@bot.event
async def on_message_edit(before, after):
    channel = bot.get_channel(670768628815364123)
    if before.author == bot.user:
        return
    if before.content is None:
        return
    elif after.content is None:
        return
    message_edit = discord.Embed(colour = 0x0c0c0c,
                                 description=f"**{before.author} Изменил сообщение в канале  {before.channel}** "
                                             f"\nСтарое сообщение: {before.content}"
                                             f"\n\nНовое сообщение: {after.content}",timestamp=before.created_at)
    
    await channel.send(embed=message_edit)

    return    

    print( 'Были использованы логи изменений сообщений.' )


# Удаление сообщений
@bot.event
async def on_message_delete(message):
    channel = bot.get_channel(670260939249156096)
    if message.content is None:
        return
    embed = discord.Embed(colour = 0x0c0c0c, description=f"**{message.author} Удалил сообщение в канале {message.channel}** \n{message.content}",timestamp=message.created_at)

    await channel.send(embed=embed)

    return

    print( 'Пользователь удалил сообщение.' )

# Оповещение о покинувших людях

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(670260939249156096)

    embed = discord.Embed(colour = 0x0c0c0c, description=f"``{member}`` Вышел с сервера")

    await channel.send(embed=embed)

    return

    print( 'Пользователь покинул сервер.' )


#ПРАВИЛА
@bot.command()
async def rules( ctx ):
        
    emb = discord.Embed( title = ':circus_tent: Правила Сервера' )
    emb.set_footer( text = '''ХЕХЕБОЙ''', icon_url = '''https://www.worldtimeserver.com/img/dst/dst-2-3.png''')

    emb.add_field( name = '**:pencil: Правила:**', value = '''**1.0 Запрещен мат в любом виде.
1.1 Запрещены провокации людей на нарушение правил.
1.2 Спам и флуд в любом виде запрещён.
1.3 Реклама или упоминание сторонних проектов/сайтов запрещёна.
1.4 Запрещено потребительское отношение и хамское поведение от игроков в сторону администрации. Администрация действует в рамках правил, помогает игрокам, если на то есть необходимость
1.5 Запрещено оскорбление/затрагивание родителей/родственников. 
1.6 Запрещается разжигание межнациональной розни, затрагивание религии и конфликты на этой почве 
1.7 Запрещено попрошайнечество. 
1.8 Администрация сервера имеет право забрать/добавить роль любому Участнику сервера.
1.9 Администрация всегда права и её действия не подлежат обсуждению.
2.0 Запрещено работать без доступа к работе.
2.1 Запрещено банить/мутить/кикать без причины. 
:no_entry: Если Вы не знаете правил, то это не освобождает Вас от ответственности.**''')

    await ctx.send( embed = emb ) 

    print( 'Была использована команда > !rules' )

# Пинг
@bot.command()   
async def ping( ctx ):
    await ctx.send(embed = discord.Embed(description= f'''Понг!''', color = 0x0c0c0c))

    print( 'Была использована команда > !ping' )

# Кинг
@bot.command()   
async def king( ctx ):
    await ctx.send(embed = discord.Embed(description= f''':gorilla: Конг!''', color = 0x0c0c0c)) 

    print( 'Была использована команда > !king' )


# Орел-решка
@bot.command()
async def coin( ctx ):
    coins = [ 'орел', 'решка' ]
    coins_r = random.choice( coins )
    coin_win = 'орел'

    if coins_r == coin_win:
        await ctx.send(embed = discord.Embed(description= f''':tada: { ctx.message.author.name }, выиграл! 
            Тебе повезло у вас: ``{ coins_r }``''', color = 0x0c0c0c))

    if coins_r != coin_win:
        await ctx.send(embed = discord.Embed(description= f''':thumbsdown:  { ctx.message.author.name }, проиграл! 
            Тебе не повезло у вас: ``{ coins_r }``''', color = 0x0c0c0c))  

        print( 'Была использована команда > !coin' ) 


# Очистка чата
@bot.command()
@commands.has_permissions( administrator = True)

async def clear(ctx,amount= 100):

    await ctx.channel.purge( limit = amount )
    channel = bot.get_channel(670768628815364123)
    await channel.send(embed = discord.Embed(description = f''f' Удалено ``{amount}`` сообщений''', color=0x0c0c0c))



# Кик
@bot.command()
@commands.has_permissions( administrator = True)

async def kick(ctx, member: discord.Member, *, reason= None):
    await ctx.channel.purge(limit = 1)

    await member.kick(reason = reason)
    await ctx.send(f'Выгнали { member. mention }')



# Бан
@bot.command()
@commands.has_permissions( ban_members = True )

async def ban( ctx, member: discord.Member, *, reason = None):
    await ctx.channel.purge( limit = 1)
    channel = bot.get_channel(670768628815364123)

    await member.ban( reason = reason )
    await channel.send(embed = discord.Embed(description = f'''Пользователь ``{member.mention}``  был заблокирован по решению администрации.''', color=0x0c0c0c))



# Хелп
@bot.command()
async def help( ctx):
    emb = discord.Embed( title = ':gear: Навигация по командам' )
    emb.set_footer( text = '''Pyher ''',
    icon_url = '''http://cdn01.ru/files/users/images/07/d6/07d617338bb7402be066ddb567ee0c8d.jpg''')
    emb.set_thumbnail( url = '''http://cdn01.ru/files/users/images/07/d6/07d617338bb7402be066ddb567ee0c8d.jpg''' )
    
    emb.add_field( name = '**Модули:**', value = 
    '''**:wrench: Информация:**
    !serverinfo, !profile, !rules, !avatar

    **:notes: Музыка:**
    +clear, +leave, +pause, +play, +skip

    **:construction_site: Экономика:**
    !delays, !works, !work, !balance, !top, !br, !pay

    **:camera: Весёлости:**
    !coin, !ping, !king''')
    await ctx.author.send( embed = emb )
    await ctx.send(embed = discord.Embed(description = f'''**:rocket: Я выслал тебе команды.**''', colour = 0x0c0c0c))



#time
@bot.command()
async def time(ctx):
    emb = discord.Embed(colour= discord.Color.green(), url= 'https://www.timeserver.ru')
    
    emb.set_author(name= bot.user.name, icon_url=bot.user.avatar_url)
    emb.set_footer(text= 'Если у вас время по МСК, то к этому добавляйте +1 час', icon_url=ctx.author.avatar_url)
    emb.set_thumbnail(url='https://www.worldtimeserver.com/img/dst/dst-2-3.png')

    now_date = datetime.datetime.now()
    emb.add_field(name='Time', value='{}'.format(now_date))

    await ctx.send( embed = emb ) 

#АЙДИ
@bot.command()
async def id( ctx,member: discord.Member ): 
    
    embed = discord.Embed(colour = 0x0c0c0c, description=f'''Пользователь: {member.mention}
        ID: {member.id}''')
    await ctx.channel.purge( limit = 1)
    await ctx.author.send( embed = embed )

    print( '[!] Была использована команда > !id' ) 

# Аватар
@bot.command()

async def ava(ctx, member : discord.Member = None):

    user = ctx.message.author if (member == None) else member

    embed = discord.Embed(title=f'Аватар пользователя {user}', color= 0x0c0c0c)

    embed.set_image(url=user.avatar_url)

    await ctx.send(embed=embed) 



#mute
@bot.command()
@commands.has_permissions( ban_members = True )

async def mute( ctx, member: discord.Member ):

    mute_role = discord.utils.get(member.guild.roles, id = 670768628815364123)

    await member.add_roles( mute_role )
    await ctx.send(embed = discord.Embed(description = f'Пользователю {member.mention} был ограничен доступ к чатам. ', color=0x0c0c0c))


#userinfo
@bot.command(pass_context=True)
async def userinfo(ctx, Member: discord.Member):
    roles = (role for role in Member.roles )
    emb = discord.Embed(title= 'Информация о игроке.'.format(Member.name), description=f"Участник зашёл на сервер: {Member.joined_at.strftime('%b %#d, %Y')}\n\n "
        f"Имя: {Member.name}\n\n"
        f"Никнейм: {Member.nick}\n\n"
        f"Статус: {Member.status}\n\n"
        f"ID: {Member.id}\n\n"
        f"Высшая роль: {Member.top_role}\n\n",color=0xff0000, timestamp=ctx.message.created_at)

    emb.set_thumbnail(url= Member.avatar_url)
    emb.set_footer(icon_url= Member.avatar_url)
    emb.set_footer(text='Команда вызвана: {}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)
    print('Была визвана команда > !userinfo')


#unmute
@bot.command()
@commands.has_permissions( administrator = True) 

async def unmute( ctx, member: discord.Member ):   

    mute_role = discord.utils.get(member.guild.roles, id = 670768628815364123)

    await member.remove_roles( mute_role )
    await ctx.send(embed = discord.Embed(description = f'Пользователю {member.mention} был вернут доступ к чатам. ', color=0x0a0c0c))

# Работы

@bot.command()
async def works( ctx ):
        
    emb = discord.Embed( title = ':construction_site:  Экономика' )
    emb.set_footer( text = '''Лев | Разработчик Падший Дух''', icon_url = '''https://cdn.discordapp.com/avatars/668883162419691531/725ba1cef8df5ed61a6d9a7676308e49.png?size=512''')

    inline = False
    emb.add_field( name = '**:helmet_with_cross: Работа:**', value = '''**1. Дворник :broom: 
2. Почтальон :mailbox_closed:
3. Продавец :label: 
4. Таксист :oncoming_taxi: 
5. Строитель :hammer_pick: 
6. Учитель :books:
7. Консультант :bellhop: (Нужен доступ)
8. Фотограф :camera: (Нужен доступ)
9. Адвокат :scales: (Нужен доступ)
10. Менеджер :briefcase: (Нужен доступ)**''' )
    emb.add_field( name = '**:dollar: Прибыль:**', value = '''**1. От 0 :gem: до 1 :gem:
2. От 1 :gem: до 2 :gem:
3. От 2 :gem: до 3 :gem:
4. От 3 :gem: до 4 :gem:
5. От 4 :gem: до 5 :gem:
6. От 6 :gem: до 7 :gem:
7. От 7 :gem: до 8 :gem:
8. От 8 :gem: до 9 :gem:
9. От 9 :gem: до 10 :gem:
10. От 10 :gem: до 11 :gem:**''') 

    await ctx.send( embed = emb ) 

    print( 'Была использована команда > !works' )


#Задержки
@bot.command()
async def delays( ctx ):
        
    emb = discord.Embed( title = ':construction_site:  Экономика' )
    emb.set_footer( text = '''''', icon_url = '''https://cdn.discordapp.com/avatars/668883162419691531/725ba1cef8df5ed61a6d9a7676308e49.png?size=512''')

    inline = False
    emb.add_field( name = '**:helmet_with_cross: Работа:**', value = '''**1. Дворник :broom: 
2. Почтальон :mailbox_closed:
3. Продавец :label: 
4. Таксист :oncoming_taxi: 
5. Строитель :hammer_pick: 
6. Учитель :books:
7. Консультант :bellhop: (Нужен доступ)
8. Фотограф :camera: (Нужен доступ)
9. Адвокат :scales: (Нужен доступ)
10. Менеджер :briefcase: (Нужен доступ)**''' )
    emb.add_field( name = '**:hourglass: Задержка:**', value = '''** 1. Задержка 15 минут
2. Задержка 25 минут
3. Задержка 35 минут
4. Задержка 45 минут
5. Задержка 55 минут
6. Задержка 65 минут
7. Задержка 75 минут
8. Задержка 85 минут
9. Задержка 95 минут
10. Задержка 110 минут**''') 

    await ctx.send( embed = emb ) 

    print( 'Была использована команда > !delays' )

#бутилка
@bot.command()
async def bottle(ctx, amount: typing.Optional[int] = 99, *, liquid="Борджоми"):
    await ctx.send('{} бутылок {} уже едут к тебе!'.format(amount, liquid))


#рандом
@bot.command()
async def kill( ctx, member: discord.Member ):
    coins = [ 'умер', 'выжил' ]
    coins_r = random.choice( coins )
    coin_win = 'выжил'

    if coins_r == coin_win:
        await ctx.send(embed = discord.Embed(description= f''':rotating_light: Полиция подоспела и {member.mention} выжил.''',color = 0x0c0c0c))

    if coins_r != coin_win:
        await ctx.send(embed = discord.Embed(description= f''':knife: {member.mention} был зарезан...''', color = 0x0c0c0c))  

        print( '[!] Была использована команда > !kill' )




# Включение
bot.run( 'token' )
