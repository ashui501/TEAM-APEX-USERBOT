import os
   
PREFIXES = ['!', '/', '$'] 
   
OWNER_ID = os.getenv("OWNER_ID",1238234357)
HANDLER = ["~", ".","!","?","@","$"]
BARATH = "https://te.legra.ph/file/6a839cecad51014a32254.mp4"
GROUP_ID = os.getenv("GROUP_ID", "-1002119409366")
SOURCE = "https://github.com/SIAmKira/PyroX-V2"
LOG_CHAT = -1002119409366
SUDOS = getenv("SUDO_USERS", None)
SUDO_USERS = []
if SUDOS:
    sudos = str(SUDOS).split(" ")
    for sudo_id in sudos:
        SUDO_USERS.append(int(sudo_id))
SUDO_USERS.append(OWNER_ID)
for x in Barath:
    SUDO_USERS.append(x)
