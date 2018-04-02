#!/bin/sh
openssl genrsa -des3 -out private.pem 2048
openssl rsa -in private.pem -outform PEM -pubout -out public.pem
openssl rsautl -encrypt -in flag.txt -pubin -inkey public.pem > encrypted.rsa