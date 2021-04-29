-- update the items table
-- with the order value
CREATE TRIGGER buy
       BEFORE INSERT ON orders
FOR EACH ROW
    UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
