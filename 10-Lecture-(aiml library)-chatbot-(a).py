import aiml


kernel=aiml.Kernel()
kernel.learn("greetings.aiml")

while True:
    print(kernel.respond(input("Enter your Message  :")))

