## pyscpapi


!!The module is not written by me!!
Author: ꜱʀ.ꜱʜᴇʀᴏʟʟᴅ#6858


# Installing

You can get the library directly from PyPI:
```
python3 -m pip install pyscpapi
```

If you are using Windows, then the following should be used instead:
```
py -3 -m pip install pyscpapi
```

# HOW TO USE
Read official API:
https://api.scpslgame.com/

Simple Code:

```py
import asyncio
from Pyscp_Api.api import API

async def start():
    ip = await API.ip()
    serverinfo = await API.serverinfo(id_ = YOUR_ID, key = YOUR_KEY, list_ = "true", players = "true")
    lobbylist = await API.lobbylist(key = YOUR_KEY, minimal = "Test")
    return (ip, serverinfo, lobbylist)
  
ip, serverinfo, lobbylist = asyncio.run(start())
print(f"IP:          {ip}")
print(f"Server Info: {serverinfo}")
print(f"Lobby List:  {lobbylist}")
```


# Donate
https://money.yandex.ru/to/410015858804944/0


