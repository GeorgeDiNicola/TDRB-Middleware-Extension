#!/bin/bash
for i in {1..40}
do
        echo "Iteration: $i"
        time python3 main.py --q "select * from student" --c "query"
        sleep 5
done 2>&1 | tee middleware_query_test.log