import azure.functions as func
import logging
import json

data = {
  "about us": {
    "name": "Sandhata Technologies",
    "Countries": "United Kingdom, Inida, United States, South Africa",
    "Continents": "Asia, Europe, Africa, North America",
    "phone": "+44 2076807105",
    "Website": "https://www.sandhata.com",
    "summary": "We transform IT for business",
    "location": {
      "address": "Thanet House, 231 232 Strand",
      "postalCode": "WC2R 1DA",
      "city": "London",
      "countryCode": "UK",
    },
    "socials": [{
      "Facebook": "https://www.facebook.com/Sandhata",
      "Instagram": "https://www.instagram.com/sandhatatech/",
      "Linkedin": "https://in.linkedin.com/company/sandhata-technologies-limited"
    }]
  },
  "customers": [{
    "Clients": "Reliance, Bank of America, BMC, Verizon, Oracle, Vodafone",
  }]
}

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="sandhata")
def sandhata(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(json.dumps(data, indent=2),
                             mimetype="application/json",
                             status_code=200)

    # name = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')

    # if name:
    #     return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )