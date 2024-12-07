import requests

def send_test_result(test_case_id, status_id, comment, username, password):
    url = 'https://<your_testrail_url>/index.php?/api/v2/add_result_for_case/<run_id>/{test_case_id}'
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        'status_id': status_id,
        'comment': comment,
    }
    response = requests.post(url, headers=headers, json=data, auth=(username, password))
    return response.json()