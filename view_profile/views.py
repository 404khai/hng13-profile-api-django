import logging
import requests
from django.http import JsonResponse
from datetime import datetime, timezone
from decouple import config

# Configure logging
logger = logging.getLogger(__name__)

CAT_FACT_API = config("CAT_FACT_API", default="https://catfact.ninja/fact")

def profile_view(request):
    try:
        response = requests.get(CAT_FACT_API, timeout=5)
        response.raise_for_status()
        cat_fact = response.json().get("fact", "Cats are awesome!")
        status_code = 200
    except requests.exceptions.Timeout:
        logger.warning("Cat Facts API request timed out.")
        cat_fact = "Cat Fact service is taking too long to respond."
        status_code = 504  # Gateway Timeout
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching cat fact: {e}")
        cat_fact = "Could not fetch a cat fact right now."
        status_code = 503  # Service Unavailable

    data = {
        "status": "success" if status_code == 200 else "error",
        "user": {
            "email": "omajeneoghenefega11@gmail.com",
            "name": "Oghenefega Omajene",
            "stack": "Python/Django",
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact,
    }

    return JsonResponse(data, status=status_code)
