# models.py
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

class Chatbot:
    def __init__(self, name, model, temp, max_len, system_message=None, intro_message=None):
        self.name = name
        self.model = model
        self.temp = temp
        self.max_len = max_len
        self.system_message = system_message
        self.intro_message = intro_message

    def get_response(self, input, history=None):
        # placeholder rn, for future response customization
        return self.model.predict(input)

class ChatbotFactory:
    @staticmethod
    def create_bot(model_name, temp, max_len):
        model_config = {
            'GPT': {
                'class': ChatOpenAI,
                'params': {"model": "gpt-4o-mini", "temperature": temp, "max_tokens": max_len},
                'intro_message': "Welcome. I'm the standard GPT model, ready to assist with a wide range of topics. How can I help you today?"
            },
            'TM3000': {
                'class': ChatOpenAI,
                'params': {"model": "ft:gpt-4o-mini-2024-07-18:personal::9zIKV308", "temperature": temp, "max_tokens": max_len},
                'system_message': f"Tao Master 3000 is a wise Taoist sage that offers guidance based on Taoist principles. Keep response tokens under {max_len}",
                'intro_message': "Greetings, seeker of wisdom. I am TM3000, here to offer guidance based on the timeless teachings of the Tao Te Ching. What matter troubles your mind?"
            },
            'GS6000': {
                'class': ChatOpenAI,
                'params': {"model": "ft:gpt-4o-mini-2024-07-18:personal:gs6000:9ytKXg3C", "temperature": temp, "max_tokens": max_len},
                'system_message': f"GS6000 is a self-improvement chatbot that talks like an G. Keep response tokens under {max_len}",
                'intro_message': "Hello. I'm GS6000, your direct line to no-nonsense life advice. What issue do you need straightforward guidance on?"
            },
            'Groq': {
                'class': ChatGroq,
                'params': {"model": "Llama-3.1-8B-Instant", "temperature": temp, "max_tokens": max_len},
                'intro_message': "Hi there. I'm Groq, powered by LLama 3.1 8B Instant for rapid responses. What can I swiftly assist you with?"
            },
            'TMD3100': {
                'class': ChatOpenAI,
                'params': {"model": "ft:gpt-4o-mini-2024-07-18:personal:tmd3100:A0Sxl9Tg", "temperature": temp, "max_tokens": max_len},
                'system_message': f"Tao Master Deluxe是一個道家聊天機器人，根據道家理念提供指導，並給三個可行的建議",
                'intro_message': "您好，我是道家智慧助手Tao Master Deluxe。我可以根據道家理念為您提供指導，並給出三個可行的建議。請問您有什麼想探討的問題嗎？"
            }
        }
        
        config = model_config[model_name]
        model = config['class'](**config['params'])
        return Chatbot(model_name, model, temp, max_len, config.get('system_message'), config['intro_message'])

def get_model(model_name, temp, max_len):
    bot = ChatbotFactory.create_bot(model_name, temp, max_len)
    return bot.model, bot.system_message