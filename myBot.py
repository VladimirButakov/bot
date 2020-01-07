from vk_api.longpoll  import VkLongPoll, VkEventType
import vk_api
from datetime import datetime

login, password = "Юзер нейм", "пароль"
vk_session = vk_api.VkApi(login=login, password=password, app_id=2685278)
vk_session.auth(token_only=True)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        user_get= session_api.users.get(user_ids = (event.user_id))
        user_get = user_get[0]
        first_name = user_get['first_name']
        print('Юзер ' + str(first_name))
        print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
        print('Текст сообщения: ' + str(event.text))
        response = event.text.lower()
        if event.from_user :
            if response == "привет":
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'ПРИВЕТ ' + str(first_name) + '! КАК ДЕЛА', 'random_id': 0})
        elif event.from_chat :
            if response == "привет":
                vk_session.method('messages.send', {'chat_id': event.chat_id, 'message': 'ПРИВЕТ ' + str(first_name) + '! КАК ДЕЛА', 'random_id': 0})