#!/bin/bash
for i in {101..140}
do
        echo "Iteration: $i"
        time python3 main.py --q "insert into student (id, name, sex, age) values (${i}, 'test${i}', 'Male', ${i});" --c "insert" --r "${i},test${i},Male,${i}"
        sleep 10
done 2>&1 | tee middleware_insert_test.log