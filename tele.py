import telebot
import token

bot = telebot.TeleBot(TOKEN)


#Идентификация пользователя
directory = 'tasks/'
@bot.message_handler(commands = ['start'])
def start(message):
	file_id = str(message.from_user.first_name) + "_" + str(message.from_user.last_name) + "_" + str(message.from_user.id)
	name = file_id + '.txt'
	new_file = open(directory + f'/{name}', mode='a')
	new_file.close()
	bot.send_message(message.from_user.id, 'Hello, ' + str(message.from_user.first_name))

#Добавление нового элемента
@bot.message_handler(commands = ['new_item'])
def new(message):
	file_id = str(message.from_user.first_name) + "_" + str(message.from_user.last_name) + "_" + str(message.from_user.id)
	name = file_id + '.txt'
	new_file = open(directory + f'/{name}', mode='a')
	task = message.text.replace('/new_item ', '')
	new_file.write(task + '\n')
	bot.send_message(message.from_user.id, 'Add it!')
	new_file.close()


#Просмотр всех задач
@bot.message_handler(commands=['all'])
def all(message):
	file_id = str(message.from_user.first_name) + "_" + str(message.from_user.last_name) + "_" + str(message.from_user.id)
	name = file_id + '.txt'
	new_file = open(directory + f'/{name}', mode='r')
	all_task = new_file.read().split('\n')
	for i in range (0, len(all_task) - 1):
		bot.send_message(message.from_user.id, str(i+1) + ') ' + str(all_task[i]))
	new_file.close()

#Удаление задачи
@bot.message_handler(commands=['delete'])
def delete(message):
	num_delete = int(message.text.replace('/delete ', ''))
	file_id = str(message.from_user.first_name) + "_" + str(message.from_user.last_name) + "_" + str(message.from_user.id)
	name = file_id + '.txt'
	new_file = open(directory + f'/{name}', mode='r')
	all_task = new_file.read().split('\n')
	new_file.close()
	all_task.remove(all_task[num_delete - 1])
	new_file = open(directory + f'/{name}', mode='w')
	for i in range(0, len(all_task) - 1):
		new_file.write(all_task[i] + '\n')
	new_file.close()
	bot.send_message(message.from_user.id, "Delete it!")




bot.polling()
