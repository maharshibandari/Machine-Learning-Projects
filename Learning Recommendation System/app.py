import streamlit as st
import mysql.connector
from mysql.connector import Error

# Database connection details
db_config = {
    'user': 'root',
    'password': 'akhila',
    'host': 'localhost',
    'database': 'job_data'
}

def fetch_job_recommendations():
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            st.success("Connected to MySQL database")

            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM job_info")
            jobs = cursor.fetchall()

            # Close the cursor and connection
            cursor.close()
        else:
            st.error("Failed to connect to MySQL database")
            return []

    except Error as e:
        st.error(f"Error: {e}")
        return []

    finally:
        if conn.is_connected():
            conn.close()
            st.info("MySQL connection is closed")

    return jobs

def display_job_recommendations(jobs):
    for job in jobs:
        st.write(f"### {job['job_title']}")
        st.write(f"**Company:** {job['company']}")
        st.write(f"**Salary Range:** {job['salary_range']}")
        st.write(f"**Responsibilities:** {job['responsibilities']}")
        st.write(f"**Qualifications:** {job['qualifications']}")
        st.write(f"**Additional Information:** {job['additional_information']}")
        st.write(f"**Personalized Advice:** {job['personalized_advice']}")
        st.write("---")

def main():
    st.title("Job Recommendation System")

    if st.button("Fetch Job Recommendations"):
        jobs = fetch_job_recommendations()
        if jobs:
            display_job_recommendations(jobs)
        else:
            st.warning("No job recommendations available")

if __name__ == '__main__':
    main()