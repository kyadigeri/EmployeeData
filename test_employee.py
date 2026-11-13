from employee import employee_details

def test_employee_details_Varun():
    result = employee_details("Varun", 123, "IT", 45000)

    expected_emp = (
        "Employee Name: Varun\n"
        "Employee ID: 123\n"
        "Department: IT\n"
        "Salary: 45000"
    )

    assert result == expected_emp