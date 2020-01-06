from aiogram import Bot, Dispatcher, types, executor
from botstate import BotState
import story
import logging
import asyncio

# fields
API_TOKEN = ''
state = BotState.IDLE

# commands
START   = '/start'
HELP    = '/help'
STORY   = '/story'

# setup
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# handlers
@dp.message_handler(commands = ['start','help','story'])
async def command_handler(message: types.Message):
    if message.text == START:
        await _send_start(message)
    if message.text == HELP:
        await _send_help(message)
    if message.text == STORY:
        await _start_story(message)
        return

@dp.message_handler(content_types = types.ContentType.TEXT)
async def text_handler(message: types.Message):
    if state == BotState.STORY_INPUT_HERO:
        await _set_hero(message)
        return
    if state == BotState.STORY_INPUT_FRIEND:
        await _set_friend(message)
        return

# handler reaction funcs
async def _send_start(message: types.Message):
    global state 
    state = BotState.IDLE
    m = """
    Здарова, что бы начать введи /story.
    Для того что бы получить список команд
    введи /help.
    """
    await message.reply(m)

async def _send_help(message: types.Message):
    global state 
    state = BotState.IDLE
    m = """
    Команды:
    /start
    /help
    /story
    """
    await message.reply(m)

async def _start_story(message: types.Message):
    global state
    state = BotState.STORY_INPUT_HERO
    m = """
    Отлично! Напиши мне имя главного героя.
    """
    await message.reply(m)

async def _set_hero(message: types.Message):
    global state
    state = BotState.STORY_INPUT_FRIEND
    story.hero = message.text
    m = """
    Круто! Теперь напиши имя твоего друга!
    """
    await message.reply(m)

async def _set_friend(message: types.Message):
    global state
    state = BotState.IDLE
    story.friend = message.text
    m = """
    Отлично! Вот твоя история.
    {}
    """.format(get_story())
    await message.reply(m)
    

# misc
def get_story():
    return story.makeStory()

# start
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)