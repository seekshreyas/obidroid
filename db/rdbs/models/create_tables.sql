CREATE TABLE app
(
  appid character varying(500) NOT NULL,
  category character varying(100),
  company character varying(100),
  content_rating character varying(100),
  description character varying(10000),
  install character varying(100),
  name character varying(250),
  screen_count integer,
  size character varying(100),
  total_reviewers integer,
  version character varying(100),
  CONSTRAINT app_pkey PRIMARY KEY (appid)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE app
  OWNER TO postgres;


CREATE TABLE review
(
  reviewid serial NOT NULL,
  playappid character varying(500) NOT NULL,
  title character varying(500),
  review character varying(10000) NOT NULL,
  CONSTRAINT review_pkey PRIMARY KEY (reviewid)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE review
  OWNER TO postgres;
