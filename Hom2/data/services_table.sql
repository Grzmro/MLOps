CREATE TABLE IF NOT EXISTS disruptions (
    rdt_id               INTEGER PRIMARY KEY,
    ns_lines             TEXT,
    rdt_lines            TEXT,
    rdt_lines_id         TEXT,
    rdt_station_names    TEXT,
    rdt_station_codes    TEXT,
    cause_nl             TEXT,
    cause_en             TEXT,
    statistical_cause_nl TEXT,
    statistical_cause_en TEXT,
    cause_group          TEXT,
    start_time           TIMESTAMP NOT NULL,
    end_time             TIMESTAMP,
    duration_minutes     INTEGER
);

CREATE INDEX IF NOT EXISTS disruptions_start_time_idx ON disruptions (start_time);
