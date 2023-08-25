import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_home():
    return "I am CI/CD hero!"

if __name__ == '__main__':
    app.run(
      debug=True,
      host="0.0.0.0" # Listen for connections _to_ any server
    )

# if __name__ == '__main__':
#   app.run(debug=True)

# if __name__ == '__main__':
#     # We also run the server differently depending on the environment.
#     # In production we don't want the fancy error messages — users won't know
#     # what to do with them. So no `debug=True`
#     if os.environ.get("APP_ENV") == "PRODUCTION":
#         app.run(port=5000, host='0.0.0.0')
#     else:
#         app.run(debug=True, port=5000, host='0.0.0.0')
