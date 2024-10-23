#!/usr/bin/env bash

host=$1
port=$2
start=$3
end=$4
step=$5

if [ -z "$host" ] || [ -z "$port" ] || [ -z "$start" ] || [ -z "$end" ] || [ -z "$step" ]; then
    echo "Usage: $0 <host> <port> <start> <end> <step>"
    exit 1
fi

for i in $(seq "$start" "$step" "$end"); do
    echo "Fuzzing with $i bytes"
    python -c "print(b'A' * $i)" | nc -w 1 "$host" "$port"
done
