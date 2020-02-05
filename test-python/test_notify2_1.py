import time 
import notify2 

# path to notification window icon 
ICON_PATH = "C:\Development-cri\test-python\test-python\alert16.gif"
  
# fetch news items 
#newsitems = topStories() 
  
# initialise the d-bus connection 
notify2.init("News Notifier") 
  
# create Notification object 
n = notify2.Notification(None, icon = ICON_PATH) 
  
# set urgency level 
n.set_urgency(notify2.URGENCY_NORMAL) 
  
# set timeout for a notification 
n.set_timeout(10000) 

 
# update notification data for Notification object 
n.update('titolo', 'descrizione') 

# show notification on screen 
n.show() 

# short delay between notifications 
time.sleep(15) 
