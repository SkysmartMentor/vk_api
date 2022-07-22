import vk_api
import json

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id

from config import app_token, group_id, path


def main():
    vk_session = vk_api.VkApi(token=app_token)
    vk = vk_session.get_api()

    logpoll = VkBotLongPoll(vk_session, group_id)

    for event in logpoll.listen():
        print(event)
        print_event_type(event)
        write_answer_to_file(path, event.object)

        if event.type == VkBotEventType.MESSAGE_NEW:
            vk.messages.send(chat_id=1, random_id=get_random_id(), message=(
                    f'Привет, как дела?'
                )
            )


def print_event_type(event):
    print(f'Тип события: {event.type}')
    print('_' * 50)


def write_answer_to_file(path, item):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(item, file, indent=4, ensure_ascii=False)


main()
