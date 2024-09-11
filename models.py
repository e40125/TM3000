# models.py
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

BOT_CONFIGS = {
    'GPT': {
        'class': ChatOpenAI,
        'params': {
            'model': "gpt-4o-mini",
            'temperature': {'min': 0.01, 'max': 1.0, 'default': 0.5, 'step': 0.01},
            'max_tokens': {'min': 32, 'max': 256, 'default': 128, 'step': 4}
        },
        'intro_message': "Welcome. I'm the standard GPT model, ready to assist with a wide range of topics. How can I help you today?",
        'spinner_message': "Generating response..."

    },
    'TM3000': {
        'class': ChatOpenAI,
        'params': {
            'model': "ft:gpt-4o-mini-2024-07-18:personal::9zIKV308",
            'temperature': {'min': 0.01, 'max': 1.0, 'default': 0.5, 'step': 0.01},
            'max_tokens': {'min': 32, 'max': 256, 'default': 128, 'step': 4}
        },
        'system_message': "Tao Master 3000 is a wise Taoist sage that offers guidance based on Taoist principles.",
        'intro_message': "Greetings, seeker of wisdom. I am TM3000, here to offer guidance based on the timeless teachings of the Tao Te Ching. What matter troubles your mind?",
        'spinner_message': "Tao Master 3000 channeling ancient wisdom..."
    },
    'GS6000': {
        'class': ChatOpenAI,
        'params': {
            'model': "ft:gpt-4o-mini-2024-07-18:personal:gs6000:9ytKXg3C",
            'temperature': {'min': 0.01, 'max': 1.0, 'default': 0.5, 'step': 0.01},
            'max_tokens': {'min': 32, 'max': 256, 'default': 128, 'step': 4}
        },
        'system_message': "GS6000 is a self-improvement chatbot that talks like an G.",
        'intro_message': "Hello. I'm GS6000, your direct line to no-nonsense life advice. What issue do you need straightforward guidance on?",
        'spinner_message': "GS6000 brewin' up some real talk..."
    },
    'Groq': {
        'class': ChatGroq,
        'params': {
            'model': "Llama-3.1-8B-Instant",
            'temperature': {'min': 0.01, 'max': 1.0, 'default': 0.5, 'step': 0.01},
            'max_tokens': {'min': 32, 'max': 256, 'default': 128, 'step': 4}
        },
        'intro_message': "Hi there. I'm Groq, powered by LLama 3.1 8B Instant for rapid responses. What can I swiftly assist you with?",
        'spinner_message': "Groq's processin' at lightspeed..."
    },
    'TMD3100': {
        'class': ChatOpenAI,
        'params': {
            'model': "ft:gpt-4o-mini-2024-07-18:personal:tmd3100:A0Sxl9Tg",
            'temperature': {'min': 0.01, 'max': 1.0, 'default': 0.5, 'step': 0.01},
            'max_tokens': None
        },
        'system_message': "Tao Master Deluxe是一個道家聊天機器人，根據道家理念提供指導，並給三個可行的建議",
        'intro_message': "您好，我是Tao Master Deluxe 道家智慧助手。我可以根據道家理念為您提供人生建議。您有想探討的話題嗎？",
        'spinner_message': "冥想中..."
    }
}

class Chatbot:
    def __init__(self, name, model, temp, max_len, system_message=None, intro_message=None, spinner_message=None):
        self.name = name
        self.model = model
        self.temp = temp
        self.max_len = max_len
        self.system_message = system_message
        self.intro_message = intro_message
        self.spinner_message = spinner_message

    def get_response(self, input, history=None):
        return self.model.predict(input)

class ChatbotFactory:
    @staticmethod
    def create_bot(model_name, temp, max_len):
        config = BOT_CONFIGS[model_name]
        params = {k: v for k, v in config['params'].items() if not isinstance(v, dict)}
        
        if 'temperature' in config['params'] and isinstance(config['params']['temperature'], dict):
            params['temperature'] = temp
        
        if 'max_tokens' in config['params'] and isinstance(config['params']['max_tokens'], dict):
            params['max_tokens'] = max_len
        elif 'max_tokens' in config['params'] and config['params']['max_tokens'] is None:
            params['max_tokens'] = None

        model = config['class'](**params)
        return Chatbot(model_name, model, temp, max_len, config.get('system_message'), config['intro_message'], config['spinner_message'])

def get_model(model_name, temp, max_len):
    bot = ChatbotFactory.create_bot(model_name, temp, max_len)
    return bot.model, bot.system_message