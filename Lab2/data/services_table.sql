CREATE TABLE IF NOT EXISTS services (
    service_rdt_id BIGINT,
    service_date DATE,
    service_type TEXT,
    service_company TEXT,
    service_train_number INTEGER,
    service_completely_cancelled BOOLEAN,
    service_partly_cancelled BOOLEAN,
    service_maximum_delay INTEGER,
    stop_rdt_id BIGINT,
    stop_station_code TEXT,
    stop_station_name TEXT,
    stop_arrival_time TIMESTAMPTZ,
    stop_arrival_delay INTEGER,
    stop_arrival_cancelled BOOLEAN,
    stop_departure_time TIMESTAMPTZ,
    stop_departure_delay INTEGER,
    stop_departure_cancelled BOOLEAN,
    stop_platform_change BOOLEAN,
    stop_planned_platform TEXT,
    stop_actual_platform TEXT
);

CREATE INDEX IF NOT EXISTS services_service_rdt_id_idx ON services (service_rdt_id);
CREATE INDEX IF NOT EXISTS services_service_date_idx ON services (service_date);
CREATE INDEX IF NOT EXISTS services_train_number_date_idx ON services (service_train_number, service_date);
CREATE INDEX IF NOT EXISTS services_stop_station_code_idx ON services (stop_station_code);
CREATE INDEX IF NOT EXISTS services_service_type_idx ON services (service_type);
CREATE INDEX IF NOT EXISTS services_service_company_idx ON services (service_company);
