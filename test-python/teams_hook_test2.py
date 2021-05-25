#https://pypi.org/project/pymsteams/
#pip install pymsteams
import pymsteams

# You must create the connectorcard object with the Microsoft Webhook URL
myTeamsMessage = pymsteams.connectorcard("https://outlook.office.com/webhook/d56a1923-223b-4905-8bf6-ad599ba36d73@09b271bc-ab5f-4085-b239-7132f983f363/IncomingWebhook/26fd3f3a9a2540a5af6b5124da50650e/af60369a-046a-4bcd-a36d-4c81f6a10046")

# Add text to the message.
myTeamsMessage.text("this is my text")

# send the message.

myTeamsMessage.title("This is my message title")
#This is useful in the event you need to post the same message to multiple rooms.
#myTeamsMessage.newhookurl("<My New URL>")

# Create Section 1
Section1 = pymsteams.cardsection()
Section1.text("My First Section")
Section1.addFact("pippero", "is fine")
# Create Section 2
Section2 = pymsteams.cardsection()
Section2.text("My Second Section")
Section2.addFact("pippero", "is finer")
# Add both Sections to the main card object
myTeamsMessage.addSection(Section1)
myTeamsMessage.addSection(Section2)


#myTeamsMessage.addLinkButton("This is the button Text", "https://github.com/rveachkc/pymsteams/")
# Then send the card
myTeamsMessage.printme()

myTeamsMessage.send()
