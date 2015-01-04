# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
import sys
reload(sys)

sys.setdefaultencoding('gbk')

from django.http import HttpResponse,HttpResponseRedirect
import datetime,os,json,time
from django.contrib import auth 
from django.contrib.auth import logout
from models import *
online_clients=[]
online_client=[]

chat_rooms={}
room_static={}
contact=[]
for room in Contact.objects.all():
	chat_rooms[room.client_id]=[]
print chat_rooms,'----',

working_dir='/home/redking/oldboy/kefu/chat'

def getclientlist(request):
	#room_name=request.GET['room_name']
	clientname=Contact.objects.order_by('-id')[0].client_id
        #clientname=sorted(Contact.objects.all())[-1].client_id
        #print clientname, '____|||||--------'
        if clientname not  in online_client:
                #clientname =int(clientname)+1
                online_client.append(clientname)	
	#print 'ddddd',online_client
	return HttpResponse(json.dumps(online_client))

	#return HttpResponse(Contact.objects.all())
def chat(request):
	clientname=Contact.objects.order_by('-id')[0].client_id
       	clientname =int(clientname)+1
        a=Contact(client_id=clientname,client_name=clientname,contact_time=time.strftime('%Y-%m-%d',time.localtime( time.time())) )
	
        a.save()
	room_static[clientname]=0
	return render_to_response('chat_red.html',{'clientname':clientname})

@login_required
def hide(request):
	clientname=Contact.objects.order_by('-id')[0].client_id
	return render_to_response('chat_hide.html',{'clientname':clientname,'teacher':request.user})

@login_required
def chat_server(request):
	return render_to_response('chat_server.html',{'teacher':request.user})


def login(request):
	if request.POST:
		username=request.POST.get('username','')
		password=request.POST.get('password','')
		user=auth.authenticate(username=username,password=password)
		#print username,password
		if user is not None: #and user.is_active:
			#correct password and user is marked "actice"
			auth.login(request,user)
			return HttpResponseRedirect("/teacher/")
			#return render_to_response('chat_server.html',{'username':username})
		else:
			return render_to_response('login.html',{'login_err':'Wrong username or password!'})
	return render_to_response('login.html')


def sendMsg(request):
	messages = request.POST['msg']
	client_name = request.POST['client']
	room_name = request.POST['room_name']
	date=time.strftime('%H:%M:%S')
	#print type(chat_rooms)
	#print type(chat_rooms[room_name]),'---------======================='
	chat_rooms[room_name].append( { date:
		{'client_name':client_name,
		'message':messages,
		'client_received':[client_name],
		}
		})
	Contact.objects.filter(client_id=room_name).update(content=json.dumps(chat_rooms[room_name])  )		
	return HttpResponse(messages)
	

def getNewMsg(request):
        client_name = request.GET['client']
        room = request.GET['room']
	new_msgs=[]
    	new_msg_count = 0
	if room not in chat_rooms.keys():
		chat_rooms[room]=[]	
	for msg in chat_rooms[room]:
		msg_info=msg.values()[0]
		#print msg_info,'ffffff--fffffff'
		if client_name not in msg_info['client_received']:
			new_msg_count += 1
			new_msgs.append(msg)
			msg_info['client_received'].append(client_name)
			#print "New message",msg_info['message']
	if new_msg_count>0:
		#print "must got some new msg",new_msg_count
		return HttpResponse(json.dumps(new_msgs))
	else:
		#print "No new messgeg"
		return HttpResponse("NONewMessage")

	
def getmax(request):
	clientname=Contact.objects.order_by('-id')[0].client_id
	return HttpResponse(json.dumps(clientname))
def mark(request):
	room1=request.GET['rooms']
	client=request.GET['client']
	#print room_static
        #print room_static[int(room1)], '======='
	marks=room_static[int(room1)]
	#print marks,'@@@@@@@@@@@@'
	if marks ==0:
		room_static[int(room1)]=client
		#print room_static[int(room1)],'&&&&&&&&&&&&&&&&&'
		#print room_static,'>>>>>>>>>>>>>>>>>'
		return HttpResponse(room_static[int(room1)])
	else:
		return HttpResponse(room_static[int(room1)])
		#print room_static,'<<<<<<<<<<<<<<<<<<'
		#print room_static[int(room1)],'&&&&&&&&&&&&&&&&&'
@login_required
def getoldmsg(request):
	time=request.POST['time']
	times=request.POST['times']
	p=Contact.objects.filter(contact_time__range=(time,times))
	#p=Contact.objects.filter(TO_DAYS(contact_time)=time)
	select_room=[]
	for group in p:
		b=group.client_id
		select_room.append(b)
	print select_room,type(select_room),"<<<<<<<<<<<<>>>>>"
	#str2list = json.loads(b)
	#return HttpResponse(json.dumps(str2list))
	return HttpResponse(json.dumps(select_room)) 
@login_required
def logout(request):
	auth.logout(request)
	return render_to_response('login.html')
@login_required
def query(request):
	return render_to_response('chat_query.html')  
def getlog(request):
	name=request.POST['client_name']
	chat_list=Contact.objects.get(client_name=name)
	b=chat_list.content
        if b=='hello!':
                return HttpResponse("NOMessage")
        else:
                str2list=json.loads(b)
                print str2list,")))))))))))"
                return HttpResponse(json.dumps(str2list))
