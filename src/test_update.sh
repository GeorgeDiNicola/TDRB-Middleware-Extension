#!/bin/bash
for i in {1..40}
do
        echo "Iteration: $i"
        time python3 main.py --q "update student set name='updated' where id=${i}" --c "update" --u "${i},updated"
        sleep 5
done 2>&1 | tee middleware_update_test.log