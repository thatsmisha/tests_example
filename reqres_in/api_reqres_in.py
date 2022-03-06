import requests

class Error(Exception): #new class for exceptions
    pass

# ---------- Get User -----------

def get_user(user_id):
    url = "https://reqres.in/api/users/" + user_id
    headers = {}
    response = requests.get(url=url, headers=headers)  # making a request

    print(response)

    return(response)

def return_user_email(response):
    if response.status_code == 200:
        resp = response.json()
        user_email = resp['data']['email']
        return user_email
    else:
        raise Error('status_code:', response.status_code, response.text) #raising an error

# ---------- Create User -----------

def create_new_user(name, job):
    url = "https://reqres.in/api/users"
    with open('bodies/create_user.txt', 'r') as file:  # open body
        body = file.read()
    body = body.replace('{{NAME}}', name)  # replace {{NAME}} with name
    body = body.replace('{{JOB}}', job)  # replace {{WORK}} with work
    headers = {}
    response = requests.post(url=url, headers=headers, data=body.encode('utf-8'))  # making a request
    print(response)
    return(response)
