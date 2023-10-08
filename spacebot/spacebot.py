import os
from hugchat import hugchat
from hugchat.login import Login

# email = os.getenv("ENV_BOT_EMAIL")
# passwd = os.getenv("ENV_BOT_PASSWD")
# cookies_path_dir = os.getenv("ENV_BOT_COOKIES")
email = 'akc33333@gmail.com'
passwd = 'Jorge1234!.'
cookies_path_dir = './cookies/'


class SpaceBot:
    def __init__(self, name="SpaceBot"):
        """Initialize a SpaceBot with a default name"""
        self._name = name
        self._msg_count = 0
        self.initialize_bot_api()
        self.new_conversation()
        self._context = "Imagine that you are a travel agent of an agency that organizes trips \
through the real planets and moons of the Solar System. You have to recomend me one destination \
based on what "
        
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
        # sign = Login(email, passwd)
        # cookies = sign.login()
        # sign.saveCookiesToDir(cookies_path_dir)
        # self.chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
        sign = Login(email, passwd)
        cookies = sign.login()
        sign.saveCookiesToDir(cookies_path_dir)
        self.chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

    def new_conversation(self):
        """
        Generates a brand new conversation, reseting
        the previous given context from the hole conversarion.
        """
        id = self.chatbot.new_conversation()
        self.chatbot.change_conversation(id)
        self._msg_count = 0

    def query(self, query):
        """Makes a query to the Bot
        Args:
            query: query to send to the bot

        Returns:
            dict: {'response': 'text of the response'}
        """
        context = self._context if self.msg_count == 0 else ""
        final_query = context + query + ". And give me the response in only one sentence, please."
        query_result = self.chatbot.query(final_query)
        self._msg_count += 1
        return {'response': query_result.text}
    