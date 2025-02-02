CREATE TYPE difficultyenum AS ENUM ('Dễ', 'Trung Bình', 'Khó');
CREATE TYPE genderenum AS ENUM ('Nữ', 'Nam', 'Khác');
CREATE TYPE roleenum AS ENUM ('user', 'admin');
CREATE TYPE submissionstatusenum AS ENUM ('Pending', 'Accepted', 'Wrong Answer', 'Time Limit Exeeded', 'Memory Limit Exeeded', 'Runtime Error', 'Compilation Error');

-- Table: organizations
CREATE TABLE organizations (
    id SERIAL PRIMARY KEY,
    ten_to_chuc VARCHAR(255) NOT NULL,
    mo_ta TEXT,
    ngay_tao TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- Table: users
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    ho_va_ten VARCHAR(255) NOT NULL,
    gioi_tinh genderenum DEFAULT 'Khác',
    ngay_sinh DATE,
    tieu_su TEXT,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    diem INTEGER DEFAULT 0,
    role roleenum DEFAULT 'user',
    email_verified TIMESTAMPTZ,
    verification_code TEXT NOT NULL,
    organization_id INTEGER REFERENCES organizations(id) ON DELETE SET NULL
);

-- Table: courses
CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    ten_khoa_hoc VARCHAR(255) NOT NULL,
    mo_ta TEXT,
    ngay_tao TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    nguoi_tao_id INTEGER REFERENCES users(id)
);

-- Table: course_problems
CREATE TABLE course_problems (
    course_id INTEGER REFERENCES courses(id) ON DELETE CASCADE,
    problem_id INTEGER REFERENCES problems(id) ON DELETE CASCADE,
    PRIMARY KEY (course_id, problem_id)
);

-- Table: contests
CREATE TABLE contests (
    id SERIAL PRIMARY KEY,
    ten_cuoc_thi VARCHAR(255) NOT NULL,
    mo_ta TEXT,
    thoi_gian_bat_dau TIMESTAMPTZ NOT NULL,
    thoi_gian_ket_thuc TIMESTAMPTZ NOT NULL,
    nguoi_tao_id INTEGER REFERENCES users(id),
    organization_id INTEGER REFERENCES organizations(id),
    ngay_tao TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- Table: contest_participants
CREATE TABLE contest_participants (
    contest_id INTEGER REFERENCES contests(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    diem INTEGER DEFAULT 0,
    thoi_gian_tha_gia TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (contest_id, user_id)
);

-- Table: contest_problems
CREATE TABLE contest_problems (
    contest_id INTEGER REFERENCES contests(id) ON DELETE CASCADE,
    problem_id INTEGER REFERENCES problems(id) ON DELETE CASCADE,
    PRIMARY KEY (contest_id, problem_id)
);

-- Table: problems
CREATE TABLE problems (
    id SERIAL PRIMARY KEY,
    tieu_de VARCHAR(255) NOT NULL,
    mo_ta TEXT NOT NULL,
    difficulty_id INTEGER REFERENCES difficulties(id) ON DELETE SET NULL,
    topic_id INTEGER REFERENCES topics(id) ON DELETE SET NULL,
    nguoi_tao_id INTEGER REFERENCES users(id),
    ngay_tao TIMESTAMPTZ,
    ngay_cap_nhat TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- Table: difficulties
CREATE TABLE difficulties (
    id SERIAL PRIMARY KEY,
    do_kho difficultyenum DEFAULT 'Dễ'
);

-- Table: topics
CREATE TABLE topics (
    id SERIAL PRIMARY KEY,
    ten_chu_de VARCHAR(100) NOT NULL
);

-- Table: discussions
CREATE TABLE discussions (
    id SERIAL PRIMARY KEY,
    problem_id INTEGER REFERENCES problems(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    tieu_de VARCHAR(255) NOT NULL,
    noi_dung TEXT NOT NULL,
    ngay_tao TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- Table: comments
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    discussion_id INTEGER REFERENCES discussions(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    noi_dung TEXT NOT NULL,
    ngay_tao TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- Table: languages
CREATE TABLE languages (
    id SERIAL PRIMARY KEY,
    ten_ngon_ngu VARCHAR(100) NOT NULL
);

-- Table: problem_languages
CREATE TABLE problem_languages (
    problem_id INTEGER REFERENCES problems(id) ON DELETE CASCADE,
    language_id INTEGER REFERENCES languages(id) ON DELETE CASCADE,
    PRIMARY KEY (problem_id, language_id)
);

-- Table: submissions
CREATE TABLE submissions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    problem_id INTEGER REFERENCES problems(id) ON DELETE CASCADE,
    code TEXT NOT NULL,
    language_id INTEGER REFERENCES languages(id),
    status submissionstatusenum DEFAULT 'Pending',
    thoi_gian_nop TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    thoi_gian_thuc_hien FLOAT,
    dung_luong_bo_nho INTEGER,
    contest_id INTEGER REFERENCES contests(id),
    diem INTEGER DEFAULT 0
);

-- Table: testcases
CREATE TABLE testcases (
    id SERIAL PRIMARY KEY,
    problem_id INTEGER REFERENCES problems(id) ON DELETE CASCADE,
    input_data TEXT NOT NULL,
    output_data TEXT NOT NULL,
    time_limit FLOAT,
    memory_limit INTEGER
);

-- Table: user_courses
CREATE TABLE user_courses (
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    course_id INTEGER REFERENCES courses(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, course_id)
);

-- Table: organizations
CREATE TABLE organizations (
    id SERIAL PRIMARY KEY,
    ten_to_chuc VARCHAR(255) NOT NULL,
    mo_ta TEXT,
    ngay_tao TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

