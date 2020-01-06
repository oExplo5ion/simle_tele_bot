from enum import Enum

class BotState(Enum):
    IDLE                = 0
    STORY_INPUT_HERO    = 1
    STORY_INPUT_FRIEND  = 2