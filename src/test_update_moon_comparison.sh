#!/bin/bash
for i in {1..100}
do
        echo "Iteration: $i"
        time python3 main.py --q "update exam SET glucose=87 WHERE id=${i};" --c "update" --u "${i},87"
        sleep 5
done 2>&1 | tee update_moon_comparison_test.log