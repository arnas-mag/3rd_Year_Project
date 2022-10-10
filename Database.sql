use group_project;
/*Bring into being account*/
create table biba
(
	/*Unique id*/
	uid integer auto_increment primary key,
    /*Potential to verify?*/
    email varchar(50),
    password varchar(40)
    
);
