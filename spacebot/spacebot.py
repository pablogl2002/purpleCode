import os
from hugchat import hugchat
from hugchat.login import Login

# ENV_BOT_EMAIL = 'adri_mrtnz@hotmail.com'
# ENV_BOT_PASSWD = 'BotSpaceApps2023'
# email = os.getenv("ENV_BOT_EMAIL")
# passwd = os.getenv("ENV_BOT_PASSWD")
email = 'adri_mrtnz@hotmail.com'
passwd = 'BotSpaceApps2023'
cookies_path_dir = './cookies/'


class SpaceBot:
    def __init__(self, name="SpaceBot"):
        """Initialize a SpaceBot with a default name"""
        self._name = name
        self._msg_count = 0
        self.initialize_bot_api()
        self.new_conversation()
        self._context = context = "Imagine that you are an agent in a \
            space travel agency that organizes travels to the planets \
            of the Solar System and "
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def msg_count(self):
        return self._msg_count

    def initialize_bot_api(self):
        """Makes the connection with the HuggingFace API"""
        try: 
            # Load cookies when restarting the program
            sign = Login(email, None)
            cookies = sign.loadCookiesFromDir(cookies_path_dir)
        except:
            sign = Login(email, passwd)
            cookies = sign.login()
            sign.saveCookiesToDir(cookies_path_dir)
        finally:
            self.chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

    def new_conversation(self):
        """
        Generates a brand new conversation, reseting
        the previous given context from the hole conversarion.
        """
        id = self.chatbot.new_conversation()
        self.chatbot.change_conversation(id)

    def query(self, query):
        """Makes a query to the Bot
        Args:
            query: query to send to the bot

        Returns:
            dict: {'response': 'text of the response'}
        """
        query = "I want a planet where i can fully express myself"

        context = self._context if self.msg_count != 0 else ""
        final_query = context + query + "Give me no more than one paragraph."

        query_result = self.chatbot.query(final_query)
        return {'response': query_result.text}
    