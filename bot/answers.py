import random

#diferentes respuestas a diferentes solicitudes del usuario

def greetAnswers():     
    responses = ["Hola buenas Yeison!!", "Gracias por saludar!!", "Hola Yeison!!", "Hola, en que te puedo ayudar?", "Hola buenas, en que te puedo ayudar?", "Hola Yeison, hablame parcero, que necesitas?", "La buena Yison, en que te ayudo?"]    
    answer = random.choice(responses)
    return answer

def thanksAnswers():
    answers = ["¡¡De nada Yeison, para servirte!!😎", "¡¡Espero que sea de ayuda💪!!", "¡¡Pasostamos!!🤙", "¡¡Es un placer servirte!!😺"]
    answer = random.choice(answers)
    return answer

def pleaseAnswers():
    answers = ["Claro que si!!", "Dame un momento", "Estoy trabajando en ello"]
    answer = random.choice(answers)
    return answer
