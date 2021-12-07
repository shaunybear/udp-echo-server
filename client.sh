#!/bin/bash

set -x

UDP_SERVER_IP="$1"

nping --udp -p 31700 $UDP_SERVER_IP --data-string "test" --rate 1 --count 60000
