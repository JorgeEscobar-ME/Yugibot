import discord
import random
import pandas as pd
from discord.ext import commands

token =""
bot = commands.Bot(command_prefix = '!', intents=discord.Intents.all())

aTDG = pd.read_excel('sobres.xlsx', sheet_name=0)
bLOD = pd.read_excel('sobres.xlsx', sheet_name=1)
prompack1='prompack1.xlsx'
hojaprompack1 = pd.read_excel(prompack1, sheet_name='Sheet1')
hojaprompack2 = pd.read_excel(prompack1, sheet_name='Hoja1')
w = 'prueba.xlsx'
hoja = pd.read_excel(w)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='Nyaa!~ owo'))
    print('Ohayo! owo')


@bot.command()
async def ping(ctx):
    await ctx.send('pong!')
    pass

@bot.command()
async def p1(ctx):
    await ctx.send(carta1())
    pass

@bot.command()
async def TDG(ctx):
    await ctx.send('Compras un sobre de Génesis del duelista')
    await ctx.send(comprar1())
    pass

@bot.command()
async def LOD(ctx):
    await ctx.send('Compras un sobre de Luz de la Destrucción')
    await ctx.send(comprar2())
    pass

@bot.command()
async def bp2(ctx):
    await ctx.send('Obtienes un sobre de evento!:')
    await ctx.send(comprarprompack2())
    pass

@bot.command()
async def d6(ctx):
    await ctx.send('Lanzas un dado de 6 caras:')
    await ctx.send(dado6())
    pass

@bot.command()
async def d6_2(ctx):
    await ctx.send ('Lanzas dos dados de 6 caras:')
    await ctx.send(dados6_2())
    pass

@bot.command()
async def bp1(ctx):
    await ctx.send('Obtienes un sobre del evento!:')
    await ctx.send(comprarprompack1())
    pass

@bot.command()
async def sm(ctx):
    await ctx.send('https://media.giphy.com/media/M9NIVq3pVu03xmIsN6/giphy.gif')
    pass



def carta1():
    a = random.randint(0, len(hoja)-1)
    return hoja.iloc[a,0]


def comprarprompack2():
    i=0
    lists1=[]
    while i<3:
        p=random.randint(1,100)
        if p<=70:
            o=random.randint(0,16)
        elif p>70 and p<=90:
            o=random.randint(17,23)
        elif p>90 and p<=98:
            o=random.randint(24,27)
        elif p>98 and p<=100:
            o=random.randint (28,29)
        i+=1
        lists1.append(hojaprompack2.iloc[o,0])  
    return lists1
def comprar1():
    i=0
    lists1=[]
    while i<8:
        p=random.randint(1,100)
        print(p)
        if p<=90:
            o=random.randint(0,71)
        elif p>90 and p<101:
            o=random.randint(72,100)
        i+=1
        lists1.append(aTDG.iloc[o, 0])
    return lists1       
def comprar2():
    i=0
    lists1=[]
    
    while i<8:
        p=random.randint(1,100)
        print(p)
        if p<=60:
            o=random.randint(0,47)
        elif p>60 and p<=72:
            o=random.randint(48,67)
        elif p>72 and p<=83:
            o=random.randint(68,79)
        elif p>83 and p<=92:
            o=random.randint (80,89)
        elif p>92 and p<=100:
            o=random.randint(90,99)
        i+=1
        lists1.append(bLOD.iloc[o,0])  
    print("_____")
    return lists1

def dado6():
    a1=random.randint(1,6)
    return a1 

def dados6_2():
    a2=random.randint(1,6)
    a3=random.randint(1,6)
    a4=a2+a3
    return a4


def comprarprompack1():
    i=0
    lists1=[]
    while i<3:
        a5=random.randint(1,100)
        if a5<=85:
            o=random.randint(6,20)
        else:
            o=random.randint(0,5)
        i+=1
        lists1.append(hojaprompack1.iloc[o,0])
    return lists1



bot.run(token)
