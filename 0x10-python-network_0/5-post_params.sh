#!/bin/bash
# displays the size of the body of the response to the URL using Curl.
curl -LdX POST "email=test@gmail.com&subject=I will always be here for PLD" "$1"
