#!/bin/bash
cd ..
poetry update
poetry shell
python batch_BizInfo/main.py
python batch_BizInfo/zipcode.py