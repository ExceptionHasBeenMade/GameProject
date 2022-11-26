# jsonClosing(importedCargo, pathOfCargo)
# jsonClosing(importedResources, pathOfResources)
# jsonClosing(importedHarbors, pathOfHarbors)
# jsonClosing(importedSettings, pathOfSettings)
# jsonClosing(importedConveyance, pathOfConveyance)
# jsonClosing(importedOwns, pathOfOwns)

# x = 5
# for i in range(x):
#     print(i+1)

import threading
import time
  
def print_project():
    for i in range(5):

        time.sleep(1)
        print("project")
  
def print_natural():
    for i in range(5):
        #the current thread is suspended
        time.sleep(1.5)
        print("natural")
  

t1 = threading.Thread(target=print_project)
t2 = threading.Thread(target=print_natural)
t1.start()
t2.start()