####___Imported_packages___####
#!!!!!!!!!!!TELETHON == 0.19!!!!!!!!!!!!!!!
import time
from telethon 						import errors
from telethon 						import TelegramClient
from telethon.tl.types 				import InputPhoneContact
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.functions.messages import EditChatTitleRequest
from telethon.tl.functions.channels import InviteToChannelRequest
#################################################################

####___Your_data___####
api_id = XXXXXXXXXXX #This api for you telegram account (not bot only you account API)
api_hash = 'XXXXXXXXXXXXXX' 
phone_number = "XXXXXXXXXX" #Phone number your telegram account
#############################################

####___Login_script_in_telegram___####
client = TelegramClient(session="session1", api_id=api_id, api_hash=api_hash)
assert client.connect()
if not client.is_user_authorized():
  client.send_code_request(phone_number)
  me = client.sign_in(phone_number, input("Enter the code you received in telegram: "))
##############################################################################

numbers = open("numbers.txt", "r").read().split("\n")

for i in numbers:
	####___More_data___####
	channel_name = "XXXXXXXXXXXXXX"
	guest_phone_number = i #The number you want to add channel
	####################################
	
	try:
		time_sleep = time.sleep(10)
		####___Add_user_to_your_contact___####
		contact = InputPhoneContact(client_id=0, phone=guest_phone_number, first_name="AddedUser", last_name="")
		result = client.invoke(ImportContactsRequest([contact]))
		###############################################################################################

		try:
			####___Add_user_to_channel___####
			client(InviteToChannelRequest(channel=channel_name, users=[result.users[0]]))
			print(result.users[0].phone + " - added ")
			############################################################################
		except errors.PeerFloodError:
			print("Too many requests, please change account or waiting")
		except errors.UserNotMutualContactError:
			print("This contact cannot be added")

	except (IndexError, TypeError):
		print(i + " error")
		continue