#!/bin/bash
port=$1
socat tcp4-listen:$port,reuseaddr,fork exec:./honeypot1.py
