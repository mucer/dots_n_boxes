#!/bin/bash
target_dir=/tmp/py
rsync -avm --include='lib' --include='*.py' --exclude='*' ./ $target_dir