from fastapi import Request
import httpx

async def get_ip(ip1:Request, ip2:str=None):
    if ip2:
        return ip2
    sent = ip1.headers.get("X-Forwarded-For")
    if sent : 
        return sent.split(",")[0].strip()
    return ip1.client.host

async def diff_ip():
    async with httpx.AsyncClient() as client1:
        res = await client1.get("https://api.ipify.org?format=text")
        return res.text


