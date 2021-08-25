#!/usr/bin/env python3

### IMPORTS ###
import os
import pytest

import app

### GLOBALS ###

### FUNCTIONS ###
@pytest.fixture
def api():
    return app.api

def test_get(api):
    r = api.requests.get("/")
    assert r.status_code == 200

### CLASSES ###
