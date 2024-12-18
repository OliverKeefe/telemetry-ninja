CREATE DATABASE IF NOT EXISTS telemetry;

USE telemetry;

CREATE TABLE iracing_telemetry (
    id INT PRIMARY KEY AUTO_INCREMENT,
    session_uuid VARCHAR(36),
    time_date TIMESTAMP AUTO_INCREMENT,
    skies VARCHAR(50),
    air_density FLOAT,
    air_pressure FLOAT,
    air_temp FLOAT,
    brake FLOAT,
    brake_abs_active BOOLEAN,
    brake_raw FLOAT,
    cam_camera_number INT,
    cam_camera_state INT,
    cam_car_idx INT,
    cam_group_number INT,
    cam_switch_num INT,
    car_class_est_lap_time FLOAT,
    car_idx_best_lap_num INT,
    car_idx_best_lap_time FLOAT,
    car_idx_class INT,
    car_idx_class_position INT,
    car_idx_est_time FLOAT,
    car_idx_f2_time FLOAT,
    car_idx_fast_repairs_used INT,
    car_idx_gear INT,
    car_idx_lap INT,
    car_idx_lap_completed INT,
    car_idx_lap_dist_pct FLOAT,
    car_idx_last_lap_time FLOAT,
    car_idx_on_pit_road BOOLEAN,
    car_idx_p2p_count INT,
    car_idx_p2p_status INT,
    car_idx_pace_flags INT,
    car_idx_pace_line INT,
    car_idx_pace_row INT,
    car_idx_position INT,
    car_idx_qual_tire_compound VARCHAR(50),
    car_idx_qual_tire_compound_locked BOOLEAN,
    car_idx_rpm INT,
    car_idx_steer FLOAT,
    car_idx_tire_compound VARCHAR(50),
    car_idx_track_surface INT,
    car_idx_track_surface_material INT,
    car_left_right INT,
    chan_avg_latency FLOAT,
    chan_clock_skew FLOAT,
    chan_latency FLOAT,
    chan_partner_quality FLOAT,
    chan_quality FLOAT,
    clutch FLOAT,
    cpu_usage_bg FLOAT,
    dc_drivers_so_far INT,
    dc_lap_status INT,
    display_units INT,
    driver_marker BOOLEAN,
    energy_battery_to_mgu_klap FLOAT,
    energy_ers_battery FLOAT,
    energy_ers_battery_pct FLOAT,
    energy_mgu_klap_deploy_pct FLOAT,
    engine_warnings INT,
    enter_exit_reset BOOLEAN,
    fast_repair_available INT,
    fast_repair_used INT,
    fog_level FLOAT,
    frame_rate FLOAT,
    fuel_level FLOAT,
    fuel_level_pct FLOAT,
    fuel_press FLOAT,
    fuel_use_per_hour FLOAT,
    gear INT,
    gpu_usage FLOAT,
    hand_brake FLOAT,
    hand_brake_raw FLOAT,
    hf_shock_defl FLOAT,
    hf_shock_defl_st FLOAT,
    hf_shock_vel FLOAT,
    hf_shock_vel_st FLOAT,
    hr_shock_defl FLOAT,
    hr_shock_defl_st FLOAT,
    hr_shock_vel FLOAT,
    hr_shock_vel_st FLOAT,
    is_disk_logging_active BOOLEAN,
    is_disk_logging_enabled BOOLEAN,
    is_in_garage BOOLEAN,
    is_on_track BOOLEAN,
    is_on_track_car BOOLEAN,
    is_replay_playing BOOLEAN,
    lap INT,
    lap_best_lap INT,
    lap_best_lap_time FLOAT,
    lap_best_nlap_lap INT,
    lap_best_nlap_time FLOAT,
    lap_current_lap_time FLOAT,
    lap_delta_to_best_lap FLOAT,
    lap_delta_to_best_lap_dd FLOAT,
    lap_delta_to_best_lap_ok BOOLEAN,
    lap_delta_to_optimal_lap FLOAT,
    lap_delta_to_optimal_lap_dd FLOAT,
    lap_delta_to_optimal_lap_ok BOOLEAN,
    lap_delta_to_session_best_lap FLOAT,
    lap_delta_to_session_best_lap_dd FLOAT,
    lap_delta_to_session_best_lap_ok BOOLEAN,
    lap_delta_to_session_lastl_lap FLOAT,
    lap_delta_to_session_lastl_lap_dd FLOAT,
    lap_delta_to_session_lastl_lap_ok BOOLEAN,
    lap_delta_to_session_optimal_lap FLOAT,
    lap_delta_to_session_optimal_lap_dd FLOAT,
    lap_delta_to_session_optimal_lap_ok BOOLEAN,
    lap_dist FLOAT,
    lap_dist_pct FLOAT,
    lap_las_nlap_seq INT,
    lap_last_lap_time FLOAT,
    lap_last_nlap_time FLOAT,
    lat_accel FLOAT,
    lat_accel_st FLOAT,
    left_tire_sets_available INT,
    left_tire_sets_used INT,
    load_num_textures INT,
    long_accel FLOAT,
    long_accel_st FLOAT,
    manifold_press FLOAT,
    manual_boost BOOLEAN,
    manual_no_boost BOOLEAN,
    mem_page_fault_sec FLOAT,
    oil_level FLOAT,
    oil_press FLOAT,
    oil_temp FLOAT,
    ok_to_reload_textures BOOLEAN,
    on_pit_road BOOLEAN,
    pace_mode INT,
    pitch FLOAT,
    pitch_rate FLOAT,
    pitch_rate_st FLOAT,
    pit_opt_repair_left FLOAT,
    pit_repair_left FLOAT,
    pits_open BOOLEAN,
    pitstop_active BOOLEAN,
    pit_sv_flags INT,
    pit_sv_fuel BOOLEAN,
    pit_sv_lfp BOOLEAN,
    pit_sv_lrp BOOLEAN,
    pit_sv_rfp BOOLEAN,
    pit_sv_rrp BOOLEAN,
    pit_sv_tire_compound VARCHAR(50),
    player_car_class INT,
    player_car_class_position INT,
    player_car_driver_incident_count INT,
    player_car_dry_tire_set_limit INT,
    player_car_idx INT,
    player_car_in_pit_stall BOOLEAN,
    player_car_my_incident_count INT,
    player_car_pit_sv_status INT,
    player_car_position INT,
    player_car_power_adjust FLOAT,
    player_car_team_incident_count INT,
    player_car_tow_time FLOAT,
    player_fast_repairs_used INT,
    player_tire_compound VARCHAR(50),
    player_track_surface INT,
    player_track_surface_material INT,
    push_to_pass BOOLEAN,
    push_to_talk BOOLEAN,
    race_laps INT,
    radio_transmit_car_idx INT,
    radio_transmit_frequency_idx INT,
    radio_transmit_radio_idx INT,
    rear_tire_sets_available INT,
    rear_tire_sets_used INT,
    relative_humidity FLOAT,
    replay_frame_num INT,
    replay_play_slow_motion BOOLEAN,
    replay_play_speed FLOAT,
    replay_session_num INT,
    replay_session_time FLOAT,
    right_tire_sets_available INT,
    right_tire_sets_used INT,
    roll FLOAT,
    roll_rate FLOAT,
    roll_rate_st FLOAT,
    rpm INT,
    session_flags INT,
    session_laps_remain INT,
    session_laps_remain_ex FLOAT,
    session_laps_total INT,
    session_num INT,
    session_state INT,
    session_tick INT,
    session_time FLOAT,
    session_time_of_day FLOAT,
    session_time_remain FLOAT,
    session_time_total FLOAT,
    session_unique_id INT,
    shift_grind_rpm INT,
    shift_indicator_pct FLOAT,
    shift_power_pct FLOAT,
    solar_altitude FLOAT,
    solar_azimuth FLOAT,
    speed FLOAT,
    steering_wheel_angle FLOAT,
    steering_wheel_angle_max FLOAT,
    steering_wheel_limiter BOOLEAN,
    steering_wheel_pct_damper FLOAT,
    steering_wheel_pct_torque FLOAT,
    steering_wheel_pct_torque_sign FLOAT,
    steering_wheel_pct_torque_sign_stops FLOAT,
    steering_wheel_peak_force_nm FLOAT,
    steering_wheel_torque FLOAT,
    steering_wheel_torque_st FLOAT,
    throttle FLOAT,
    throttle_raw FLOAT,
    tire_lf_rumble_pitch FLOAT,
    tire_lr_rumble_pitch FLOAT,
    tire_rf_rumble_pitch FLOAT,
    tire_rr_rumble_pitch FLOAT,
    tire_sets_available INT,
    tire_sets_used INT,
    track_temp FLOAT,
    track_temp_crew FLOAT,
    velocity_x FLOAT,
    velocity_x_st FLOAT,
    velocity_y FLOAT,
    velocity_y_st FLOAT,
    velocity_z FLOAT,
    velocity_z_st FLOAT,
    vert_accel FLOAT,
    vert_accel_st FLOAT,
    vid_cap_active BOOLEAN,
    vid_cap_enabled BOOLEAN,
    voltage FLOAT,
    water_level FLOAT,
    water_temp FLOAT,
    weather_type INT,
    wind_dir FLOAT,
    wind_vel FLOAT,
    yaw FLOAT,
    yaw_north FLOAT,
    yaw_rate FLOAT,
    yaw_rate_st FLOAT

    -- FOREIGN KEY (speed_unit_id) REFERENCES measurement_units(id)
);


CREATE TABLE f1_23_telemetry (
    id INT PRIMARY KEY AUTO_INCREMENT,
    session_uuid VARCHAR(36),
    time_date TIMESTAMP
);

CREATE TABLE measurement_units (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(10),
    description TEXT
);