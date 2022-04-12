-- create tables for auditory

create schema auditory;

create table auditory.event_type(
	id serial primary key,
	event varchar(10) unique not null
);

create table auditory.product_audit (
	id serial primary key,
	title varchar(100) not null,
	category varchar(20) not null,
	photos bytea array, 
	rate integer,
	brand varchar(100) not null,
	vendor_name varchar(100) not null,
	datetime timestamptz,
	event_type integer references auditory.event_type(id) on delete set null
);

create table auditory.variant_audit(
	id serial primary key,
	price numeric(13,2) not null,
	stock integer not null,
	characteristics text not null,
	product varchar(100) not null,
	datetime timestamptz,
	event_type integer references auditory.event_type(id) on delete set null
)

--Create functions for auditory

create or replace function auditory.trigger_product_audit()
	returns trigger
	language plpgsql
	as
$$
	declare
		product_category category.category%type;
		product_brand brand.name%type;
		product_supplier app_user.full_name%type;
		product_calification integer;
	begin
	
	if tg_op = 'INSERT' OR TG_OP = 'UPDATE' THEN	
		select u.full_name 
			into product_supplier
			from app_user u
			where u.document = new.supplier;

		select c.category
			into product_category
			from category c
			where c.id = new.category;

		select b.name
			into product_brand
			from brand b
			where b.id = new.brand;
		
		select *
			into product_calification
			from public.get_product_calification(new.id);
		
		
	elseif TG_OP = 'DELTE' then
		select u.full_name 
			into product_supplier
			from app_user u
			where u.document = old.supplier;

		select c.category
			into product_category
			from category c
			where c.id = old.category;

		select b.name
			into product_brand
			from brand b
			where b.id = old.brand;
		
		select *
			into product_calification
			from public.get_product_calification(old.id);
	end if;
	
	if tg_op = 'INSERT' then	
		insert into auditory.product_audit 
			(title, category, photos, rate, brand, vendor_name, datetime, event_type)
		values 
			(new.title, product_category, new.photos, product_calification, product_brand, product_supplier, now(), 1);
		return new;
	end if;
	
	if tg_op = 'UPDATE' then	
		insert into auditory.product_audit 
			(title, category, photos, rate, brand, vendor_name, datetime, event_type)
		values 
			(new.title, product_category, new.photos, product_calification, product_brand, product_supplier, now(), 2);
		return new;
	end if;
	
	if tg_op = 'DELETE' then	
		insert into auditory.product_audit 
			(title, category, photos, rate, brand, vendor_name, datetime, event_type)
		values 
			(old.title, product_category, old.photos, product_calification, product_brand, product_supplier, now(), 3);
		return old;
	end if;	
	
	end;
$$;

create or replace trigger product_audit
	after update or insert or delete
	on product
	for each row
	execute procedure auditory.trigger_product_audit();
	
create or replace function auditory.trigger_variant_audit()
	returns trigger
	language plpgsql
	as
$$
	declare
		variant_product product.title%type;
	begin
	
	if tg_op = 'INSERT' OR TG_OP = 'UPDATE' THEN
	
		select p.title
			into variant_product
			from product p
			where p.id = new.product;
			
	elseif TG_OP = 'DELTE' then
	
		select p.title
			into variant_product
			from product p
			where p.id = old.product;
			
	end if;
	
	if tg_op = 'INSERT' then	
		insert into auditory.variant_audit 
			(price, stock, characteristics, product, datetime, event_type)
		values 
			(new.price, new.stock, new.charact, variant_product, now(), 1);
		return new;
	end if;
	
	if tg_op = 'UPDATE' then	
		insert into auditory.variant_audit 
			(price, stock, characteristics, product, datetime, event_type)
		values 
			(new.price, new.stock, new.charact, variant_product, now(), 2);
		return new;
	end if;
	
	if tg_op = 'DELETE' then		
		insert into auditory.variant_audit 
			(price, stock, characteristics, product, datetime, event_type)
		values 
			(old.price, old.stock, old.charact, variant_product, now(), 3);
		return old;
	end if;	
	
	end;
$$;

create or replace trigger variant_audit
	after update or insert or delete
	on variant
	for each row
	execute procedure auditory.trigger_variant_audit();