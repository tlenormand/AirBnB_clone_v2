#!/usr/bin/python3.8

"""
List all States through an end point
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """
    teardown the database, to reset it.
    """
    storage.close()


@app.route('/states', strict_slashes=False)
def statesList():
    """

    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('9-states.html', states=states, choice=True)


@app.route('/states/<id>', strict_slashes=False)
def statesCityList(id):
    """

    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    for state in states:
        if state.id == id:
            return render_template('9-states.html', states=state, choice=False)
    return render_template('9-states.html', states=False, choice=False)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    cities = list()

    for state in states:
        for city in state.cities:
            cities.append(city)

    return render_template('10-hbnb_filters.html',
                            states=states, state_cities=cities,
                            amenities=amenities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
