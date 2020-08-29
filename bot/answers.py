import random

#diferentes respuestas a diferentes solicitudes del usuario

def greetAnswers():
    answers = ["Hola, buen día Yeison", "Gracias por saludar","Buen día jefe", "Hola, gracias por saludar, que tenga un buen dia Yeison"]

    answer = random.choice(answers)
    return answer

def thanksAnswers():
    answers = ["¡¡De nada Yeison, para servirte!!😎", "¡¡Espero que sea de ayuda💪!!", "¡¡Pasostamos!!🤙", "¡¡Es un placer servirte!!😺"]
    answer = random.choice(answers)
    return answer

def pleaseAnswers():
    answers = ["Claro que si!!", "Dame un momento", "Estoy trabajando en ello"]
    answer = random.choice(answers)
    return answer
