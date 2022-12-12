DROP DATABASE IF EXISTS group_project;
create database group_project;
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
    login_id integer primary key auto_increment,
	unique_id integer,
    email varchar(50),
    password varchar(40),
    constraint login_fk foreign key (unique_id) references create_account (unique_id)
);
/*Dashboard*/
create table dashboard
(
    dashboard_id integer auto_increment primary key,
    login_id integer,
	power_use varchar(20),
    water_use varchar(20),
    temperature varchar(20),
    constraint dashboard_fk foreign key (login_id) references login (login_id)
);
/*Prediction*/
create table prediction
(
	prediction_id integer auto_increment primary key,
    dashboard_id integer,
    date_entered date,
    power_use varchar(20),
    water_use varchar(20),
    temperature varchar(20),
    constraint prediction_fk foreign key (dashboard_id) references dashboard (dashboard_id)
);
/*Graph Page*/
/*Prepared statement for the actual graph?*/
create table graph_page
(
    graph_page_id integer auto_increment primary key,
    dashboard_id integer,
	to_date date,
    from_date date,
    constraint graph_page_fk foreign key (dashboard_id) references prediction (dashboard_id)
);

DROP PROCEDURE IF EXISTS newAccount;
DELIMITER //
CREATE PROCEDURE newAccount
(
	IN fname varchar(20),
    IN lname varchar(20),
    IN eml varchar(50),
    IN pwd varchar(40)
)
BEGIN
    INSERT INTO create_account (first_name, last_name, email, password) VALUES (fname, lname, eml, pwd);
END//
DELIMITER ;

/*Testing 'newAccount' Procedure by checking entries in 'create_account' table, calling the procedure and inputting details, and then checking entries in 'create_account' table again.
	SELECT * FROM create_account;
	CALL newAccount('John','Doe','jd@gmail.com','jdg');
	SELECT * FROM create_account;
*/