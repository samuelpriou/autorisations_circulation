"""
    Dev server. Do not use this in production.

    Use a WSGI setup instead.
"""

import os
import argparse

parser = argparse.ArgumentParser(description='Run the development server')
parser.add_argument('--config-file', help='Path to the config file')
parser.add_argument('--host', help='Serve to this host', default="127.0.0.1")
parser.add_argument('--port', help='Serve to this port', default=5000, type=int)

args = parser.parse_args()
os.environ.setdefault('AUTH_CIRCU_CONFIG_FILE', args.config_file or "")

from auth_circu.routes import app  # noqa
from auth_circu.db.utils import init_db  # noqa

# help for debugging. Do not use that in producting.
app.config['DEBUG'] = True
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['INIT_APP_WITH_DB'] = True

init_db(app)

app.run(host=args.host, port=args.port, threaded=True)
