DO_INTERFACE = True

WIN_SELL_VALUE = 2048

MAX_QUEUE_DEPTH = 10
MIN_SIZE_VALUE = 4
MAX_SIZE_VALUE = 10

MINECRAFT_MUSIC = ["music/C418 - Living Mice.mp3",
                   "music/C418 - Minecraft.mp3",
                   "music/C418 - Subwoofer Lullaby.mp3",
                   "music/C418 - Sweden.mp3", "C418 - Wet Hands.mp3"]
BEETHOVEN_MUSIC = ["music/Piano-Sonata-No.21-1.mp3"]
CHOPIN_MUSIC = ["music/Chopin-Nocturn-in-c-sharp.mp3"]

RANDOM_COMMENTS = ["You're doing pretty good!",
                   "Do you like Python?",
                   "This app is amazing, isn't it?",
                   "That's almost a world record!",
                   "Great speedrun!",
                   "Truly exciting Minecraft gameplay!",
                   "This is actually a new 1.20.48 Minecraft update",
                   "Good weather today... Wanna go out?",
                   "So far so good!",
                   "Finally a game we deserved!",
                   "This game has a lot in common with Minecraft because.. it consists of.. squares...",
                   "Aren't you enjoying music on the background?",
                   "This game is totally free.. Should we change it?..",
                   "A new, huuuge update is coming. It will change the color scheme...",
                   "I tried my best!",
                   "Comment, like and subscribe for more content in the future!",
                   "Let the game begin!"
                  ]
RANDOM_COMMENT_CHANCE = 0.1

BUTTON_PRESS_MESSAGES = ["Yep.. that's a number...",
                         "I don't know why these are buttons..",
                         "Is it funny to press these?",
                         "So colourful!",
                         "This number is called ",
                         "Stupid jokes, right?"
                         ]
BUTTON_PRESS_MESSAGE_CHANCE = 0.4

WRONG_INPUT_REPORTS = ["Are you OK?",
                       "Is everything fine?",
                       "Check if your keyboard has any cats jumping on it",
                       "Oh, you're throwing...",
                       "Wrong input!!",
                       "Come on, you can do it in the proper way!",
                       "Looks like you haven't practiced your typing for a while...",
                       "Game can't really understand you..."
                       ]
WRONG_INPUT_REPORT_CHANCE = 0.4


class Bright:
    STATS_COLOR = "#7ad4f7"
    MAIN_BG_COLOR = "#FAEBD7"
    MAIN_FG_COLOR = '#9411c0'
    BUTTON_FG_COLOR = '#000000'
    BUTTON_BG_COLOR = '#e5ee88'

    @staticmethod
    def choose_color(num):
        dict_colors = {0: ('#000000', '#fefde4', '#000000', '#fefcdb'),
                       2: ('#000000', '#fcf5ad', '#000000', '#f9f092'),
                       4: ('#000000', '#f7db7a', '#000000', '#f4d158'),
                       8: ('#000000', '#f1c05f', '#000000', '#efb646'),
                       16: ('#000000', '#ef9a1d', '#000000', '#e79012'),
                       32: ('#000000', '#e1804e', '#000000', '#df7137'),
                       64: ('#000000', '#e92121', '#000000', '#d01616'),
                       128: ('#000000', '#d4ef2f', '#000000', '#c4e112'),
                       256: ('#000000', '#aff13e', '#000000', '#9dea19'),
                       512: ('#000000', '#7ff13e', '#000000', '#5fea11'),
                       1024: ('#000000', '#1bed38', '#000000', '#12cc2c'),
                       2048: ('#e11414', '#0bad21', '#000000', '#0a871b'),
                       4096: ('#000000', '#09c87e', '#000000', '#08a267'),
                       8192: ('#000000', '#12afd2', '#000000', '#0f91ae'),
                       16384: ('#000000', '#2c3deb', '#000000', '#0e1db1'),
                       32768: ('#000000', '#792baf', '#000000', '#682497')
                       }
        if num not in dict_colors.keys():
            answer = '#ffffff', '#000000', '#ffffff', '#525252'
        else:
            answer = dict_colors[num]
        return answer


class Standart:
    STATS_COLOR = "#f3f1b1"
    MAIN_BG_COLOR = "#f0eeba"
    MAIN_FG_COLOR = '#000000'
    BUTTON_FG_COLOR = '#000000'
    BUTTON_BG_COLOR = '#949494'
    TEXT_BG_COLOR = '#ffffff'

    @staticmethod
    def choose_color(num):
        dict_colors = {0: ('#000000', '#f9f8f7', '#000000', '#f4f1ef'),
                       2: ('#000000', '#f3ece5', '#000000', '#eee5dc'),
                       4: ('#000000', '#f5e4d2', '#000000', '#f2dcc4'),
                       8: ('#000000', '#fbd5b0', '#000000', '#facc9e'),
                       16: ('#000000', '#f09e79', '#000000', '#ed946b'),
                       32: ('#000000', '#f86262', '#000000', '#f65050'),
                       64: ('#000000', '#f93434', '#000000', '#f91919'),
                       128: ('#000000', '#ffff87', '#000000', '#fdfd66'),
                       256: ('#000000', '#fbff68', '#000000', '#f0f382'),
                       512: ('#000000', '#f5f949', '#000000', '#eaef2f'),
                       1024: ('#000000', '#faff34', '#000000', '#eef409'),
                       2048: ('#000000', '#e4ea0f', '#000000', '#d2d617')
                       }
        if num not in dict_colors.keys():
            answer = '#ffffff', '#000000', '#ffffff', '#525252'
        else:
            answer = dict_colors[num]
        return answer


class Dark:
    STATS_COLOR = "#7ad4f7"
    MAIN_BG_COLOR = "#9229b5"
    MAIN_FG_COLOR = '#ffffff'
    BUTTON_FG_COLOR = '#000000'
    BUTTON_BG_COLOR = '#1519f6'

    @staticmethod
    def choose_color(num):
        dict_colors = {0: ('#000000', '#fffc6a', '#000000', '#faf64c'),
                       2: ('#000000', '#b8f536', '#000000', '#a6ed10'),
                       4: ('#000000', '#0eeb14', '#000000', '#0cd911'),
                       8: ('#000000', '#0bad21', '#000000', '#0a871b'),
                       16: ('#000000', '#09c87e', '#000000', '#08a267'),
                       32: ('#000000', '#09c8ae', '#000000', '#07ad96'),
                       64: ('#000000', '#12afd2', '#000000', '#0f91ae'),
                       128: ('#000000', '#2c3deb', '#000000', '#0e1db1'),
                       256: ('#000000', '#811ded', '#000000', '#7513e0'),
                       512: ('#000000', '#792baf', '#000000', '#682497'),
                       1024: ('#000000', '#af2baf', '#000000', '#9a279a'),
                       2048: ('#000000', '#af2b67', '#000000', '#99265a'),
                       4096: ('#000000', '#aa1919', '#000000', '#911717'),
                       8192: ('#000000', '#e81a1a', '#000000', '#d21515'),
                       16384: ('#000000', '#db611a', '#000000', '#bf5517'),
                       32768: ('#000000', '#fba51b', '#000000', '#d98807'),
                       65536: ("#000000", '#aaa306', '#000000', '#8a8405'),
                       131072: ("#ffffff", '#5e5a01', '#ffffff', '#7f7a02')
                       }
        if num not in dict_colors.keys():
            answer = '#ffffff', '#000000', '#ffffff', '#525252'
        else:
            answer = dict_colors[num]
        return answer
