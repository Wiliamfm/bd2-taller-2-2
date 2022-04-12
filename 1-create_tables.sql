-- Database: taller_1

create schema public;

create table city(
	id serial primary key,
	city varchar(100) unique not null
);

create table user_type(
	id serial primary key,
	type varchar(20) unique not null
);

create table document_type(
	id serial primary key,
	type varchar(3) unique not null
);

create table app_user(
	document varchar(20) primary key,
	full_name varchar(100),
	email varchar(100) unique not null,
	password varchar(100) not null,
	address varchar(100),
	user_type serial references user_type (id) on delete cascade,
	document_type serial references document_type (id) on delete set null,
	city serial references city (id) on delete set null
);

create table phone(
	id serial primary key,
	phone_numer varchar(10) unique not null,
	owner varchar(20) references app_user(document) on delete cascade
);

create table brand(
	id serial primary key,
	name varchar(100) unique not null
);

create table category(
	id serial primary key,
	category varchar(20) not null unique
);

create table product(
	id serial primary key,
	title varchar(100) not null,
	photos bytea array,
	price numeric(13,2) not null,
	brand serial references brand (id) on delete cascade,
	category integer references category (id) on delete set null,
	supplier varchar(20) references app_user (document) on delete cascade
);

create table variant(
	id serial primary key,
	stock integer not null,
	description text not null,
	product serial references product (id) on delete cascade
);

create table cart_condition(	
	id serial primary key,
	condition varchar(10) unique not null
);

create table shopping_cart(
	id serial primary key,
	amount integer not null,
	cart_condition serial references cart_condition (id) on delete set null,
	app_user varchar(20) references app_user(document) on delete set null
);

create table shopping_product(
	id serial primary key,
	variant integer references variant (id) on delete set null,
	shopping_cart serial references shopping_cart (id) on delete set null
);

create table shipping_type(
	id serial primary key,
	shipping_type varchar(20) unique not null
);

create table pay_method(
	id serial primary key,
	pay_method varchar(20) unique not null
);

create table bill_state(
	id serial primary key,
	bill_condition varchar(40) unique not null
);

create table bill(
	id serial primary key,
	total numeric (20, 4) not null,
	bill_date timestamptz not null,
	shopping_cart integer references shopping_cart (id) on delete set null,
	shipping_type serial references shipping_type (id) on delete set null,
	pay_method serial references pay_method (id) on delete set null,
	bill_state serial references bill_state (id) on delete set null
);

alter table bill
	add constraint unique_shopping_cart
	unique (shopping_cart);
	
create table product_calification(
	id serial primary key,
	calification integer not null,
	product integer references product (id) on delete cascade,
	bill integer references bill (id) on delete cascade
);