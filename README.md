 #Parking-System
##python project for parking vehicles in mall


need mysql installed in system  and a mysql-python connector;
tables to be generated in them
![] photo/Screenshot%20(12).png
+-------------------+
| Tables_in_parking |
+-------------------+
| owner_detail      |
| park              |
| revenue           |
+-------------------+


 desc owner_detail;
+---------------------+-------------+------+-----+---------+-------+
| Field               | Type        | Null | Key | Default | Extra |
+---------------------+-------------+------+-----+---------+-------+
| mallname            | varchar(20) | NO   | PRI | NULL    |       |
| CAPACITYTWOWHEELER  | int         | NO   |     | NULL    |       |
| CAPACITYFOURWHEELER | int         | NO   |     | NULL    |       |
+---------------------+-------------+------+-----+---------+-------!

desc park;
+----------------+-------------+------+-----+---------+-------+
| Field          | Type        | Null | Key | Default | Extra |
+----------------+-------------+------+-----+---------+-------+
| uuid           | varchar(40) | NO   |     | NULL    |       |
| vehicle_number | varchar(20) | NO   |     | NULL    |       |
| vehicle_type   | int         | NO   |     | NULL    |       |
| mallname       | varchar(20) | NO   | MUL | NULL    |       |
| entry_time     | datetime    | NO   |     | NULL    |       |
+----------------+-------------+------+-----+---------+-------+

 desc revenue;
+----------------+-------------+------+-----+---------+-------+
| Field          | Type        | Null | Key | Default | Extra |
+----------------+-------------+------+-----+---------+-------+
| U_id           | varchar(40) | NO   | PRI | NULL    |       |
| Time           | time        | YES  |     | NULL    |       |
| vehicle_number | varchar(20) | YES  |     | NULL    |       |
| cost           | int         | YES  |     | NULL    |       |
| MALLNAME       | varchar(20) | YES  |     | NULL    |       |
| exit_time      | datetime    | YES  |     | NULL    |       |
| month          | int         | YES  |     | NULL    |       |
| date           | int         | YES  |     | NULL    |       |
| year           | int         | YES  |     | NULL    |       |
+----------------+-------------+------+-----+---------+-------+
