import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """Scrape information from Linkedin profiles,
    using the Linkedin API."""
    # api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    # header_dic = {
    #     'Authorization': f'Bearer {os.environ.get("PROXUCURL_API_KEY")}'}

    print("PROXYCURL KEEYYYYYYYYYYY", os.environ["PROXYCURL_API_KEY"])

    # response = requests.get(
    #     api_endpoint, params={'url': linkedin_profile_url}, headers=header_dic
    # )
    # return response
    response = requests.get(
        "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
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


# python3 code to scrape my linkedin profileS
# api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
# api_key = 'w3Mc8o6ivTwk_yGaH62JKw'
# print(api_key)
# header_dic = {'Authorization': 'Bearer ' + api_key}
# params = {
#     'url': 'https://www.linkedin.com/in/pedro-moyano/',
# }
# response = requests.get(api_endpoint, headers=header_dic, params=params)
