
import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("MIMO_OPENAI_API_KEY")

url = "https://ai.mimo.org/v1/openai/message"
headers = {"api-key": api_key}
current_thread_id = None



def send_message(user_message, current_thread_id):
  body = {"message" : user_message}
  if current_thread_id is not None:
    body["threadId"] = current_thread_id
  response = requests.post(url, headers = headers, json = body)
  return response.json()

print("Welcome to this ChatGPT clone created by Joshua. Please go ahead and type your message and press Enter to send.")
print("To exit, type 'exit' to end your interaction with the program.")
print("Would like to start a new conversation? Type 'new' to start a new conversation thread.")
print("A new thread has been started for you. \n")

threads = [] 

while True:
  user_message = input("You: ")
  
  if user_message == "exit":
    break
  elif user_message == "new":
    current_thread_id = None
    print("A new conversation thread is starting.")
    continue
  

  response_data = send_message(user_message, current_thread_id)
  latest_message = response_data.get("response")
  current_thread_id = response_data.get("threadId")

  print(f"GPT: {latest_message}")
  threads.append(current_thread_id)
