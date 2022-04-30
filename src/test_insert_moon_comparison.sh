#!/bin/bash
for i in {1..100}
do
        echo "Iteration: $i"
        time python3 main.py --q "insert into exam (id, id_doctor, id_lab_worker, id_patient, date_exam, glucose, insulin, leptin, adiponecti, resistin, mcp_1) values (101, 1, 2, 86, '2020/01/08', 70, 2.7, 8.8, 9.7, 7.9, 417.1);" --c "insert" --r "101,2,86,'2020/01/08',70,2.7,8.8,9.7,7.9,417.1"
        sleep 5
        python3 main.py --q "delete from exam where id=101" --c "delete" --d 101
        sleep 5

done 2>&1 | tee insert_moon_comparison_test.log