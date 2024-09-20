"""Mock data for enrollments"""

import pandas as pd

ENROLLMENTS = [
    {
        "enterprise_customer_name": "Hill Ltd",
        "enterprise_customer_uuid": "33ce656295e04ecfa2a77d407eb96f69",
        "lms_enrollment_id": 1013,
        "user_id": 8907,
        "email": "rebeccanelson@example.com",
        "course_key": "hEmW+tvk03",
        "courserun_key": "course-v1:hEmW+tvk03+1T9889",
        "course_id": "1681",
        "course_subject": "business-management",
        "course_title": "Re-engineered tangible approach",
        "enterprise_enrollment_date": "2021-07-04",
        "lms_enrollment_mode": "verified",
        "enroll_type": "certificate",
        "program_title": "Non-Program",
        "date_certificate_awarded": "2021-08-25",
        "grade_percent": 0.99,
        "cert_awarded": 1,
        "date_certificate_created_raw": "2021-08-25",
        "passed_date_raw": "2021-08-25",
        "passed_date": "2021-08-25",
        "has_passed": 1,
    },
    {
        "enterprise_customer_name": "Hill Ltd",
        "enterprise_customer_uuid": "33ce656295e04ecfa2a77d407eb96f69",
        "lms_enrollment_id": 9172,
        "user_id": 8369,
        "email": "taylorjames@example.com",
        "course_key": "hEmW+tvk03",
        "courserun_key": "course-v1:hEmW+tvk03+1T9889",
        "course_id": "1681",
        "course_subject": "business-management",
        "course_title": "Re-engineered tangible approach",
        "enterprise_enrollment_date": "2021-07-03",
        "lms_enrollment_mode": "verified",
        "enroll_type": "certificate",
        "program_title": "Non-Program",
        "date_certificate_awarded": "2021-09-01",
        "grade_percent": 0.93,
        "cert_awarded": 1,
        "date_certificate_created_raw": "2021-09-01",
        "passed_date_raw": "2021-09-01",
        "passed_date": "2021-09-01",
        "has_passed": 1,
    },
    {
        "enterprise_customer_name": "Hill Ltd",
        "enterprise_customer_uuid": "33ce656295e04ecfa2a77d407eb96f69",
        "lms_enrollment_id": 9552,
        "user_id": 8719,
        "email": "ssmith@example.com",
        "course_key": "qZJC+KFX86",
        "courserun_key": "course-v1:qZJC+KFX86+1T8918",
        "course_id": "1725",
        "course_subject": "medicine",
        "course_title": "Secured static capability",
        "enterprise_enrollment_date": "2021-05-11",
        "lms_enrollment_mode": "verified",
        "enroll_type": "certificate",
        "program_title": "Non-Program",
        "date_certificate_awarded": None,
        "grade_percent": 0.0,
        "cert_awarded": 0,
        "date_certificate_created_raw": None,
        "passed_date_raw": None,
        "passed_date": None,
        "has_passed": 0,
    },
    {
        "enterprise_customer_name": "Hill Ltd",
        "enterprise_customer_uuid": "33ce656295e04ecfa2a77d407eb96f69",
        "lms_enrollment_id": 3436,
        "user_id": 3125,
        "email": "kathleenmartin@example.com",
        "course_key": "QWXx+Jqz64",
        "courserun_key": "course-v1:QWXx+Jqz64+1T9449",
        "course_id": "4878",
        "course_subject": "social-sciences",
        "course_title": "Horizontal solution-oriented hub",
        "enterprise_enrollment_date": "2020-04-03",
        "lms_enrollment_mode": "verified",
        "enroll_type": "certificate",
        "program_title": "Non-Program",
        "date_certificate_awarded": None,
        "grade_percent": 0.0,
        "cert_awarded": 0,
        "date_certificate_created_raw": None,
        "passed_date_raw": None,
        "passed_date": None,
        "has_passed": 0,
    },
    {
        "enterprise_customer_name": "Hill Ltd",
        "enterprise_customer_uuid": "33ce656295e04ecfa2a77d407eb96f69",
        "lms_enrollment_id": 5934,
        "user_id": 4853,
        "email": "amber79@example.com",
        "course_key": "NOGk+UVD31",
        "courserun_key": "course-v1:NOGk+UVD31+1T4956",
        "course_id": "4141",
        "course_subject": "communication",
        "course_title": "Streamlined zero-defect attitude",
        "enterprise_enrollment_date": "2020-04-08",
        "lms_enrollment_mode": "verified",
        "enroll_type": "certificate",
        "program_title": "Non-Program",
        "date_certificate_awarded": None,
        "grade_percent": 0.0,
        "cert_awarded": 0,
        "date_certificate_created_raw": None,
        "passed_date_raw": None,
        "passed_date": None,
        "has_passed": 0,
    },
]

ENGAGEMENTS = [
    {
        "user_id": 2340,
        "email": "padillamichelle@example.org",
        "enterprise_customer_uuid": "33ce656295e04ecfa2a77d407eb96f69",
        "course_key": "luGg+KNt30",
        "enroll_type": "certificate",
        "activity_date": "2021-08-05",
        "course_title": "Synergized reciprocal encoding",
        "course_subject": "business-management",
        "is_engaged": 1,
        "is_engaged_video": 1,
        "is_engaged_forum": 0,
        "is_engaged_problem": 1,
        "is_active": 1,
        "learning_time_hours": 3724/3600,
        "learning_time_seconds": 3724,
    },
    {
        "user_id": 1869,
        "email": "yallison@example.org",
        "enterprise_customer_uuid": "33ce656295e04ecfa2a77d407eb96f69",
        "course_key": "luGg+KNt30",
        "enroll_type": "certificate",
        "activity_date": "2021-07-27",
        "course_title": "Synergized reciprocal encoding",
        "course_subject": "business-management",
        "is_engaged": 1,
        "is_engaged_video": 1,
        "is_engaged_forum": 0,
        "is_engaged_problem": 1,
        "is_active": 1,
        "learning_time_hours": 4335/3600,
        "learning_time_seconds": 4335,
    },
    {
        "user_id": 6962,
        "email": "weaverpatricia@example.net",
        "enterprise_customer_uuid": "33ce656295e04ecfa2a77d407eb96f69",
        "course_key": "luGg+KNt30",
        "enroll_type": "certificate",
        "activity_date": "2021-08-05",
        "course_title": "Synergized reciprocal encoding",
        "course_subject": "business-management",
        "is_engaged": 1,
        "is_engaged_video": 1,
        "is_engaged_forum": 0,
        "is_engaged_problem": 1,
        "is_active": 1,
        "learning_time_hours": 9441/3600,
        "learning_time_seconds": 9441,
    },
    {
        "user_id": 6798,
        "email": "seth57@example.org",
        "enterprise_customer_uuid": "33ce656295e04ecfa2a77d407eb96f69",
        "course_key": "luGg+KNt30",
        "enroll_type": "certificate",
        "activity_date": "2021-08-21",
        "course_title": "Synergized reciprocal encoding",
        "course_subject": "business-management",
        "is_engaged": 1,
        "is_engaged_video": 1,
        "is_engaged_forum": 1,
        "is_engaged_problem": 1,
        "is_active": 1,
        "learning_time_hours": 9898/3600,
        "learning_time_seconds": 9898,
    },
    {
        "user_id": 8530,
        "email": "mackwilliam@example.com",
        "enterprise_customer_uuid": "33ce656295e04ecfa2a77d407eb96f69",
        "course_key": "luGg+KNt30",
        "enroll_type": "certificate",
        "activity_date": "2021-10-24",
        "course_title": "Synergized reciprocal encoding",
        "course_subject": "business-management",
        "is_engaged": 0,
        "is_engaged_video": 0,
        "is_engaged_forum": 0,
        "is_engaged_problem": 0,
        "is_active": 1,
        "learning_time_hours": 0,
        "learning_time_seconds": 0,
    },
    {
        "user_id": 7584,
        "email": "graceperez@example.com",
        "enterprise_customer_uuid": "33ce656295e04ecfa2a77d407eb96f69",
        "course_key": "luGg+KNt30",
        "enroll_type": "certificate",
        "activity_date": "2022-05-17",
        "course_title": "Synergized reciprocal encoding",
        "course_subject": "business-management",
        "is_engaged": 0,
        "is_engaged_video": 0,
        "is_engaged_forum": 0,
        "is_engaged_problem": 0,
        "is_active": 1,
        "learning_time_hours": 21/3600,
        "learning_time_seconds": 21,
    },
    {
        "user_id": 68,
        "email": "yferguson@example.net",
        "enterprise_customer_uuid": "33ce656295e04ecfa2a77d407eb96f69",
        "course_key": "luGg+KNt30",
        "enroll_type": "certificate",
        "activity_date": "2021-09-02",
        "course_title": "Synergized reciprocal encoding",
        "course_subject": "business-management",
        "is_engaged": 1,
        "is_engaged_video": 1,
        "is_engaged_forum": 0,
        "is_engaged_problem": 1,
        "is_active": 1,
        "learning_time_hours": 4747/3600,
        "learning_time_seconds": 4747,
    },
    {
        "user_id": 4278,
        "email": "caseyjohnny@example.com",
        "enterprise_customer_uuid": "33ce656295e04ecfa2a77d407eb96f69",
        "course_key": "Kcpr+XoR30",
        "enroll_type": "certificate",
        "activity_date": "2022-05-20",
        "course_title": "Assimilated even-keeled focus group",
        "course_subject": "engineering",
        "is_engaged": 0,
        "is_engaged_video": 0,
        "is_engaged_forum": 0,
        "is_engaged_problem": 0,
        "is_active": 1,
        "learning_time_hours": 0,
        "learning_time_seconds": 0,
    },
    {
        "user_id": 8726,
        "email": "webertodd@example.com",
        "enterprise_customer_uuid": "33ce656295e04ecfa2a77d407eb96f69",
        "course_key": "luGg+KNt30",
        "enroll_type": "certificate",
        "activity_date": "2021-09-21",
        "course_title": "Synergized reciprocal encoding",
        "course_subject": "business-management",
        "is_engaged": 1,
        "is_engaged_video": 1,
        "is_engaged_forum": 1,
        "is_engaged_problem": 1,
        "is_active": 1,
        "learning_time_hours": 5285/3600,
        "learning_time_seconds": 5285,
    },
    {
        "user_id": 282,
        "email": "crystal86@example.net",
        "enterprise_customer_uuid": "33ce656295e04ecfa2a77d407eb96f69",
        "course_key": "luGg+KNt30",
        "enroll_type": "certificate",
        "activity_date": "2021-07-11",
        "course_title": "Synergized reciprocal encoding",
        "course_subject": "business-management",
        "is_engaged": 0,
        "is_engaged_video": 0,
        "is_engaged_forum": 0,
        "is_engaged_problem": 0,
        "is_active": 1,
        "learning_time_hours": 0,
        "learning_time_seconds": 0,
    },
    {
        "user_id": 2731,
        "email": "paul77@example.org",
        "enterprise_customer_uuid": "33ce656295e04ecfa2a77d407eb96f69",
        "course_key": "luGg+KNt30",
        "enroll_type": "certificate",
        "activity_date": "2021-07-26",
        "course_title": "Synergized reciprocal encoding",
        "course_subject": "business-management",
        "is_engaged": 1,
        "is_engaged_video": 1,
        "is_engaged_forum": 1,
        "is_engaged_problem": 1,
        "is_active": 1,
        "learning_time_hours": 15753/3600,
        "learning_time_seconds": 15753,
    },
    {
        "user_id": 4038,
        "email": "samanthaclarke@example.org",
        "enterprise_customer_uuid": "33ce656295e04ecfa2a77d407eb96f69",
        "course_key": "luGg+KNt30",
        "enroll_type": "certificate",
        "activity_date": "2021-07-19",
        "course_title": "Synergized reciprocal encoding",
        "course_subject": "business-management",
        "is_engaged": 0,
        "is_engaged_video": 0,
        "is_engaged_forum": 0,
        "is_engaged_problem": 0,
        "is_active": 1,
        "learning_time_hours": 29/3600,
        "learning_time_seconds": 29,
    }
]


def enrollments_dataframe():
    """Return a DataFrame of enrollments."""
    enrollments = pd.DataFrame(ENROLLMENTS)

    enrollments['enterprise_enrollment_date'] = enrollments['enterprise_enrollment_date'].astype('datetime64[ns]')
    enrollments['date_certificate_awarded'] = enrollments['date_certificate_awarded'].astype('datetime64[ns]')
    enrollments['date_certificate_created_raw'] = enrollments['date_certificate_created_raw'].astype('datetime64[ns]')
    enrollments['passed_date_raw'] = enrollments['passed_date_raw'].astype('datetime64[ns]')
    enrollments['passed_date'] = enrollments['passed_date'].astype('datetime64[ns]')

    return enrollments


def engagements_dataframe():
    """Return a DataFrame of engagements."""
    engagements = pd.DataFrame(ENGAGEMENTS)
    engagements['activity_date'] = engagements['activity_date'].astype('datetime64[ns]')
    return engagements


def leaderboard_csv_content():
    """Return the CSV content of leaderboard."""
    return (
        b'email,learning_time_hours,sessions,average_session_length,course_completions\r\n'
        b'paul77@example.org,4.4,1,4.4,\r\nseth57@example.org,2.7,1,2.7,\r\n'
        b'weaverpatricia@example.net,2.6,1,2.6,\r\nwebertodd@example.com,1.5,1,1.5,\r\n'
        b'yferguson@example.net,1.3,1,1.3,\r\nyallison@example.org,1.2,1,1.2,\r\n'
        b'padillamichelle@example.org,1.0,1,1.0,\r\ncaseyjohnny@example.com,0.0,0,0.0,\r\n'
        b'crystal86@example.net,0.0,0,0.0,\r\ngraceperez@example.com,0.0,0,0.0,\r\n'
        b'mackwilliam@example.com,0.0,0,0.0,\r\nsamanthaclarke@example.org,0.0,0,0.0,\r\n'
    )


LEADERBOARD_RESPONSE = [
    {
        "email": "paul77@example.org",
        "sessions": 1,
        "learning_time_hours": 4.4,
        "average_session_length": 4.4,
        "course_completions": None,
    },
    {
        "email": "seth57@example.org",
        "sessions": 1,
        "learning_time_hours": 2.7,
        "average_session_length": 2.7,
        "course_completions": None,
    },
    {
        "email": "weaverpatricia@example.net",
        "sessions": 1,
        "learning_time_hours": 2.6,
        "average_session_length": 2.6,
        "course_completions": None,
    },
    {
        "email": "webertodd@example.com",
        "sessions": 1,
        "learning_time_hours": 1.5,
        "average_session_length": 1.5,
        "course_completions": None,
    },
    {
        "email": "yferguson@example.net",
        "sessions": 1,
        "learning_time_hours": 1.3,
        "average_session_length": 1.3,
        "course_completions": None,
    },
    {
        "email": "yallison@example.org",
        "sessions": 1,
        "learning_time_hours": 1.2,
        "average_session_length": 1.2,
        "course_completions": None,
    },
    {
        "email": "padillamichelle@example.org",
        "sessions": 1,
        "learning_time_hours": 1.0,
        "average_session_length": 1.0,
        "course_completions": None,
    },
    {
        "email": "caseyjohnny@example.com",
        "sessions": 0,
        "learning_time_hours": 0.0,
        "average_session_length": 0.0,
        "course_completions": None,
    },
    {
        "email": "crystal86@example.net",
        "sessions": 0,
        "learning_time_hours": 0.0,
        "average_session_length": 0.0,
        "course_completions": None,
    },
    {
        "email": "graceperez@example.com",
        "sessions": 0,
        "learning_time_hours": 0.0,
        "average_session_length": 0.0,
        "course_completions": None,
    },
    {
        "email": "mackwilliam@example.com",
        "sessions": 0,
        "learning_time_hours": 0.0,
        "average_session_length": 0.0,
        "course_completions": None,
    },
    {
        "email": "samanthaclarke@example.org",
        "sessions": 0,
        "learning_time_hours": 0.0,
        "average_session_length": 0.0,
        "course_completions": None,
    },
]


TOP_SKILLS = [
    {
        "skill_name": "Python (Programming Language)",
        "skill_type": "Specialized Skill",
        "enrolls": 19027.0,
        "completions": 3004.0
    },
    {
        "skill_name": "Data Science",
        "skill_type": "Specialized Skill",
        "enrolls": 13756.0,
        "completions": 1517.0
    },
    {
        "skill_name": "Algorithms",
        "skill_type": "Specialized Skill",
        "enrolls": 12776.0,
        "completions": 1640.0
    },
]
TOP_SKILLS_BY_ENROLLMENTS = [
    {
        "skill_name": "Python (Programming Language)",
        "subject_name": "business-management",
        "count": 313.0
    },
    {
        "skill_name": "Machine Learning",
        "subject_name": "business-management",
        "count": 442.0
    },
    {
        "skill_name": "Computer Science",
        "subject_name": "business-management",
        "count": 39.0
    },
]
TOP_SKILLS_BY_COMPLETIONS = [
    {
        "skill_name": "Python (Programming Language)",
        "subject_name": "business-management",
        "count": 21.0
    },
    {
        "skill_name": "SQL (Programming Language)",
        "subject_name": "business-management",
        "count": 11.0
    },
    {
        "skill_name": "Algorithms",
        "subject_name": "business-management",
        "count": 15.0
    },
]
