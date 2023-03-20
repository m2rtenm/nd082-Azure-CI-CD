#!/usr/bin/env bash
APP_NAME='nd082-marten'
LOCATION='westeurope' # closest location geographically
SKU='FREE' # for cost effective purposes

az webapp up -n $APP_NAME -l $LOCATION --sku $SKU