# FastAPI

# Start server 
$ uvicorn main:app --reload


# PG
```
CREATE DATABASE fastapi
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;
```

```
CREATE TABLE public.products
(
    name character varying NOT NULL,
    price integer NOT NULL,
    id serial,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.products
    OWNER to postgres;
```