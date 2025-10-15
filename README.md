# HNG13 Task| Stage 0 | Backend | Profile API — Django

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
