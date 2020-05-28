import aiml
 
k = aiml.Kernel()
k.learn("data.aiml")
print("")
print("Klient wchodzi do sklepu z obuwiem i podchodzi do obslugi, aby sie przywitac")
print("")
while True:
    print(k.respond(input("> ")))
