/*
    renipress_diresa_departamento_rel debe ser una vista, sino se elimina
 */
DO
$do$
BEGIN
    IF (SELECT COUNT(*) FROM pg_catalog.pg_tables WHERE tablename='renipress_diresa_departamento_rel' LIMIT 1) >0
    THEN
        DROP TABLE IF EXISTS renipress_diresa_departamento_rel ;
    END IF;
END
$do$;

-- RELACION DIRESA - DEPARTAMENTO
CREATE or REPLACE VIEW renipress_diresa_departamento_rel AS
(
    SELECT diresa_id, departamento_id FROM renipress_EESS 
    GROUP BY diresa_id, departamento_id
    ORDER BY diresa_id, departamento_id
);


/*
    renipress_red_provincia_rel debe ser una vista, sino se elimina
 */
DO
$do$
BEGIN
    IF (SELECT COUNT(*) FROM pg_catalog.pg_tables WHERE tablename='renipress_red_provincia_rel' LIMIT 1) >0
    THEN
        DROP TABLE IF EXISTS renipress_red_provincia_rel ;
    END IF;
END
$do$;

-- RELACION RED - PROVINCIA
CREATE or REPLACE VIEW renipress_red_provincia_rel AS
(
    SELECT red_id, provincia_id FROM renipress_EESS
    GROUP BY red_id, provincia_id
    ORDER BY red_id, provincia_id
);