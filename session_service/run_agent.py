import asyncio

from dotenv import load_dotenv


load_dotenv()

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types 

from agent import root_agent

APP_NAME = "session_agent"
USER_ID = "aryan"

# session service for saving data in database 
session_service = InMemorySessionService()

# Runner : connects agent to the session service 
runner = Runner(
    app_name=APP_NAME,
    agent=root_agent,
    session_service=session_service
)


# create a session ( a conversation)
# Session services are async, so we wrap it in asyncio.run()

def create_session():
    session = asyncio.run(
        session_service.create_session(app_name=APP_NAME,user_id=USER_ID)
    ) 

    print("New session created")
    print(f"session id {session.id}")
    print(f"session app name {session.app_name}")
    print(f"session user id   {session.user_id}")
    print(f"events {len(session.events)}")

    return session 

def ask(session_id:str, text:str):

    print("User text: ", text)
    message = types.Content(role="User",parts=[types.Part(text=text)])

    for event in runner.run(user_id=USER_ID,session_id=session_id,new_message=message):
        if event.is_final_response():
            print(f"Agent: {event.content.parts[0].text}\n")

def main():
    chat_1 = create_session()
    ask(chat_1.id,"Hello, My name is Aryan")
    ask(chat_1.id,"What is my name?")

    chat_2 = create_session()
    ask(chat_2.id,"What is my name?")

if __name__=="__main__":
    main()



    