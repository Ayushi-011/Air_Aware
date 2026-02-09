# Air_Aware
Implementation of a production-ready FastAPI backend that determines a client’s geographic location from their IP address and retrieves real-time air quality information for that location.  
**Air Aware** is a lightweight Streamlit web app that provides real-time **air quality and weather insights** based on the user’s IP-derived location. It combines geolocation, weather, and AQI data to promote environmental awareness in a simple and interactive way.

---
## For Front_End Implementation
The project has front-end at [this link](https://github.com/Ayushi-011/Air_Front_End)
Also visit the front-end repo, as this link of front-end repo contains the required implementation of "Timeout Handling" and "Caching Strategy."  
The site can be visited at https://find-your-aqi.streamlit.app/

##  Features
- Automatic location detection using IP address  
- Current weather and air quality information  
- Clean, minimal Streamlit UI  
- Fast responses using API caching and retries  

---

##  Tech Stack
- **Python**
- **Streamlit**
- **ipwho.is API** – IP-based geolocation  
- **Open-Meteo API** – Weather & Air Quality data  

---

##  Run Locally (Streamlit)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Ayushi-011/Air_Aware.git
cd Air_Aware
```
### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Run the app
```bash
unicorn main:app --reload
```

**The app will be available at:**
http://127.0.0.1:8000/aqi

##  Design Choices
###  Why ipwho.is
- Free and reliable IP-based geolocation service  
- No API key required  
- Returns latitude, longitude, city, and country in a single request  
- Supports detection of private and local IP addresses  

###  Why Open-Meteo
- Free and open-source API  
- No authentication required  
- Provides accurate global weather and air quality data  
- Well-documented and developer-friendly  

###  Caching Strategy
- 15-minute TTL caching for geolocation and AQI data  
- Reduces redundant API calls  
- Improves performance and response time  

###  Retry and Timeout Configuration
- Automatic retries for temporary network failures  
- Request timeouts prevent application freezing  
- Ensures a smoother and more reliable user experience  

###  Handling Private / Local IP Addresses
- Detects private or localhost IPs (e.g., `127.0.0.1`)  
- Falls back to a default or safe location when required  
- Prevents crashes during local development and testing

## Folder Structure
```text
Air_Aware/
 ├── main.py
 ├── routers/
 │    └── aqi.py
 ├── services/
 │    ├── ip_service.py
 │    ├── geo_service.py
 │    └── aqi_service.py
 ├── models/
 │    └── schemas.py
 └── README.md
```
