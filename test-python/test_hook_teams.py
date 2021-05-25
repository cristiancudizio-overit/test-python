#https://pypi.org/project/pymsteams/
#pip install pymsteams
import pymsteams

# You must create the connectorcard object with the Microsoft Webhook URL
myTeamsMessage = pymsteams.connectorcard("https://outlook.office.com/webhook/d56a1923-223b-4905-8bf6-ad599ba36d73@09b271bc-ab5f-4085-b239-7132f983f363/IncomingWebhook/26fd3f3a9a2540a5af6b5124da50650e/af60369a-046a-4bcd-a36d-4c81f6a10046")

# Add text to the message.
myTeamsMessage.text("this is my text")

# send the message.

myTeamsMessage.title("This is my message title")
myTeamsMessage.addLinkButton("This is the button Text", "https://github.com/rveachkc/pymsteams/")
#This is useful in the event you need to post the same message to multiple rooms.
#myTeamsMessage.newhookurl("<My New URL>")

# create the section
myMessageSection = pymsteams.cardsection()

# Section Title
myMessageSection.title("Section title")

# Activity Elements
myMessageSection.activityTitle("my activity title")
myMessageSection.activitySubtitle("my activity subtitle")
myMessageSection.activityImage("http://i.imgur.com/c4jt321l.png")
myMessageSection.activityText("This is my activity Text")

# Facts are key value pairs displayed in a list.
myMessageSection.addFact("this", "is fine")
myMessageSection.addFact("this is", "also fine")

# Section Text
myMessageSection.text("This is my section text")

# Section Images
myMessageSection.addImage("http://i.imgur.com/c4jt321l.png", ititle="This Is Fine")

# Add your section to the connector card object before sending
myTeamsMessage.addSection(myMessageSection)
myTeamsMessage.printme()

myTeamsMessage.send()
