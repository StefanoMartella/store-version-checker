from fastapi import FastAPI
from google_play_scraper import app as playstore_app
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

@app.get("/latest-version/{platform}/{app_id}")
async def get_latest_version(platform: str, app_id: str):
    try:
        if platform.lower() == "android":
            result = playstore_app(app_id)
            return {"platform": "Android", "app_id": app_id, "latest_version": result["version"]}
        
        elif platform.lower() == "ios":
            url = f"https://itunes.apple.com/lookup?bundleId={app_id}"
            response = requests.get(url)
            data = response.json()  
            if data["resultCount"] > 0:
                version = data["results"][0]["version"]
                return {"platform": "iOS", "app_id": app_id, "latest_version": version}
            else:
                return JSONResponse(status_code=404, content={"error": "App not found in the App Store"})
        
        else:
            return JSONResponse(status_code=400, content={"error": "Invalid platform. Use 'android' or 'ios'."})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
