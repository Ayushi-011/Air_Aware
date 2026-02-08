from fastapi import APIRouter,Request
from services.ip_service import get_ip
from services.geo_service import get_loc
from services.aqi_service import get_aqi
from models.schemas import Op

router = APIRouter()

@router.get("/aqi")
async def home( ip1:Request, ip2:str=None, Response_model=Op):
    ip = await get_ip(ip1,ip2)
    loc = await get_loc(ip)
    aqi = await get_aqi(loc.get("latitude"),loc.get("longitude"))
    category = "Not-Defined"
    if int(aqi)<50:
        category = "Good AQI"
    elif int(aqi)<100:
        category = "Moderate AQI"
    elif int(aqi)<150:
        category = "Unhealthy for Sensitive Groups"
    elif int(aqi)<200:
        category = "Unhealthy AQI"
    elif int(aqi)<300:
        category = "Very Unhealthy AQI"
    else:
        category = "Hazardous AQI" 


    return {
        "ip" : ip,
        "location" :
        {
            "city": loc.get("city"),
            "region": loc.get("region"),
            "country": loc.get("country"),
            "lat": loc.get("latitude"),
            "lon": loc.get("longitude"),
        },
        "aqi" :
        {
            "value" : aqi,
            "category" : category,
        },
        "src" : "open-meteo"
    } 


    

