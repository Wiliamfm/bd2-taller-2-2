create or replace function trigger_verify_order()
	returns trigger
	language plpgsql
	as
$$
	begin
	
		perform *
			from shopping_cart sp
			where sp.id = new.shopping_cart;
			
		if found then
	
			perform *
				from bill b
				where b.shopping_cart = new.shopping_cart;
				
			if found then
				raise exception 'The cart already has a bill';
			else
				return new;
			end if;
		
		else		
			raise exception 'the cart does not exists';			
		end if;
	end;
$$;

create or replace trigger verify_order
	before insert
	on bill
	for each row
	execute procedure trigger_verify_order();
	
create or replace function get_product_calification(product_id integer)
	returns integer
	language plpgsql 
	as 
$$
	declare 
		calification integer;
	begin 
		
		select sum(c.calification)
			into calification 
			from product_calification c
			where c.product = product_id;
		
		return calification;
	end;
$$;

drop function  get_product_calification ;