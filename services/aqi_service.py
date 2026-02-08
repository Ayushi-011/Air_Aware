import httpx

async def get_aqi( lat:str, long:str):
    async with httpx.AsyncClient() as client1:
        aqi = await client1.get(f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={lat}&longitude={long}&current=us_aqi")
        data = aqi.json()
        return data.get("current",{}).get("us_aqi")