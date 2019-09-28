from django.shortcuts import render

# Create your views here.
def chat(request):
    return render(request,'chat_bot/chat.html',{'username':request.session['username']})

def room_chat(request):
    return render(request,'chat_bot/room.html',{'username':request.session['username']})