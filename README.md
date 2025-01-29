# Play Store & App Store Version Checker API

A FastAPI-based microservice that fetches the latest version of an app from the Google Play Store and Apple App Store using package names.

## Features
- Retrieve the latest app version from the **Google Play Store** using `google-play-scraper`
- Retrieve the latest app version from the **Apple App Store** using the iTunes Search API
- Hosted on **Render** with **Docker**

## API Endpoints
### Get Latest Version
#### Request:
```
GET /latest-version/{platform}/{app_id}
```

| Parameter  | Type   | Description |
|------------|--------|-------------|
| `platform` | string | `android` or `ios` |
| `app_id`   | string | Package name (Android) or numeric App Store ID (iOS) |

#### Example Usage
- **Android:** `GET /latest-version/android/<it.package.name>`
- **iOS:** `GET /latest-version/ios/<it.package.name>`

#### Response:
```json
{
  "platform": "Android",
  "app_id": "it.package.name",
  "latest_version": "2.24.3.77"
}
```

## Installation & Setup
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/playstore-version-checker.git
cd playstore-version-checker
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the API Locally
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

### 4. Run with Docker
#### Build the Docker Image:
```bash
docker build -t playstore-api .
```

#### Run the Container:
```bash
docker run -p 8000:8000 playstore-api
```

## License
This project is licensed under the MIT License.

## Author
Developed by Stefano Martella.