#!/bin/bash

/opt/google/chrome/google-chrome --profile-directory=Default >/dev/null 2>&1 &
/opt/google/chrome/google-chrome --profile-directory="Profile 1" >/dev/null 2>&1 &

