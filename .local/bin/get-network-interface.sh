#!/usr/bin/env bash
route |
    grep default |
    head -1 |
    awk '{print $8}'
