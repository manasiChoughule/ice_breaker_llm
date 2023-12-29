import os
import requests
import json


def scrape_linkedin_profile(linkedin_profile_url: str):
    """
    scrape information from LinkedIn Profiles,
    Manually scrape the information from the LinkedIn profile
    """

    ## Uncomment it when using API calls

    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )
    data = response.json()

    ## static testing data

    # static_json = open('third_parties/eden_marco.json')
    #
    # data = json.load(static_json)

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
