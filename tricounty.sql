-- PROJECT 2 DATABASE

-- DATA MODELING
-- Pulled from https://app.quickdatabasediagrams.com/#/d/Ln1t5S 

-- DATA ENGINEERING

CREATE TABLE "geographic" (
    "county" VARCHAR   NOT NULL,
    "city" VARCHAR   NOT NULL,
    "program_id" INT   NOT NULL
);

CREATE TABLE "pe_description" (
    "loc_description" VARCHAR   NOT NULL,
    "pe_desc" INT   NOT NULL,
    PRIMARY KEY (
        "loc_description"
     )
);

CREATE TABLE "programs" (
    "program_id" VARCHAR   NOT NULL,
    "county" VARCHAR   NOT NULL,
    "site_address" VARCHAR   NOT NULL,
    "total_violations" INT   NOT NULL,
    PRIMARY KEY (
        "program_id"
     )
);

CREATE TABLE "risk" (
    "risk_category" VARCHAR NOT NULL,
    "pe_desc" VARCHAR   NOT NULL,
    "program_id" INT   NOT NULL,
    PRIMARY KEY (
        "risk_category"
     )
);

CREATE TABLE "violations" (
    "program_id" VARCHAR   NOT NULL,
    "county" VARCHAR   NOT NULL,
    "site_address" VARCHAR   NOT NULL,
    "foodborne_illness_violations" INT   NOT NULL,
    "good_retail_practices_violations" INT   NOT NULL,
    "total_violations" INT   NOT NULL,
    "inspScore" INT   NOT NULL
);


SELECT * FROM geographic;
SELECT * FROM pe_description;
SELECT * FROM programs;
SELECT * FROM risk;
SELECT * FROM violations;