#!/usr/bin/env bash
APP_NAME='nd082-marten'
LOCATION='westeurope'
SKU='FREE'

az webapp up -n $APP_NAME -l $LOCATION --sku $SKU

./make_predict_azure_app.sh

locust -f locustfile.py -H https://$APP_NAME.azurewebsites.net