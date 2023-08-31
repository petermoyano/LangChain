import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """Scrape information from Linkedin profiles,
    Manually scrape the information from the LinkedIn profile."""

    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"

    header_dic = {
        'Authorization': f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'
    }

    response = requests.get(
        api_endpoint, params={'url': linkedin_profile_url}, headers=header_dic
    )

    # Clean json response from unnecessary fields
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)  # Avoid any field that is empty
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            # remove picture since we won't use it
            group_dict.pop("profile_pic_url")

    return data
