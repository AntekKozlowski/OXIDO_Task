import openai

#Klucz api usuniety aby nie udostepniac go w publicznym repo na githubie
openai.api_key = ''

with open('artykulTekst.txt', 'r') as f:
    artykul = f.read()

prompt = (
        "Create HTML code based on the article, containing content between <body> </body> tags, without <html>, <head>, or <body> tags. "
        "Use appropriate HTML tags to structure the content. Indicate places for images using the <img src=\"image_placeholder.jpg\" alt=\"precise description\"> "
        "tag, where alt includes a precise description of what the image should depict for it to be generated. "
        "Add short captions below the images using an appropriate HTML tag. Do not include any CSS or JavaScript.\n\n" + artykul
)

response = openai.chat.completions.create(
    model='chatgpt-4o-latest',
    messages=[
        {
        "role": "user",
         "content": prompt
        }
    ]
)

htmlGenText = response.choices[0].message.content

with open('artykul.html', 'w') as f:
    f.write(htmlGenText)

print("Zakonczono sukcesem")