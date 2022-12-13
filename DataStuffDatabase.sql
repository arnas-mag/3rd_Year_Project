create database project;

use project;

create table temperture(
temperture_id varchar(20) primary key not null,
temperture_celcius double,
timestamp datetime
);
/*Water and Power tables have their foreign keys from temperture*/
create table water(
water_id varchar(20) primary key not null,
water_usage double,
timestamp datetime,
constraint water_fk foreign key (timestamp) references temperture (timestamp)
);

create table power(
power_id varchar(20) primary key not null,
power_usage double,
timestamp datetime,
constraint power_fk foreign key (timestamp) references temperture (timestamp)
);
