// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

contract SimpleStorage {
    uint256 public Salary; // Declare Salary as a public variable.

    // Struct to define Employees
    struct Employee {
        uint256 Salary;
        string name;
    }

    // Array to store Employee data
    Employee[] public employees;

    // Mapping to link employee name to their salary
    mapping(string => uint256) public nameToSalary;

    // Function to store a single salary value
    function store(uint256 _Salary) public {
        Salary = _Salary;
    }

    // Function to retrieve the stored salary value
    function retrieve() public view returns (uint256) {
        return Salary;
    }

    // Function to add an employee to the list
    function addPerson(string memory _name, uint256 _Salary) public {
        employees.push(Employee(_Salary, _name)); // Add employee to the array
        nameToSalary[_name] = _Salary; // Update the mapping
    }
}