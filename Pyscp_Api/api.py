import aiohttp
import asyncio
import ujson


# Errors
class ServerError(Exception):
    pass

class API():
    @staticmethod
    async def serverinfo(id_: int, key: str, lo: str = "false", players: str = "false", list_: str = "false", info: str = "false",\
    pastebin: str = "false", version: str = "false", flags: str = "false", nicknames: str = "false", online: str = "false") -> dict:
        """
        Returns info about own servers.
        """

        params = {'id':        id_,
                  'key':       key,
                  'lo':        lo,
                  'players':   players,
                  'list':      list_,
                  'info':      info,
                  'pastebin':  pastebin,
                  'version':   version,
                  'flags':     flags,
                  'nicknames': nicknames,
                  'online':    online,
        }

        headers = {"accept": "application/json"}

        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.scpslgame.com/serverinfo.php', params=params, headers = headers) as resp:
                status = resp.status
                json_ = ujson.loads(await resp.text())
                if status == 200:
                    return json_
                else:
                    raise (ServerError(f"[{status}] {json_['Error']}"))

    @staticmethod
    async def lobbylist(format_: str = "json", key: str = None, minimal: str = None) -> dict:
        """
        Returns full servers list.
        """

        params = {'format': format_,
                  'key':    key,
        }

        if minimal:
            params["minimal"] = minimal

        headers = {"accept": "*/*"}

        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.scpslgame.com/lobbylist.php', params=params, headers = headers) as resp:
                status = resp.status
                if status == 200:
                    json_ = ujson.loads(await resp.text())
                    return json_
                else:
                    text = await resp.text()
                    raise (ServerError(f"[{status}] {text}"))

    @staticmethod
    async def ip() -> str:
        """
        Returns current IP.
        """

        headers = {"accept": "*/*"}
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.scpslgame.com/ip.php', headers = headers) as resp:
                status = resp.status
                text = await resp.text()

                if status == 200:
                    return text

                else:
                    raise (ServerError(f"[{status}] {text}"))


