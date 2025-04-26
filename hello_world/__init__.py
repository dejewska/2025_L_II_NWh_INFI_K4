from flask import Flask # noqa
app = Flask(__name__)

import hello_world.views # noqa
