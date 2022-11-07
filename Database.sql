use group_project;
/*Forget password*/



/*Bring into being account*/
create table biba
(
	/*Unique id*/
	uid integer auto_increment primary key,
    first_name varchar(20),
    last_name varchar(20),
    /*Potential to verify?*/
    email varchar(50),
    password varchar(40)
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
    login_id integer foreign key,
	power_use varchar(20),
    water_use varchar(20),
    temperature varchar(20)
);
/*Prediction*/
create table prediction
(
	/*Date entered*/
    dashboard_id integer foreign key,
    date_entered date,
    power_use varchar(20),
    water_use varchar(20),
    temperature varchar(20)
);
/*Graph Page*/
/*Prepared statement for the actual graph?*/
create table graph_page
(
    dashboard_id foreign key,
	to_date date,
    from_date date
);

