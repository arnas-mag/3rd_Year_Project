use group_project;
/*Forget password*/



/*Bring into being account*/
create table create_account
(
	/*Unique id*/
	unique_id integer auto_increment primary key,
    first_name varchar(20),
    last_name varchar(20),
    /*Potential to verify?*/
    email varchar(50),
    password varchar(40)
);
/*Log into account*/
create table login
(
    login_id auto_increment primary key,
	unique_id integer foreign key,
    email varchar(50),
    password varchar(40)
);
/*Dashboard*/
create table dashboard
(
    dashboard_id integer auto_increment primary key,
    login_id integer foreign key,
	power_use varchar(20),
    water_use varchar(20),
    temperature varchar(20)
);
/*Prediction*/
create table prediction
(
	prediction_id integer auto_increment primary key,
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
    graph_page_id integer auto_increment primary key,
    dashboard_id integer foreign key,
	to_date date,
    from_date date
);

