knowledge_base = {     '''a knowledge_base is just likeour memmory'''
    'hello':'hai',
    'Hi':'Hi',
    'hi':'hai',
    'what is your name':'viju',
    'how old are you':'iam just born',
    'do you walk':'no but i do run',
    
}
class Bot(object):      '''create a class'''
    def respond(selfself,msg):   '''create a function''' 
        return knowledge_base[msg]
status = True
bot = Bot()     '''object'''
while status:
    msg = input("you > ")
    if msg == 'exit':
        print("Bot > Bye")
        break
    res = bot.respond(msg)  '''function calling'''
    print("Bot >"+res)
