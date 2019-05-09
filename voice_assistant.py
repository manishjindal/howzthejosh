import json
import ibm_watson
import pyttsx
import speech_recognition as sr

while True:
    user_input = ""
    service = ibm_watson.AssistantV2(
        iam_apikey='Lxa1VrZzTwE9xnMrMFJUaE1Q74txlo8tj1oFLlvaTy61',
        version='2019-02-28',
        url='https://gateway-lon.watsonplatform.net/assistant/api'
    )

    session_response = service.create_session(
        assistant_id='cc6ddadf-b029-47ac-956a-8ccfdf354996'
    ).get_result()

    session_id = str(session_response['session_id'])

    assistant_response = service.message(
        assistant_id='cc6ddadf-b029-47ac-956a-8ccfdf354996',
        session_id=session_id,
        input={
            'message_type': 'text',
            'text': 'Hello'
        }
    ).get_result()
    print(json.dumps(assistant_response, indent=2))

    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        print("Say something!!!")
        user_input = str(r.recognize_google(audio))
        print(user_input)

    except Exception:
        print("Something went wrong")

    Josh = user_input.find("Josh")
    print(Josh)
    if Josh >= 0:
        assistant_response = service.message(
            assistant_id='cc6ddadf-b029-47ac-956a-8ccfdf354996',
            session_id=session_id,
            input={
                'message_type': 'text',
                'text': user_input
            }
        ).get_result()

        print(json.dumps(assistant_response, indent=2))
        speak = assistant_response['output']['generic'][0]['text']
        engine = pyttsx.init()
        engine.say(speak)
        engine.runAndWait()
    else:
        print("Josh is missing")

