import os
import openai
#open_ai_key="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"
#openai.api_key=os.getenv("open_ai_key")
openai.api_key="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"
prompt=input("Enter here:")
completion=openai.Completion.create(
    engine='text-davinci-003',
    prompt= prompt,
    max_tokens=3000,
    n=1,
    stop=None,   
    temperature=0.8
    
)
response=completion.choices[0].text 
print(response)