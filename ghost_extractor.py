import os
from googleapiclient import discovery
def pull_absolute_metadata():
    service = discovery.build('compute', 'v1')
    hc_request = service.healthChecks().aggregatedList(project="enter-empire-pro")
    while hc_request is not None:
        hc_response = hc_request.execute()
        for scope, items in hc_response.get('items', {}).items():
            if 'healthChecks' in items:
                for hc in items['healthChecks']:
                    print(f"SENTRY: {hc['name']} | URI: {hc['selfLink']}")
        hc_request = service.healthChecks().aggregatedList_next(hc_request, hc_response)
if __name__ == "__main__":
    pull_absolute_metadata()
