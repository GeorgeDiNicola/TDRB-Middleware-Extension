#!/bin/bash
for i in {1..100}
do
        echo "Iteration: $i"
        time python3 main.py --q "select * from exam" --c "query"
        sleep 5
done 2>&1 | tee query_moon_comparison_test.log