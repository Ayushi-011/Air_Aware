import httpx

async def get_loc( ip:str ):
    async with httpx.AsyncClient() as client1:
        loc = await client1.get(f"https://ipwho.is/{ip}")
        return loc.json()