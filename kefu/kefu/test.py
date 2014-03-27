import random

online_clients=[]
chat_rooms={}
room_members={}

while True:

                client_name=random.randint(1,10)
                if client_name not in online_clients:
                        online_clients.append(client_name)
           #             request.session['ClientName']=client_name
		
#                        room_members[room.name].append(client_name)
              #          return HttpResponse(client_name)
#			print online_clients,
			break
                else:
                        continue
print online_clients,
