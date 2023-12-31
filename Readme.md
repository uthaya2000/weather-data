# Weather Data (Python Fast API)

### Pre-requisites

- Run following commands to run this project
```
pip install fastapi
pip install "uvicorn[standard]"
```



### Project Setup
- Add [Weather API](https://rapidapi.com/weatherapi/api/weatherapi-com) key in env variable
  - ``export API_KEY=<Your API Key>``
- Run below command
  - ``uvicorn main:app --reload``
 
### Sample curL
```
  curl --location 'http://127.0.0.1:8000' \
  --header 'Content-Type: application/json' \
  --data '{
      "city": "tuticorin",
      "output_format": "xml"
  }'
```
```
curl --location 'http://127.0.0.1:8000' \
--header 'Content-Type: application/json' \
--data '{
    "city": "tuticorin",
    "output_format": "json"
}'
```
