--
-- PostgreSQL database dump
--

-- Dumped from database version 10.6 (Ubuntu 10.6-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.6 (Ubuntu 10.6-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO django;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO django;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO django;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO django;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO django;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO django;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO django;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO django;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO django;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO django;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO django;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO django;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO django;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO django;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO django;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO django;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO django;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO django;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO django;

--
-- Name: others_aboutus; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.others_aboutus (
    id integer NOT NULL,
    text_about_us_page text NOT NULL,
    text_about_us_page_2 text,
    phone character varying(50),
    address character varying(200),
    time_work character varying(200),
    email character varying(254),
    smal_company_name character varying(200),
    discription_name character varying(100),
    notes text,
    full_company_name character varying(200),
    fio_entrepreneur character varying(200),
    ip_registration_address character varying(200),
    inn_kpp character varying(200),
    bin character varying(200),
    okved character varying(200),
    okpo character varying(200),
    requisites text,
    self_phone character varying(200),
    self_email character varying(200)
);


ALTER TABLE public.others_aboutus OWNER TO django;

--
-- Name: others_aboutus_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.others_aboutus_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.others_aboutus_id_seq OWNER TO django;

--
-- Name: others_aboutus_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.others_aboutus_id_seq OWNED BY public.others_aboutus.id;


--
-- Name: others_collback; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.others_collback (
    id integer NOT NULL,
    title character varying(200),
    description character varying(500),
    description_short character varying(200),
    btn_name character varying(100),
    image character varying(100),
    avalible boolean NOT NULL
);


ALTER TABLE public.others_collback OWNER TO django;

--
-- Name: others_collback_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.others_collback_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.others_collback_id_seq OWNER TO django;

--
-- Name: others_collback_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.others_collback_id_seq OWNED BY public.others_collback.id;


--
-- Name: others_collbackclient; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.others_collbackclient (
    id integer NOT NULL,
    name_client character varying(200) NOT NULL,
    phone_client character varying(100) NOT NULL,
    coll_time character varying(300) NOT NULL,
    description_client text,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL
);


ALTER TABLE public.others_collbackclient OWNER TO django;

--
-- Name: others_collbackclient_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.others_collbackclient_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.others_collbackclient_id_seq OWNER TO django;

--
-- Name: others_collbackclient_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.others_collbackclient_id_seq OWNED BY public.others_collbackclient.id;


--
-- Name: others_documentation; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.others_documentation (
    id integer NOT NULL,
    title character varying(200) NOT NULL,
    description text,
    file character varying(100) NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL
);


ALTER TABLE public.others_documentation OWNER TO django;

--
-- Name: others_documentation_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.others_documentation_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.others_documentation_id_seq OWNER TO django;

--
-- Name: others_documentation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.others_documentation_id_seq OWNED BY public.others_documentation.id;


--
-- Name: others_faq; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.others_faq (
    id integer NOT NULL,
    question character varying(400) NOT NULL,
    answer text NOT NULL
);


ALTER TABLE public.others_faq OWNER TO django;

--
-- Name: others_faq_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.others_faq_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.others_faq_id_seq OWNER TO django;

--
-- Name: others_faq_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.others_faq_id_seq OWNED BY public.others_faq.id;


--
-- Name: others_homepagetext; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.others_homepagetext (
    id integer NOT NULL,
    text_home_page text NOT NULL,
    text_home_page_2 text
);


ALTER TABLE public.others_homepagetext OWNER TO django;

--
-- Name: others_homepagetext_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.others_homepagetext_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.others_homepagetext_id_seq OWNER TO django;

--
-- Name: others_homepagetext_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.others_homepagetext_id_seq OWNED BY public.others_homepagetext.id;


--
-- Name: others_maincomments; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.others_maincomments (
    id integer NOT NULL,
    name_person character varying(200) NOT NULL,
    email character varying(200) NOT NULL,
    phone character varying(100),
    job_satisfaction integer NOT NULL,
    kind_job character varying(200),
    comment_body text,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    moderation boolean NOT NULL
);


ALTER TABLE public.others_maincomments OWNER TO django;

--
-- Name: others_maincomments_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.others_maincomments_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.others_maincomments_id_seq OWNER TO django;

--
-- Name: others_maincomments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.others_maincomments_id_seq OWNED BY public.others_maincomments.id;


--
-- Name: others_mainslider; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.others_mainslider (
    id integer NOT NULL,
    title character varying(50),
    description character varying(200),
    image character varying(100) NOT NULL,
    button_name character varying(50),
    serial_number integer NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    CONSTRAINT others_mainslider_serial_number_check CHECK ((serial_number >= 0))
);


ALTER TABLE public.others_mainslider OWNER TO django;

--
-- Name: others_mainslider_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.others_mainslider_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.others_mainslider_id_seq OWNER TO django;

--
-- Name: others_mainslider_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.others_mainslider_id_seq OWNED BY public.others_mainslider.id;


--
-- Name: others_order; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.others_order (
    id integer NOT NULL,
    name_client character varying(200) NOT NULL,
    phone_client character varying(100) NOT NULL,
    email_client character varying(254) NOT NULL,
    subject_work character varying(200) NOT NULL,
    description_client text,
    file character varying(100),
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL
);


ALTER TABLE public.others_order OWNER TO django;

--
-- Name: others_order_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.others_order_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.others_order_id_seq OWNER TO django;

--
-- Name: others_order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.others_order_id_seq OWNED BY public.others_order.id;


--
-- Name: others_partners; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.others_partners (
    id integer NOT NULL,
    name character varying(200) NOT NULL,
    image character varying(100) NOT NULL,
    link character varying(200)
);


ALTER TABLE public.others_partners OWNER TO django;

--
-- Name: others_partners_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.others_partners_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.others_partners_id_seq OWNER TO django;

--
-- Name: others_partners_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.others_partners_id_seq OWNED BY public.others_partners.id;


--
-- Name: portfolio_images; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.portfolio_images (
    id integer NOT NULL,
    image character varying(100) NOT NULL,
    name character varying(200) NOT NULL,
    description character varying(800),
    slug character varying(50),
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL
);


ALTER TABLE public.portfolio_images OWNER TO django;

--
-- Name: portfolio_images_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.portfolio_images_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.portfolio_images_id_seq OWNER TO django;

--
-- Name: portfolio_images_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.portfolio_images_id_seq OWNED BY public.portfolio_images.id;


--
-- Name: portfolio_portfolio; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.portfolio_portfolio (
    id integer NOT NULL,
    name character varying(200) NOT NULL,
    slug character varying(50) NOT NULL,
    description text,
    main_image character varying(100) NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    availability boolean NOT NULL,
    topic_id integer NOT NULL
);


ALTER TABLE public.portfolio_portfolio OWNER TO django;

--
-- Name: portfolio_portfolio_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.portfolio_portfolio_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.portfolio_portfolio_id_seq OWNER TO django;

--
-- Name: portfolio_portfolio_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.portfolio_portfolio_id_seq OWNED BY public.portfolio_portfolio.id;


--
-- Name: portfolio_portfolio_images; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.portfolio_portfolio_images (
    id integer NOT NULL,
    portfolio_id integer NOT NULL,
    images_id integer NOT NULL
);


ALTER TABLE public.portfolio_portfolio_images OWNER TO django;

--
-- Name: portfolio_portfolio_images_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.portfolio_portfolio_images_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.portfolio_portfolio_images_id_seq OWNER TO django;

--
-- Name: portfolio_portfolio_images_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.portfolio_portfolio_images_id_seq OWNED BY public.portfolio_portfolio_images.id;


--
-- Name: portfolio_portfoliocomments; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.portfolio_portfoliocomments (
    id integer NOT NULL,
    parent_object integer,
    name_person character varying(200) NOT NULL,
    email character varying(200) NOT NULL,
    comment_body text NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    moderation boolean NOT NULL
);


ALTER TABLE public.portfolio_portfoliocomments OWNER TO django;

--
-- Name: portfolio_portfoliocomments_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.portfolio_portfoliocomments_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.portfolio_portfoliocomments_id_seq OWNER TO django;

--
-- Name: portfolio_portfoliocomments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.portfolio_portfoliocomments_id_seq OWNED BY public.portfolio_portfoliocomments.id;


--
-- Name: portfolio_topic; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.portfolio_topic (
    id integer NOT NULL,
    name character varying(200) NOT NULL,
    slug character varying(50) NOT NULL,
    descriprion text
);


ALTER TABLE public.portfolio_topic OWNER TO django;

--
-- Name: portfolio_topic_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.portfolio_topic_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.portfolio_topic_id_seq OWNER TO django;

--
-- Name: portfolio_topic_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.portfolio_topic_id_seq OWNED BY public.portfolio_topic.id;


--
-- Name: service_images; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.service_images (
    id integer NOT NULL,
    image character varying(100) NOT NULL,
    name character varying(200) NOT NULL,
    description character varying(800),
    slug character varying(50),
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL
);


ALTER TABLE public.service_images OWNER TO django;

--
-- Name: service_images_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.service_images_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.service_images_id_seq OWNER TO django;

--
-- Name: service_images_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.service_images_id_seq OWNED BY public.service_images.id;


--
-- Name: service_kindworks; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.service_kindworks (
    id integer NOT NULL,
    name character varying(200) NOT NULL,
    slug character varying(50) NOT NULL,
    intro character varying(200),
    main_image character varying(100),
    desctiption text,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    gallery_availability boolean NOT NULL
);


ALTER TABLE public.service_kindworks OWNER TO django;

--
-- Name: service_kindworks_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.service_kindworks_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.service_kindworks_id_seq OWNER TO django;

--
-- Name: service_kindworks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.service_kindworks_id_seq OWNED BY public.service_kindworks.id;


--
-- Name: service_kindworks_image; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.service_kindworks_image (
    id integer NOT NULL,
    kindworks_id integer NOT NULL,
    images_id integer NOT NULL
);


ALTER TABLE public.service_kindworks_image OWNER TO django;

--
-- Name: service_kindworks_image_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.service_kindworks_image_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.service_kindworks_image_id_seq OWNER TO django;

--
-- Name: service_kindworks_image_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.service_kindworks_image_id_seq OWNED BY public.service_kindworks_image.id;


--
-- Name: service_kindworkscomments; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.service_kindworkscomments (
    id integer NOT NULL,
    parent_object integer,
    name_person character varying(200) NOT NULL,
    email character varying(200) NOT NULL,
    comment_body text NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    moderation boolean NOT NULL
);


ALTER TABLE public.service_kindworkscomments OWNER TO django;

--
-- Name: service_kindworkscomments_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.service_kindworkscomments_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.service_kindworkscomments_id_seq OWNER TO django;

--
-- Name: service_kindworkscomments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.service_kindworkscomments_id_seq OWNED BY public.service_kindworkscomments.id;


--
-- Name: service_service; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.service_service (
    id integer NOT NULL,
    name character varying(200) NOT NULL,
    slug character varying(50) NOT NULL,
    main_image character varying(100),
    desctiptions text,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    price character varying(50),
    gallery_availability boolean NOT NULL,
    kindworks_id integer NOT NULL,
    unit_id integer
);


ALTER TABLE public.service_service OWNER TO django;

--
-- Name: service_service_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.service_service_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.service_service_id_seq OWNER TO django;

--
-- Name: service_service_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.service_service_id_seq OWNED BY public.service_service.id;


--
-- Name: service_service_image; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.service_service_image (
    id integer NOT NULL,
    service_id integer NOT NULL,
    images_id integer NOT NULL
);


ALTER TABLE public.service_service_image OWNER TO django;

--
-- Name: service_service_image_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.service_service_image_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.service_service_image_id_seq OWNER TO django;

--
-- Name: service_service_image_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.service_service_image_id_seq OWNED BY public.service_service_image.id;


--
-- Name: service_servicecomments; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.service_servicecomments (
    id integer NOT NULL,
    parent_object integer,
    name_person character varying(200) NOT NULL,
    email character varying(200) NOT NULL,
    comment_body text NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    moderation boolean NOT NULL
);


ALTER TABLE public.service_servicecomments OWNER TO django;

--
-- Name: service_servicecomments_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.service_servicecomments_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.service_servicecomments_id_seq OWNER TO django;

--
-- Name: service_servicecomments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.service_servicecomments_id_seq OWNED BY public.service_servicecomments.id;


--
-- Name: service_unit; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.service_unit (
    id integer NOT NULL,
    name character varying(100) NOT NULL
);


ALTER TABLE public.service_unit OWNER TO django;

--
-- Name: service_unit_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.service_unit_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.service_unit_id_seq OWNER TO django;

--
-- Name: service_unit_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.service_unit_id_seq OWNED BY public.service_unit.id;


--
-- Name: site_some_settings_sitesettings; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.site_some_settings_sitesettings (
    id integer NOT NULL,
    site_name character varying(100),
    confirm_main_comments boolean NOT NULL,
    confirm_portfolio_comments boolean NOT NULL,
    confirm_services_comments boolean NOT NULL,
    avalible_load_files_order boolean NOT NULL,
    social_link_vk character varying(200),
    social_link_youtube character varying(200),
    social_link_linkedin character varying(200),
    social_link_twitter character varying(200),
    social_link_facebook character varying(200),
    social_link_other_1 character varying(200),
    social_link_other_2 character varying(200)
);


ALTER TABLE public.site_some_settings_sitesettings OWNER TO django;

--
-- Name: site_some_settings_sitesettings_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.site_some_settings_sitesettings_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.site_some_settings_sitesettings_id_seq OWNER TO django;

--
-- Name: site_some_settings_sitesettings_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.site_some_settings_sitesettings_id_seq OWNED BY public.site_some_settings_sitesettings.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: others_aboutus id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.others_aboutus ALTER COLUMN id SET DEFAULT nextval('public.others_aboutus_id_seq'::regclass);


--
-- Name: others_collback id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.others_collback ALTER COLUMN id SET DEFAULT nextval('public.others_collback_id_seq'::regclass);


--
-- Name: others_collbackclient id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.others_collbackclient ALTER COLUMN id SET DEFAULT nextval('public.others_collbackclient_id_seq'::regclass);


--
-- Name: others_documentation id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.others_documentation ALTER COLUMN id SET DEFAULT nextval('public.others_documentation_id_seq'::regclass);


--
-- Name: others_faq id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.others_faq ALTER COLUMN id SET DEFAULT nextval('public.others_faq_id_seq'::regclass);


--
-- Name: others_homepagetext id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.others_homepagetext ALTER COLUMN id SET DEFAULT nextval('public.others_homepagetext_id_seq'::regclass);


--
-- Name: others_maincomments id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.others_maincomments ALTER COLUMN id SET DEFAULT nextval('public.others_maincomments_id_seq'::regclass);


--
-- Name: others_mainslider id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.others_mainslider ALTER COLUMN id SET DEFAULT nextval('public.others_mainslider_id_seq'::regclass);


--
-- Name: others_order id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.others_order ALTER COLUMN id SET DEFAULT nextval('public.others_order_id_seq'::regclass);


--
-- Name: others_partners id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.others_partners ALTER COLUMN id SET DEFAULT nextval('public.others_partners_id_seq'::regclass);


--
-- Name: portfolio_images id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.portfolio_images ALTER COLUMN id SET DEFAULT nextval('public.portfolio_images_id_seq'::regclass);


--
-- Name: portfolio_portfolio id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.portfolio_portfolio ALTER COLUMN id SET DEFAULT nextval('public.portfolio_portfolio_id_seq'::regclass);


--
-- Name: portfolio_portfolio_images id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.portfolio_portfolio_images ALTER COLUMN id SET DEFAULT nextval('public.portfolio_portfolio_images_id_seq'::regclass);


--
-- Name: portfolio_portfoliocomments id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.portfolio_portfoliocomments ALTER COLUMN id SET DEFAULT nextval('public.portfolio_portfoliocomments_id_seq'::regclass);


--
-- Name: portfolio_topic id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.portfolio_topic ALTER COLUMN id SET DEFAULT nextval('public.portfolio_topic_id_seq'::regclass);


--
-- Name: service_images id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.service_images ALTER COLUMN id SET DEFAULT nextval('public.service_images_id_seq'::regclass);


--
-- Name: service_kindworks id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.service_kindworks ALTER COLUMN id SET DEFAULT nextval('public.service_kindworks_id_seq'::regclass);


--
-- Name: service_kindworks_image id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.service_kindworks_image ALTER COLUMN id SET DEFAULT nextval('public.service_kindworks_image_id_seq'::regclass);


--
-- Name: service_kindworkscomments id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.service_kindworkscomments ALTER COLUMN id SET DEFAULT nextval('public.service_kindworkscomments_id_seq'::regclass);


--
-- Name: service_service id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.service_service ALTER COLUMN id SET DEFAULT nextval('public.service_service_id_seq'::regclass);


--
-- Name: service_service_image id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.service_service_image ALTER COLUMN id SET DEFAULT nextval('public.service_service_image_id_seq'::regclass);


--
-- Name: service_servicecomments id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.service_servicecomments ALTER COLUMN id SET DEFAULT nextval('public.service_servicecomments_id_seq'::regclass);


--
-- Name: service_unit id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.service_unit ALTER COLUMN id SET DEFAULT nextval('public.service_unit_id_seq'::regclass);


--
-- Name: site_some_settings_sitesettings id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.site_some_settings_sitesettings ALTER COLUMN id SET DEFAULT nextval('public.site_some_settings_sitesettings_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add Настройки сайта	7	add_sitesettings
26	Can change Настройки сайта	7	change_sitesettings
27	Can delete Настройки сайта	7	delete_sitesettings
28	Can view Настройки сайта	7	view_sitesettings
29	Can add Изображения	8	add_images
30	Can change Изображения	8	change_images
31	Can delete Изображения	8	delete_images
32	Can view Изображения	8	view_images
33	Can add Тематика работ	9	add_kindworks
34	Can change Тематика работ	9	change_kindworks
35	Can delete Тематика работ	9	delete_kindworks
36	Can view Тематика работ	9	view_kindworks
37	Can add Коментарии объектов "типы работ"	10	add_kindworkscomments
38	Can change Коментарии объектов "типы работ"	10	change_kindworkscomments
39	Can delete Коментарии объектов "типы работ"	10	delete_kindworkscomments
40	Can view Коментарии объектов "типы работ"	10	view_kindworkscomments
41	Can add Наименование работ	11	add_service
42	Can change Наименование работ	11	change_service
43	Can delete Наименование работ	11	delete_service
44	Can view Наименование работ	11	view_service
45	Can add Коментарии объектов объектов "предоставяемые услуги"	12	add_servicecomments
46	Can change Коментарии объектов объектов "предоставяемые услуги"	12	change_servicecomments
47	Can delete Коментарии объектов объектов "предоставяемые услуги"	12	delete_servicecomments
48	Can view Коментарии объектов объектов "предоставяемые услуги"	12	view_servicecomments
49	Can add Единица измерения	13	add_unit
50	Can change Единица измерения	13	change_unit
51	Can delete Единица измерения	13	delete_unit
52	Can view Единица измерения	13	view_unit
53	Can add Тексты страницы о компании и контакты	14	add_aboutus
54	Can change Тексты страницы о компании и контакты	14	change_aboutus
55	Can delete Тексты страницы о компании и контакты	14	delete_aboutus
56	Can view Тексты страницы о компании и контакты	14	view_aboutus
57	Can add Настройки страницы заказа обратного звонка	15	add_collback
58	Can change Настройки страницы заказа обратного звонка	15	change_collback
59	Can delete Настройки страницы заказа обратного звонка	15	delete_collback
60	Can view Настройки страницы заказа обратного звонка	15	view_collback
61	Can add Заказ клиента на звонок	16	add_collbackclient
62	Can change Заказ клиента на звонок	16	change_collbackclient
63	Can delete Заказ клиента на звонок	16	delete_collbackclient
64	Can view Заказ клиента на звонок	16	view_collbackclient
65	Can add Документация	17	add_documentation
66	Can change Документация	17	change_documentation
67	Can delete Документация	17	delete_documentation
68	Can view Документация	17	view_documentation
69	Can add FAQ/Часто задоваемые вопросы	18	add_faq
70	Can change FAQ/Часто задоваемые вопросы	18	change_faq
71	Can delete FAQ/Часто задоваемые вопросы	18	delete_faq
72	Can view FAQ/Часто задоваемые вопросы	18	view_faq
73	Can add Тексты главной страницы	19	add_homepagetext
74	Can change Тексты главной страницы	19	change_homepagetext
75	Can delete Тексты главной страницы	19	delete_homepagetext
76	Can view Тексты главной страницы	19	view_homepagetext
77	Can add Отзывы	20	add_maincomments
78	Can change Отзывы	20	change_maincomments
79	Can delete Отзывы	20	delete_maincomments
80	Can view Отзывы	20	view_maincomments
81	Can add Слайдер на главной странице	21	add_mainslider
82	Can change Слайдер на главной странице	21	change_mainslider
83	Can delete Слайдер на главной странице	21	delete_mainslider
84	Can view Слайдер на главной странице	21	view_mainslider
85	Can add Заказы клиентов	22	add_order
86	Can change Заказы клиентов	22	change_order
87	Can delete Заказы клиентов	22	delete_order
88	Can view Заказы клиентов	22	view_order
89	Can add Партнеры и бренды	23	add_partners
90	Can change Партнеры и бренды	23	change_partners
91	Can delete Партнеры и бренды	23	delete_partners
92	Can view Партнеры и бренды	23	view_partners
93	Can add Изображения	24	add_images
94	Can change Изображения	24	change_images
95	Can delete Изображения	24	delete_images
96	Can view Изображения	24	view_images
97	Can add Портфолио	25	add_portfolio
98	Can change Портфолио	25	change_portfolio
99	Can delete Портфолио	25	delete_portfolio
100	Can view Портфолио	25	view_portfolio
101	Can add Коментарии объектов портфолио	26	add_portfoliocomments
102	Can change Коментарии объектов портфолио	26	change_portfoliocomments
103	Can delete Коментарии объектов портфолио	26	delete_portfoliocomments
104	Can view Коментарии объектов портфолио	26	view_portfoliocomments
105	Can add Категории	27	add_topic
106	Can change Категории	27	change_topic
107	Can delete Категории	27	delete_topic
108	Can view Категории	27	view_topic
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	site_some_settings	sitesettings
8	service	images
9	service	kindworks
10	service	kindworkscomments
11	service	service
12	service	servicecomments
13	service	unit
14	others	aboutus
15	others	collback
16	others	collbackclient
17	others	documentation
18	others	faq
19	others	homepagetext
20	others	maincomments
21	others	mainslider
22	others	order
23	others	partners
24	portfolio	images
25	portfolio	portfolio
26	portfolio	portfoliocomments
27	portfolio	topic
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2019-02-18 04:01:21.905257+03
2	auth	0001_initial	2019-02-18 04:01:22.990137+03
3	admin	0001_initial	2019-02-18 04:01:23.106781+03
4	admin	0002_logentry_remove_auto_add	2019-02-18 04:01:23.121997+03
5	admin	0003_logentry_add_action_flag_choices	2019-02-18 04:01:23.137348+03
6	contenttypes	0002_remove_content_type_name	2019-02-18 04:01:23.215123+03
7	auth	0002_alter_permission_name_max_length	2019-02-18 04:01:23.231874+03
8	auth	0003_alter_user_email_max_length	2019-02-18 04:01:23.248247+03
9	auth	0004_alter_user_username_opts	2019-02-18 04:01:23.262514+03
10	auth	0005_alter_user_last_login_null	2019-02-18 04:01:23.281587+03
11	auth	0006_require_contenttypes_0002	2019-02-18 04:01:23.29011+03
12	auth	0007_alter_validators_add_error_messages	2019-02-18 04:01:23.303994+03
13	auth	0008_alter_user_username_max_length	2019-02-18 04:01:23.373474+03
14	auth	0009_alter_user_last_name_max_length	2019-02-18 04:01:23.398445+03
15	others	0001_initial	2019-02-18 04:01:23.985136+03
16	portfolio	0001_initial	2019-02-18 04:01:24.677736+03
17	service	0001_initial	2019-02-18 04:01:25.687841+03
18	sessions	0001_initial	2019-02-18 04:01:25.804275+03
19	site_some_settings	0001_initial	2019-02-18 04:01:25.937819+03
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
\.


--
-- Data for Name: others_aboutus; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.others_aboutus (id, text_about_us_page, text_about_us_page_2, phone, address, time_work, email, smal_company_name, discription_name, notes, full_company_name, fio_entrepreneur, ip_registration_address, inn_kpp, bin, okved, okpo, requisites, self_phone, self_email) FROM stdin;
\.


--
-- Data for Name: others_collback; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.others_collback (id, title, description, description_short, btn_name, image, avalible) FROM stdin;
\.


--
-- Data for Name: others_collbackclient; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.others_collbackclient (id, name_client, phone_client, coll_time, description_client, created, updated) FROM stdin;
\.


--
-- Data for Name: others_documentation; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.others_documentation (id, title, description, file, created, updated) FROM stdin;
\.


--
-- Data for Name: others_faq; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.others_faq (id, question, answer) FROM stdin;
\.


--
-- Data for Name: others_homepagetext; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.others_homepagetext (id, text_home_page, text_home_page_2) FROM stdin;
\.


--
-- Data for Name: others_maincomments; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.others_maincomments (id, name_person, email, phone, job_satisfaction, kind_job, comment_body, created, updated, moderation) FROM stdin;
\.


--
-- Data for Name: others_mainslider; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.others_mainslider (id, title, description, image, button_name, serial_number, created, updated) FROM stdin;
\.


--
-- Data for Name: others_order; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.others_order (id, name_client, phone_client, email_client, subject_work, description_client, file, created, updated) FROM stdin;
\.


--
-- Data for Name: others_partners; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.others_partners (id, name, image, link) FROM stdin;
\.


--
-- Data for Name: portfolio_images; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.portfolio_images (id, image, name, description, slug, created, updated) FROM stdin;
\.


--
-- Data for Name: portfolio_portfolio; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.portfolio_portfolio (id, name, slug, description, main_image, created, updated, availability, topic_id) FROM stdin;
\.


--
-- Data for Name: portfolio_portfolio_images; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.portfolio_portfolio_images (id, portfolio_id, images_id) FROM stdin;
\.


--
-- Data for Name: portfolio_portfoliocomments; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.portfolio_portfoliocomments (id, parent_object, name_person, email, comment_body, created, updated, moderation) FROM stdin;
\.


--
-- Data for Name: portfolio_topic; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.portfolio_topic (id, name, slug, descriprion) FROM stdin;
\.


--
-- Data for Name: service_images; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.service_images (id, image, name, description, slug, created, updated) FROM stdin;
\.


--
-- Data for Name: service_kindworks; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.service_kindworks (id, name, slug, intro, main_image, desctiption, created, updated, gallery_availability) FROM stdin;
\.


--
-- Data for Name: service_kindworks_image; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.service_kindworks_image (id, kindworks_id, images_id) FROM stdin;
\.


--
-- Data for Name: service_kindworkscomments; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.service_kindworkscomments (id, parent_object, name_person, email, comment_body, created, updated, moderation) FROM stdin;
\.


--
-- Data for Name: service_service; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.service_service (id, name, slug, main_image, desctiptions, created, updated, price, gallery_availability, kindworks_id, unit_id) FROM stdin;
\.


--
-- Data for Name: service_service_image; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.service_service_image (id, service_id, images_id) FROM stdin;
\.


--
-- Data for Name: service_servicecomments; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.service_servicecomments (id, parent_object, name_person, email, comment_body, created, updated, moderation) FROM stdin;
\.


--
-- Data for Name: service_unit; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.service_unit (id, name) FROM stdin;
\.


--
-- Data for Name: site_some_settings_sitesettings; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.site_some_settings_sitesettings (id, site_name, confirm_main_comments, confirm_portfolio_comments, confirm_services_comments, avalible_load_files_order, social_link_vk, social_link_youtube, social_link_linkedin, social_link_twitter, social_link_facebook, social_link_other_1, social_link_other_2) FROM stdin;
1	Название сайта	f	f	f	t	\N	\N	\N	\N	\N	\N	\N
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 108, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, false);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 27, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 19, true);


--
-- Name: others_aboutus_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.others_aboutus_id_seq', 1, false);


--
-- Name: others_collback_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.others_collback_id_seq', 1, false);


--
-- Name: others_collbackclient_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.others_collbackclient_id_seq', 1, false);


--
-- Name: others_documentation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.others_documentation_id_seq', 1, false);


--
-- Name: others_faq_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.others_faq_id_seq', 1, false);


--
-- Name: others_homepagetext_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.others_homepagetext_id_seq', 1, false);


--
-- Name: others_maincomments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.others_maincomments_id_seq', 1, false);


--
-- Name: others_mainslider_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.others_mainslider_id_seq', 1, false);


--
-- Name: others_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.others_order_id_seq', 1, false);


--
-- Name: others_partners_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.others_partners_id_seq', 1, false);


--
-- Name: portfolio_images_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.portfolio_images_id_seq', 1, false);


--
-- Name: portfolio_portfolio_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.portfolio_portfolio_id_seq', 1, false);


--
-- Name: portfolio_portfolio_images_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.portfolio_portfolio_images_id_seq', 1, false);


--
-- Name: portfolio_portfoliocomments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.portfolio_portfoliocomments_id_seq', 1, false);


--
-- Name: portfolio_topic_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.portfolio_topic_id_seq', 1, false);


--
-- Name: service_images_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.service_images_id_seq', 1, false);


--
-- Name: service_kindworks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.service_kindworks_id_seq', 1, false);


--
-- Name: service_kindworks_image_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.service_kindworks_image_id_seq', 1, false);


--
-- Name: service_kindworkscomments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.service_kindworkscomments_id_seq', 1, false);


--
-- Name: service_service_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.service_service_id_seq', 1, false);


--
-- Name: service_service_image_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.service_service_image_id_seq', 1, false);


--
-- Name: service_servicecomments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.service_servicecomments_id_seq', 1, false);


--
-- Name: service_unit_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.service_unit_id_seq', 1, false);


--
-- Name: site_some_settings_sitesettings_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.site_some_settings_sitesettings_id_seq', 1, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: others_aboutus others_aboutus_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.others_aboutus
    ADD CONSTRAINT others_aboutus_pkey PRIMARY KEY (id);


--
-- Name: others_collback others_collback_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.others_collback
    ADD CONSTRAINT others_collback_pkey PRIMARY KEY (id);


--
-- Name: others_collbackclient others_collbackclient_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.others_collbackclient
    ADD CONSTRAINT others_collbackclient_pkey PRIMARY KEY (id);


--
-- Name: others_documentation others_documentation_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.others_documentation
    ADD CONSTRAINT others_documentation_pkey PRIMARY KEY (id);


--
-- Name: others_faq others_faq_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.others_faq
    ADD CONSTRAINT others_faq_pkey PRIMARY KEY (id);


--
-- Name: others_homepagetext others_homepagetext_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.others_homepagetext
    ADD CONSTRAINT others_homepagetext_pkey PRIMARY KEY (id);


--
-- Name: others_maincomments others_maincomments_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.others_maincomments
    ADD CONSTRAINT others_maincomments_pkey PRIMARY KEY (id);


--
-- Name: others_mainslider others_mainslider_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.others_mainslider
    ADD CONSTRAINT others_mainslider_pkey PRIMARY KEY (id);


--
-- Name: others_order others_order_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.others_order
    ADD CONSTRAINT others_order_pkey PRIMARY KEY (id);


--
-- Name: others_partners others_partners_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.others_partners
    ADD CONSTRAINT others_partners_pkey PRIMARY KEY (id);


--
-- Name: portfolio_images portfolio_images_name_key; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.portfolio_images
    ADD CONSTRAINT portfolio_images_name_key UNIQUE (name);


--
-- Name: portfolio_images portfolio_images_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.portfolio_images
    ADD CONSTRAINT portfolio_images_pkey PRIMARY KEY (id);


--
-- Name: portfolio_portfolio_images portfolio_portfolio_images_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.portfolio_portfolio_images
    ADD CONSTRAINT portfolio_portfolio_images_pkey PRIMARY KEY (id);


--
-- Name: portfolio_portfolio_images portfolio_portfolio_images_portfolio_id_images_id_8f1fc3d0_uniq; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.portfolio_portfolio_images
    ADD CONSTRAINT portfolio_portfolio_images_portfolio_id_images_id_8f1fc3d0_uniq UNIQUE (portfolio_id, images_id);


--
-- Name: portfolio_portfolio portfolio_portfolio_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.portfolio_portfolio
    ADD CONSTRAINT portfolio_portfolio_pkey PRIMARY KEY (id);


--
-- Name: portfolio_portfoliocomments portfolio_portfoliocomments_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.portfolio_portfoliocomments
    ADD CONSTRAINT portfolio_portfoliocomments_pkey PRIMARY KEY (id);


--
-- Name: portfolio_topic portfolio_topic_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.portfolio_topic
    ADD CONSTRAINT portfolio_topic_pkey PRIMARY KEY (id);


--
-- Name: service_images service_images_name_key; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.service_images
    ADD CONSTRAINT service_images_name_key UNIQUE (name);


--
-- Name: service_images service_images_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.service_images
    ADD CONSTRAINT service_images_pkey PRIMARY KEY (id);


--
-- Name: service_kindworks_image service_kindworks_image_kindworks_id_images_id_f151af5a_uniq; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.service_kindworks_image
    ADD CONSTRAINT service_kindworks_image_kindworks_id_images_id_f151af5a_uniq UNIQUE (kindworks_id, images_id);


--
-- Name: service_kindworks_image service_kindworks_image_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.service_kindworks_image
    ADD CONSTRAINT service_kindworks_image_pkey PRIMARY KEY (id);


--
-- Name: service_kindworks service_kindworks_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.service_kindworks
    ADD CONSTRAINT service_kindworks_pkey PRIMARY KEY (id);


--
-- Name: service_kindworkscomments service_kindworkscomments_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.service_kindworkscomments
    ADD CONSTRAINT service_kindworkscomments_pkey PRIMARY KEY (id);


--
-- Name: service_service_image service_service_image_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.service_service_image
    ADD CONSTRAINT service_service_image_pkey PRIMARY KEY (id);


--
-- Name: service_service_image service_service_image_service_id_images_id_1177f691_uniq; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.service_service_image
    ADD CONSTRAINT service_service_image_service_id_images_id_1177f691_uniq UNIQUE (service_id, images_id);


--
-- Name: service_service service_service_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.service_service
    ADD CONSTRAINT service_service_pkey PRIMARY KEY (id);


--
-- Name: service_service service_service_slug_key; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.service_service
    ADD CONSTRAINT service_service_slug_key UNIQUE (slug);


--
-- Name: service_servicecomments service_servicecomments_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.service_servicecomments
    ADD CONSTRAINT service_servicecomments_pkey PRIMARY KEY (id);


--
-- Name: service_unit service_unit_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.service_unit
    ADD CONSTRAINT service_unit_pkey PRIMARY KEY (id);


--
-- Name: site_some_settings_sitesettings site_some_settings_sitesettings_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.site_some_settings_sitesettings
    ADD CONSTRAINT site_some_settings_sitesettings_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: portfolio_images_id_slug_a34270d5_idx; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX portfolio_images_id_slug_a34270d5_idx ON public.portfolio_images USING btree (id, slug);


--
-- Name: portfolio_images_name_fc64e1a7_like; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX portfolio_images_name_fc64e1a7_like ON public.portfolio_images USING btree (name varchar_pattern_ops);


--
-- Name: portfolio_images_slug_221986ce; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX portfolio_images_slug_221986ce ON public.portfolio_images USING btree (slug);


--
-- Name: portfolio_images_slug_221986ce_like; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX portfolio_images_slug_221986ce_like ON public.portfolio_images USING btree (slug varchar_pattern_ops);


--
-- Name: portfolio_portfolio_id_slug_ffcac6ee_idx; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX portfolio_portfolio_id_slug_ffcac6ee_idx ON public.portfolio_portfolio USING btree (id, slug);


--
-- Name: portfolio_portfolio_images_images_id_70ef752d; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX portfolio_portfolio_images_images_id_70ef752d ON public.portfolio_portfolio_images USING btree (images_id);


--
-- Name: portfolio_portfolio_images_portfolio_id_01b49866; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX portfolio_portfolio_images_portfolio_id_01b49866 ON public.portfolio_portfolio_images USING btree (portfolio_id);


--
-- Name: portfolio_portfolio_slug_7bbc2436; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX portfolio_portfolio_slug_7bbc2436 ON public.portfolio_portfolio USING btree (slug);


--
-- Name: portfolio_portfolio_slug_7bbc2436_like; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX portfolio_portfolio_slug_7bbc2436_like ON public.portfolio_portfolio USING btree (slug varchar_pattern_ops);


--
-- Name: portfolio_portfolio_topic_id_bb327ec6; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX portfolio_portfolio_topic_id_bb327ec6 ON public.portfolio_portfolio USING btree (topic_id);


--
-- Name: portfolio_topic_slug_df699cb6; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX portfolio_topic_slug_df699cb6 ON public.portfolio_topic USING btree (slug);


--
-- Name: portfolio_topic_slug_df699cb6_like; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX portfolio_topic_slug_df699cb6_like ON public.portfolio_topic USING btree (slug varchar_pattern_ops);


--
-- Name: service_images_id_slug_a18d3f38_idx; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX service_images_id_slug_a18d3f38_idx ON public.service_images USING btree (id, slug);


--
-- Name: service_images_name_ce272d6f_like; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX service_images_name_ce272d6f_like ON public.service_images USING btree (name varchar_pattern_ops);


--
-- Name: service_images_slug_cf63e96b; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX service_images_slug_cf63e96b ON public.service_images USING btree (slug);


--
-- Name: service_images_slug_cf63e96b_like; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX service_images_slug_cf63e96b_like ON public.service_images USING btree (slug varchar_pattern_ops);


--
-- Name: service_kindworks_id_slug_71b2fc8f_idx; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX service_kindworks_id_slug_71b2fc8f_idx ON public.service_kindworks USING btree (id, slug);


--
-- Name: service_kindworks_image_images_id_a0273911; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX service_kindworks_image_images_id_a0273911 ON public.service_kindworks_image USING btree (images_id);


--
-- Name: service_kindworks_image_kindworks_id_2d9cb436; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX service_kindworks_image_kindworks_id_2d9cb436 ON public.service_kindworks_image USING btree (kindworks_id);


--
-- Name: service_kindworks_slug_37d100c5; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX service_kindworks_slug_37d100c5 ON public.service_kindworks USING btree (slug);


--
-- Name: service_kindworks_slug_37d100c5_like; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX service_kindworks_slug_37d100c5_like ON public.service_kindworks USING btree (slug varchar_pattern_ops);


--
-- Name: service_service_id_slug_257fdbf0_idx; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX service_service_id_slug_257fdbf0_idx ON public.service_service USING btree (id, slug);


--
-- Name: service_service_image_images_id_94cec661; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX service_service_image_images_id_94cec661 ON public.service_service_image USING btree (images_id);


--
-- Name: service_service_image_service_id_3d0e9d96; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX service_service_image_service_id_3d0e9d96 ON public.service_service_image USING btree (service_id);


--
-- Name: service_service_kindworks_id_24117307; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX service_service_kindworks_id_24117307 ON public.service_service USING btree (kindworks_id);


--
-- Name: service_service_slug_542cade8_like; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX service_service_slug_542cade8_like ON public.service_service USING btree (slug varchar_pattern_ops);


--
-- Name: service_service_unit_id_499a81ee; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX service_service_unit_id_499a81ee ON public.service_service USING btree (unit_id);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: portfolio_portfolio_images portfolio_portfolio__images_id_70ef752d_fk_portfolio; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.portfolio_portfolio_images
    ADD CONSTRAINT portfolio_portfolio__images_id_70ef752d_fk_portfolio FOREIGN KEY (images_id) REFERENCES public.portfolio_images(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: portfolio_portfolio_images portfolio_portfolio__portfolio_id_01b49866_fk_portfolio; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.portfolio_portfolio_images
    ADD CONSTRAINT portfolio_portfolio__portfolio_id_01b49866_fk_portfolio FOREIGN KEY (portfolio_id) REFERENCES public.portfolio_portfolio(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: portfolio_portfolio portfolio_portfolio_topic_id_bb327ec6_fk_portfolio_topic_id; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.portfolio_portfolio
    ADD CONSTRAINT portfolio_portfolio_topic_id_bb327ec6_fk_portfolio_topic_id FOREIGN KEY (topic_id) REFERENCES public.portfolio_topic(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: service_kindworks_image service_kindworks_im_kindworks_id_2d9cb436_fk_service_k; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.service_kindworks_image
    ADD CONSTRAINT service_kindworks_im_kindworks_id_2d9cb436_fk_service_k FOREIGN KEY (kindworks_id) REFERENCES public.service_kindworks(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: service_kindworks_image service_kindworks_image_images_id_a0273911_fk_service_images_id; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.service_kindworks_image
    ADD CONSTRAINT service_kindworks_image_images_id_a0273911_fk_service_images_id FOREIGN KEY (images_id) REFERENCES public.service_images(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: service_service_image service_service_image_images_id_94cec661_fk_service_images_id; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.service_service_image
    ADD CONSTRAINT service_service_image_images_id_94cec661_fk_service_images_id FOREIGN KEY (images_id) REFERENCES public.service_images(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: service_service_image service_service_image_service_id_3d0e9d96_fk_service_service_id; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.service_service_image
    ADD CONSTRAINT service_service_image_service_id_3d0e9d96_fk_service_service_id FOREIGN KEY (service_id) REFERENCES public.service_service(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: service_service service_service_kindworks_id_24117307_fk_service_kindworks_id; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.service_service
    ADD CONSTRAINT service_service_kindworks_id_24117307_fk_service_kindworks_id FOREIGN KEY (kindworks_id) REFERENCES public.service_kindworks(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: service_service service_service_unit_id_499a81ee_fk_service_unit_id; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.service_service
    ADD CONSTRAINT service_service_unit_id_499a81ee_fk_service_unit_id FOREIGN KEY (unit_id) REFERENCES public.service_unit(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

