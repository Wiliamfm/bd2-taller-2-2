insert into city
values (1, 'bogota');

insert into city
values (2, 'cali');

insert into city
values (3, 'medellin');

insert into user_type
values (1, 'admin');

insert into user_type
values (2, 'user');

insert into user_type
values (3, 'vendor');

insert into document_type
values (1, 'cc');

insert into document_type
values (2, 'ce');

insert into document_type
values (3, 'nit');

insert into brand
values (1, 'adidas');

insert into brand
values (2, 'nike');

insert into brand
values (3, 'rebook');

insert into category
values (1, 'clothes');

insert into category
values (2, 'tecnology');

insert into category
values (3, 'vehicules');

insert into cart_condition
values (1, 'abandoned');

insert into cart_condition
values (2, 'sold');

insert into shipping_type
values(1, 'standar');

insert into shipping_type
values(2, 'express');

insert into pay_method
values (1, 'credit card');

insert into pay_method
values (2, 'bank transfer');

insert into pay_method
values (3, 'upon delivery');

insert into bill_state
values (1, 'delivered');

insert into bill_state
values (2, 'preparation');

insert into bill_state
values (3, 'sent');

insert into bill_state
values (4, 'canceled');

insert into app_user
values ('0123456789', 'admin', 'asdf@asdf.asdf', '1234', 'calle 185 a # 11 b - 07', 1, 1, 1);

insert into app_user
values ('1234567890', 'example', 'asdf2@asdf.asdf', '1234', 'calle 185 a # 11 b - 07', 2, 1, 1);

insert into app_user
values ('2345678901', 'vendor example', 'asdf3@asdf.asdf', '1234', 'calle 185 a # 11 b - 07', 3, 1, 1);

insert into phone
values (1, '1234567890', '0123456789');

insert into phone
values (2, '4567891230', '0123456789');

insert into phone
values (3, '9876543210', '2345678901');

insert into auditory.event_type
values (1, 'insert');

insert into auditory.event_type
values (2, 'update');

insert into auditory.event_type
values (3, 'delete');

insert into product
values (1, 'example', null, 10000, 1, 1, '2345678901');

insert into product
values (2, 'example 2', null, 11000, 1, 1, '2345678901');

insert into variant
values (1, 1, 'variant example', 1);

insert into variant
values (2, 2, 'variant example 2', 1);

insert into variant
values (3, 5, 'variant example 3', 1);

insert into variant
values (4, 2, 'variant example 4', 1);

insert into variant
values (5, 2, 'variant example 5', 1);

insert into variant
values (6, 2, 'variant example 1', 2);