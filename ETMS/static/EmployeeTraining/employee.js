function Employee(na, em, dob, hd, add, ps)
{
    this.name = na;
    this.email = em;
    this.DOB = dob;
    this.hiredate = hd;
    this.address = add;
    this.password = ps;
}
var employees = [];
var userID = document.title;
function initEmployees()
{
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function()
    {
        if(this.readyState == 4 && this.status == 200)
        {
            var data = this.responseText;
            var employeeStrings = data.split(";");

            for(var i=0; i<employeeStrings.length; i++)
            {
                var employeeString = employeeStrings[i];
                var attributeStrings = employeeString.split(",");
                var newEmployee = new Employee(attributeStrings[0],attributeStrings[1],attributeStrings[2],attributeStrings[3],attributeStrings[4],attributeStrings[5],attributeStrings[6])
                employees.push(newEmployee);
            }
            index = findIndex(employees, userID);
            document.getElementById("name").innerHTML = employees[index].name;
            document.getElementById("address").innerHTML = employees[index].address;
            document.getElementById("email").innerHTML = employees[index].email;
            document.getElementById("DOB").innerHTML = employees[index].DOB;
        }
    };

    xhttp.open("GET", "/loadEmployee/",true);
    xhttp.send();
}

function findIndex(employeeClass, userID)
{
    for(i=0; i<employeeClass.length; i++)
    {
        if(employeeClass[i].password == userID)
        {
            return i;
        }
    }
}