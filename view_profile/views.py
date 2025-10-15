import requests
from django.http import JsonResponse
from datetime import datetime, timezone

def profile_view(request):
    try:
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        response.raise_for_status()
        cat_fact = response.json().get("fact", "Cats are awesome!")
    except Exception:
        cat_fact = "Could not fetch a cat fact right now."

    data = {
        "status": "success",
        "user": {
            "email": "omajeneoghenefega11@gmail.com",
            "name": "Oghenefega Omajene",
            "stack": "Python/Django"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
    }

    return JsonResponse(data)
