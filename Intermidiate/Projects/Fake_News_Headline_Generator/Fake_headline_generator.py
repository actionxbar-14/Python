
# step 1 : import the random module

import random 

# step 2 : create subjects 

subjects = [
    "Shah Rukh Khan",
    "Narendra Modi",
    "Rahul Gandhi",
    "Virat Kohli",
    "Elon Musk",
    "Salman Khan",
    "Deepika Padukone",
    "Rohit Sharma",
    "MS Dhoni",
    "Alia Bhatt",
    "Bill Gates",
    "Cristiano Ronaldo",
    "Lionel Messi",
    "Amitabh Bachchan",
    "Ranveer Singh",
    "Hardik Pandya",
    "Sundar Pichai",
    "Mark Zuckerberg",
    "Akshay Kumar",
    "Kangana Ranaut"
]


actions = [
    "launches",
    "cancels",
    "dances with",
    "fights with",
    "collaborates with",
    "secretly meets",
    "announces new plan with",
    "starts controversy with",
    "tweets about",
    "accidentally leaks",
    "celebrates with",
    "gets spotted with",
    "argues with",
    "starts business with",
    "reveals truth about",
    "joins",
    "quits",
    "invests in",
    "creates meme with",
    "goes viral with"
]


places = [
    "at Red Fort",
    "in Mumbai local train",
    "inside Parliament",
    "on Instagram Live",
    "at IPL match",
    "in Dubai",
    "at a secret party",
    "in a village",
    "on a private jet",
    "during press conference",
    "in a reality show",
    "at a wedding",
    "in a college fest",
    "on the streets of Delhi",
    "at a startup event",
    "in a movie set",
    "during election rally",
    "at midnight",
    "on Twitter",
    "in a five-star hotel"
]


emojis = [
    "\U0001F525",
    "\U0001F602",
    "\U0001F631",
    "\U0001F60E",
    "\U0001F680",
    "\U0001F92F",
    "\U0001F4A5",
    "\U0001F976",
    "\U0001F440",
    "\U0001F64C",
    "\U0001F921",
    "\U0001F480",
    "\U0001F973",
    "\U0001F4E2",
    "\u26A1",
    "\U0001F620",
    "\U0001F634",
    "\U0001F914",
    "\U0001F911"
]




# step 3 : start the headline generation loop 

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place  = random.choice(places)
    emoji  = random.choice(emojis)
    
    headline = f" BREAKING NEWS : {subject} {action} {place} {emoji}"
    
    print("\n" + headline)
    
    user_input = input("\n Do You want another headline ? (yes/no) : ").strip().lower() 
    
    if user_input == 'no':
        break 
    
 
print("\n Thanks For using the fake headline generator!!!")   
    