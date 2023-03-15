#!/usr/bin/env bash
stream=$( amixer sget Master | grep "%" | awk -F'[][]' '{print $4}' | sort -u )
if [ $stream == "on" ]
then echo off
else echo on
fi
