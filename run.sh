#!/bin/bash

# Flask stuff
export FLASK_APP=reference
export FLASK_ENV=development

# Install dependencies only if needed
python setup.py develop

# Run
flask run
