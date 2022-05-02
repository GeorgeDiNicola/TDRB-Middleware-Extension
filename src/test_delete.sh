#!/bin/bash
for i in {40..1}
do
        echo "Iteration: $i"
        time python3 main.py --q "delete from student where id=${i}" --c "delete" --d ${i}
        sleep 5
done 2>&1 | tee middleware_delete_test.log