# Barcode generator for scanner testing

## Purpose

This software has been written to test a barcode scanner over a long period
of time.

Just scanning random barcodes might not lead to the point were the problem actually appears, and does
not lead to a stable reproduction method.

This application will show Code128 barcodes in a loop with a user configurable interval.
The barcodes will contain a sequence number and the current time.

## Barcode contents
 
* "#00001 17:24:46.450663"
* "#00002 17:24:47.450663"
* "#00003 17:24:48.450663"
* "#00004 17:24:49.450663"

## Requirements

This project is writting in Python3 and makes use of 

