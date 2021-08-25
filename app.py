#!/usr/bin/env python3

### IMPORTS ###
import logging
import os
import random

import responder

import images

### GLOBALS ###
LISTENER_PORT = os.getenv('PORT', '8080')

api = responder.API()

### FUNCTIONS ###
@api.route("/")
def root(req, resp):
    base64_image = random.choice(images.catternaut_images_embed)
    output_html = "<html><body><h1>Catternaut:</h1><img src=\"{}\"></img></body></html>".format(base64_image)
    logging.debug("GET Response: %s", output_html)
    resp.html = output_html

### CLASSES ###

### MAIN ###
def main():
    # Init logging
    log_format = "%(asctime)s:%(levelname)s:%(name)s.%(funcName)s: %(message)s"
    logging.basicConfig(format=log_format, level=logging.DEBUG)

    # Start the http server
    logging.info("Starting https...")
    api.run()

if __name__ == '__main__':
    main()
