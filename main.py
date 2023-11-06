from fastapi import FastAPI
from pydantic import BaseModel
import requests
from fastapi.responses import JSONResponse
import os

from starlette.responses import Response

app = FastAPI()


class City(BaseModel):
    city: str
    output_format: str | None


@app.post("/")
async def get_weather_details(city: City):

    url = "https://weatherapi-com.p.rapidapi.com/current.json?q=" + city.city

    payload = {}
    headers = {
        'X-RapidAPI-Key': os.getenv("API_KEY"),
        'X-RapidAPI-Host': 'weatherapi-com.p.rapidapi.com'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if 200 <= response.status_code <= 299:
        data = response.json()
        location = data['location']
        weather_data = {
            "Weather": f"{str(data['current']['temp_c'])} C",
            "Latitude": str(location['lat']),
            "Longitude": str(location['lon']),
            "City": f"{location['name']}, {location['region']}, {location['country']}"
        }

        if city.output_format is not None and city.output_format.lower() == 'xml':
            xml_str = '<?xml version="1.0" encoding="UTF-8" ?>\n<root>\n'
            for key, value in weather_data.items():
                xml_str += f"<{key}>{value}</{key}>\n"
            xml_str += '</root>'

            xml_response = Response(content=xml_str, media_type="application/xml")
            return xml_response

        return JSONResponse(content=weather_data)

    else:
        err_response = JSONResponse(content={"error": response.text}, status_code=400)
        return err_response
