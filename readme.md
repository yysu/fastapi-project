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
CREATE TABLE public.posts
(
    title character varying NOT NULL,
    content character varying NOT NULL,
    id serial,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.products
    OWNER to postgres;
```