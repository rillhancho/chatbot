from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer


bot=ChatBot('chatbot', read_only=False,logic_adapter= [
    
    {
       'import_path':'chatterbot.logic.BestMatch',
       'default_response':'Sorry,I do not know what that means',
       'maximum_similarity_threshold':0.90 
        
        
    }
])
    

    
    

list_to_train={ 
            
        #greetings
         "Hello",
         "Hi there, how may I help you?",
         "Hallo",
         "Hi there, how may I help you?",
         "what's up",
         "Hi there, how may I help you?",
         "Hey",
         "Hi there, how may I help you?",
         "wagwan",
         "Hi there, how may I help you?",
         "Hi",
         "Hi there, how may I help you?",
         
         
        
        
               
               
               }



list_trainer=ListTrainer(bot)
list_trainer.train(list_to_train)



def index(request):
    return render(request, 'blog/index.html')


def getResponse(request):
    userMessage= request.GET.get('userMessage')
    chatResponse=str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)





    