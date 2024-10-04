import random
from openai import OpenAI
from pick_stock import make_pick
from trader import make_trade

import pick_stock
from trader import make_trade

with open('api_keys.txt', 'r') as f:
    api_keys = f.read().splitlines()

openai_key = api_keys[3]
client = OpenAI(api_key=openai_key)

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "image_url",
          "image_url": {
            "url": "https://i.gyazo.com/57650d83981cbfc7d0a06851e0c412f8.png"
            }
        },
        {
          "type": "text",
          "text": "Analyze the attached image of an EA FC25 match result screen. Calculate the average match rating for all the players and return this value in the exact format: average_rating = {average rating}. Then determine if the team named \"Tinos\" won or lost. Return this as a boolean in the format: result = {result}. Do not explain anything, simply return the two variable results and NOTHING else."
        }
      ]
    },
  ],
  temperature=0,
  max_tokens=500,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  response_format={
    "type": "text"
  }
)

response_vars = response.choices[0].message.content
#parse the response_vars string to get the two variables
response_vars = response_vars.split("\n")
average_rating = response_vars[0].split("=")[1].strip()
result = response_vars[1].split("=")[1].strip()

print("Average Rating: " + average_rating)
print("Win: " + result)

score = float(average_rating) + random.uniform(0.001, 0.009)

loss_penalty = random.uniform(0.5, 2.0)
if result == "False":
    score = score - loss_penalty

stock_to_buy = make_pick(score)
make_trade(stock_to_buy, score)