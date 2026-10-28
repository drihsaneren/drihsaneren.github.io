#!/bin/bash
# Yeni oturumda dizin düzeni (betiklerdeki sabit yollar bunu bekler):
#   /home/claude/main                 -> main dalı (yayındaki site)
#   /home/claude/drihsaneren.github.io -> kaynak dalı (araçlar, worktree)
set -e; cd /home/claude
URL=https://github.com/drihsaneren/drihsaneren.github.io
if [ -e drihsaneren.github.io/.git ] && [ ! -d main ]; then
  b=$(git -C drihsaneren.github.io rev-parse --abbrev-ref HEAD)
  [ "$b" != "kaynak" ] && mv drihsaneren.github.io main
fi
[ -d main ] || git clone -q $URL main
git -C main fetch -q origin main kaynak
git -C main checkout -q main && git -C main pull -q --ff-only origin main
[ -d drihsaneren.github.io ] || git -C main worktree add -q /home/claude/drihsaneren.github.io kaynak
git -C drihsaneren.github.io pull -q --ff-only origin kaynak
mkdir -p drihsaneren.github.io/up40 drihsaneren.github.io/shots6
echo "kurulum tamam: main=$(git -C main log --oneline -1) | kaynak=$(git -C drihsaneren.github.io log --oneline -1)"
