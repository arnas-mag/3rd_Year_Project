use group_project;
/*Bring into being account*/
create table biba
(
	/*Unique id*/
	uid integer auto_increment primary key,
    first_name varchar(20),
    last_name varchar(20),
    /*Potential to verify?*/
    email varchar(50),
    password varchar(40),
    redo_password varchar(40)
);
/*Log into account*/
create table lia
(
	uid integer auto_increment,
    email varchar(50),
    password varchar(40)
);
/*Dashboard*/
create table dashboard
(
	power_use varchar(20),
    water_use varchar(20),
    temperature varchar(20)
);
/*Prediction*/
create table prediction
(
	/*Date entered*/
    date_entered date,
    power_use varchar(20),
    water_use varchar(20),
    temperature varchar(20)
);
/*Graph Page*/
/*Prepared statement for the actual graph?*/
create table graph_page
(
	to_date date,
    from_date date
);

