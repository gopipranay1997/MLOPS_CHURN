#!/bin/bash
set -e
python test_churn.py && python server.py
