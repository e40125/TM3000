# models.py
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

class Chatbot:
    def __init__(self, name, model, temp, max_len, system_message=None):
        self.name = name
        self.model = model
        self.temp = temp
        self.max_len = max_len
        self.system_message = system_message

    def get_response(self, input, history=None):
        # placeholder rn, for future response customization
        return self.model.predict(input)

class ChatbotFactory:
    @staticmethod
    def create_bot(model_name, temp, max_len):
        model_config = {
            'GPT': {
                'class': ChatOpenAI,
                'params': {"model": "gpt-4o-mini", "temperature": temp, "max_tokens": max_len}
            },
            'TM3000': {
                'class': ChatOpenAI,
                'params': {"model": "ft:gpt-4o-mini-2024-07-18:personal::9zIKV308", "temperature": temp, "max_tokens": max_len},
                'system_message': f"Tao Master 3000 is a wise Taoist sage that offers guidance based on Taoist principles. Keep response tokens under {max_len}"
            },
            'GS6000': {
                'class': ChatOpenAI,
                'params': {"model": "ft:gpt-4o-mini-2024-07-18:personal:gs6000:9ytKXg3C", "temperature": temp, "max_tokens": max_len},
                'system_message': f"GS6000 is a self-improvement chatbot that talks like an G. Keep response tokens under {max_len}"
            },
            'Groq': {
                'class': ChatGroq,
                'params': {"model": "Llama-3.1-8B-Instant", "temperature": temp, "max_tokens": max_len}
            }
        }
        
        config = model_config[model_name]
        model = config['class'](**config['params'])
        return Chatbot(model_name, model, temp, max_len, config.get('system_message'))

def get_model(model_name, temp, max_len):
    bot = ChatbotFactory.create_bot(model_name, temp, max_len)
    return bot.model, bot.system_message