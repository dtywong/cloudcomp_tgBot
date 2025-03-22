import configparser
import os
import requests
import logging #Add missing import


class HKBU_ChatGPT():
    # def __init__(self, config_='config.ini'):
    #     if type(config_) == str:
    #         self.config = configparser.ConfigParser()
    #         self.config.read(config_)
    #     elif type(config_) == configparser.ConfigParser:
    #         self.config = config_

    def __init__(self):
        # Read directly from environment variables
        self.basic_url = os.environ['CHATGPT_BASICURL']
        self.model_name = os.environ['CHATGPT_MODELNAME']
        self.api_version = os.environ['CHATGPT_APIVERSION']
        self.api_key = os.environ['CHATGPT_ACCESS_TOKEN']

    def __init__(self):
        # Read directly from environment variables
        self.basic_url = os.environ['CHATGPT_BASICURL']
        self.model_name = os.environ['CHATGPT_MODELNAME']
        self.api_version = os.environ['CHATGPT_APIVERSION']
        self.api_key = os.environ['CHATGPT_ACCESS_TOKEN']

    def submit(self, message):
        conversation = [{"role": "user", "content": message}]

        url = ((self.config['CHATGPT']['BASICURL'])
               + "/deployments/" + (self.config['CHATGPT']['MODELNAME'])
               + "/chat/completions/?api-version="
               + (self.config['CHATGPT']['APIVERSION']))

        headers = {'Content-Type': 'application/json',
                   'api-key': (self.config['CHATGPT']['ACCESS_TOKEN'])}

        payload = {'messages': conversation}

        #response = requests.post(url, json=payload, headers=headers)
        #if response.status_code == 200:
            #data = response.json()
            #return data['choices'][0]['message']['content']
        #else:
            #return 'Error:', response

        try:
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            response.raise_for_status()  # Raise HTTP errors
            data = response.json()
            return data['choices'][0]['message']['content']
        except Exception as e:
            logging.error(f"ChatGPT API Error: {str(e)}")
            return "Sorry, I couldn't process your request. Please try again later."


if __name__ == '__main__':
    ChatGPT_test = HKBU_ChatGPT()
    while True:
        user_input = input("Typing anything to ChatGPT:\t")
        response = ChatGPT_test.submit(user_input)
        print(response)