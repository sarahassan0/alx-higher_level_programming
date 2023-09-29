#!/bin/bash
# displays the size of the body of the response to the URL using Curl.
curl -s "$1" | wc -c
