import openai

openai.api_key = "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"


def generate_response(prompt):
    model_engine = "text-davinci-003"

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=4024,
        n=1,
        stop=None,
        temperature=0,
    )

    message = completions.choices[0].text
    return message.strip()


while True:
    questions_nb = input("Combien de questions? ")
    if questions_nb != "exit":
        chapter = input("Quel chapitre? ")
        book = input("Quel livre? ")
        writer = input("Quel ecrivain ")
        prompt = f"{questions_nb} questions sur le chapitre { chapter} de {book} de {writer} avec 4 choix pour chaque question"
        print(prompt)   
        response = generate_response(prompt)
        print(response)
    else:
        break
