from urllib import request
import requests
from mohawk import Sender

id = "a206c5980f385ba96ff3f1b5979986c0d11a058e"
key = "33d1ac21bec6cae44c2d7bedcb521938b9b3d436"
sender = Sender({
    'id': 'a206c5980f385ba96ff3f1b5979986c0d11a058e',
    'key': '33d1ac21bec6cae44c2d7bedcb521938b9b3d436',
    'algorithm': 'sha256'
}, "http://127.0.0.1:8000/api/v2.1/test/",
method="GET", content="", content_type="application/x-www-form-urlencoded", always_hash_content=False)

response = requests.get("http://127.0.0.1:8000/api/v2.1/test/", data="", headers={
    'Authorization': sender.request_header,
    'Content-Type': 'application/x-www-form-urlencoded',
})

import pdb; pdb.set_trace()
# sender.accept_response(response.headers['Server-Authorization'])

