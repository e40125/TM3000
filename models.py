# models.py
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

def get_model(model_name, temp, max_len):
    model_config = {
        'GPT': {
            'class': ChatOpenAI,
            'params': {"model": "gpt-4o-mini", "temperature": temp, "max_tokens": 50}
        },
        'TM3000': {
            'class': ChatOpenAI,
            'params': {"model": "ft:gpt-4o-mini-2024-07-18:personal::9zIKV308", "temperature": temp, "max_tokens": max_len},
            'system_message': "Tao Master 3000 is a wise Taoist sage that offers guidance based on Taoist principles."
        },
        'GS6000': {
            'class': ChatOpenAI,
            'params': {"model": "ft:gpt-4o-mini-2024-07-18:personal:gs6000:9ytKXg3C", "temperature": temp, "max_tokens": max_len},
            'system_message': "GS6000 is a self-improvement chatbot that talks like an G"
        },
        'Groq': {
            'class': ChatGroq,
            'params': {"model": "Llama-3.1-8B-Instant", "temperature": temp, "max_tokens": max_len}
        }
    }
    
    config = model_config[model_name]
    model = config['class'](**config['params'])
    return model, config.get('system_message')