#!/usr/bin/bash

# cd "$PWD" || exit 1

# read first argument as binary

if [ -z "$1" ]; then
    echo "Usage: $0 <binary>"
    exit 1
fi

binary="$1"

echo "$binary"

str="$(printf "A%.0s" {1..32})"

# run binary with str as argument in bash


for i in $(seq 1 32); do
    echo "Fuzzing with ${#str} A's"
    echo "$str" | "$binary"
    str+="A"
    printf "\n"
done

