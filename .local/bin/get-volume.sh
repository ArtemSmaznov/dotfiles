#!/usr/bin/env bash
amixer sget Master | grep "%" | awk -F'[][]' '{print $2}' | tr -d '%' | sort -r | head -1
