import random

PROMPTS = [

    "A futuristic Indian city at night",

    "A dragon flying above snowy mountains",

    "A cyberpunk Kolkata street",

    "A magical forest with glowing trees",

    "A robot chef cooking food",

    "An astronaut riding a tiger",

    "A floating castle in the clouds",

    "A cat wearing sunglasses",

    "An ancient temple on Mars",

    "A giant turtle carrying a city"
]

def get_random_prompt():
    return random.choice(PROMPTS)