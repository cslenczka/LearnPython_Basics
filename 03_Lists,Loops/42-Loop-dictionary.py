# loop and add data to the existing dictionary

spanish_translations = { "dog": "perro", "house": "casa", "cat": "gato" }

# Programatically add the following translations to the spanish_translations dictionary:
#  love -> amor
#  code -> codigo
#  smart -> inteligente

print('The original dictionary: \n' + str(spanish_translations))
print('**********')

# add the above values to the dictionary

spanish_translations["love"] = "amor"
spanish_translations["code"] = "codigo"
spanish_translations["smart"] = "inteligente"

print('New dictionary adding elements programatically: \n' + str(spanish_translations))
print('**********')

# add the above values to the dictionary using a loop

new_words = {"love": "amor", "code": "codigo", "smart": "inteligente"}
for key, value in new_words.items():
    spanish_translations[key] = value

print('New dictionary adding elements using a loop: \n' + str(spanish_translations))

# add the above values to the dictionary using a loop and a function

def add_to_dict(dictionary, new_words):
    for key, value in new_words.items():
        dictionary[key] = value
    return dictionary

new_words = {"love": "amor", "code": "codigo", "smart": "inteligente"}
print('**********')
print('New dictionary adding words using a loop and a function: \n' + str(add_to_dict(spanish_translations, new_words)))

