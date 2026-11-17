#!/bin/sh

# Lock after 10 minutes of inactivity
xset s 600 600

# Lock on inactivity and before suspend
xss-lock --transfer-sleep-lock -- i3lock --nofork &

# Keyboard shortcuts
sxhkd &

# Start window manager
exec bspwm
