# HNG13 Task | Stage 0 | Backend | Profile API — Django

A simple Django API endpoint that returns a user's profile information along with a random cat fact fetched from the [Cat Facts API](https://catfact.ninja/fact).

This project was built as part of the HNG13 Internship task.

---

## 🚀 Features

- Returns user profile info and a random cat fact at `/me`
- Gracefully handles external API errors
- Includes timestamp and proper JSON response
- Uses environment variables for configuration
- Deployed on [Railway](https://railway.app/)

---

## 🧩 API Endpoint

| Method | Endpoint | Description |
|:-------|:----------|:-------------|
| GET | `/me` | Returns user profile with a cat fact |

### ✅ Example Response

```json
{
  "status": "success",
  "user": {
    "email": "omajeneoghenefega11@gmail.com",
    "name": "Oghenefega Omajene",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-15T18:25:43Z",
  "fact": "Cats sleep 70% of their lives."
}


```

## 💻 Tech Stack

- `Backend:` Django

- `Language:` Python

- `HTTP Client:` requests

- `Environment Management:` python-decouple or python-dotenv

- `Deployment:` Railway


---

## ⚙️ Environment variables
- Create a .env file in the project root:
```env
DJANGO_SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=*

```
## You can generate a new Django secret key from your terminal with
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"


```
## Cloning the repository
```bash
git clone https://github.com/404khai/hng13-profile-api-django.git
cd hng13-profile-api-django


```
## Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate     # On macOS/Linux
venv\Scripts\activate        # On Windows
