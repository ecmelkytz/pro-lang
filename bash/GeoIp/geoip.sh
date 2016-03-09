#!/bin/bash

GETGEOIPCONTEXT="http://www.webservicex.net/geoipservice.asmx/GetGeoIPContext"
GETGEOIP="http://www.webservicex.net/geoipservice.asmx/GetGeoIP"


get_ip() {
  curl -H "Accept: application/soap+xml" -d "IPAddress=$1" ${GETGEOIP}
}

my_ip() {
  curl -H "Accept: application/soap+xml" -d "IPAddress=$1" ${GETGEOIPCONTEXT}
}

$@
