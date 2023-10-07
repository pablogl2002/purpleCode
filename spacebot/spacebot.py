from hugchat import hugchat
from hugchat.login import Login

email = 'adri_mrtnz@hotmail.com'
passwd = 'BotSpaceApps2023'
cookies_path_dir = './cookies/'


class SpaceBot:
    def __init__(self, name="SpaceBot"):
        self._name = name
        self.load_bot()
        self._context = context = "Imagine that you are an agent in a \
            space travel agency that organizes travels to the planets \
            of the Solar System and "
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    def load_bot(self):
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
        id = self.chatbot.new_conversation()
        self.chatbot.change_conversation(id)

    def query(self, query):
        query = "I want a planet where i can fully express myself"
        final_query = self._context + query + "Give me no more than one paragraph."

        query_result = self.chatbot.query(final_query)
        return {'response': query_result.text}