import wikipedia



search=input("enter the topic you want: ")
print(wikipedia.summary(search))

language="et"

wikipedia.set_lang(language)

print("summary of ethiopian education {language}: ", wikipedia.page("Ethiopian Education").summary)