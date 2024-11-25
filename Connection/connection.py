q_table = """create table employee(e_id int auto_increment primary key,
e_name varchar(200),age int,doj datetime,createon datetime,active int
,foreign key(active) references active(id))"""
q_active = """create table active(id int auto_increment primary key,type varchar(100))"""
q_insert = """insert into active(type) values('active'),('deactive')"""