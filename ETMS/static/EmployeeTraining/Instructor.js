/**
 * Created by jingx on 2016/11/23.
 */
function Instructor(na, ph, sp, ps)
{
    this.name = na;
    this.phone = ph;
    this.speciality = sp;
    this.password = ps
}
var instructors = [];
var userID = document.title;
function initInstructor()
{
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function()
    {
        if(this.readyState == 4 && this.status == 200)
        {
            var data = this.responseText;
            var instructorStrings = data.split(";");

            for(var i=0; i<instructorStrings.length; i++)
            {
                var instructorString = instructorStrings[i];
                var attributeStrings = instructorString.split(",");
                var newinstructor = new Instructor(attributeStrings[0],attributeStrings[1],attributeStrings[2],attributeStrings[3]);
                instructors.push(newinstructor);
            }

            index = findIndex(instructors, userID);
            document.getElementById("name").innerHTML = instructors[index].name;
            document.getElementById("phone").innerHTML = instructors[index].phone;
            document.getElementById("speciality").innerHTML = instructors[index].speciality;
        }
    };
    xhttp.open("GET", "/loadInstructor/",true);
    xhttp.send();
}

function findIndex(Class, userID)
{
    for (i = 0; i < Class.length; i++) {
        if (Class[i].password == userID) {
            return i;
        }
    }
}

function addCourse()
{
    var phone = document.getElementById("phone").innerHTML;
    newxhttp = new XMLHttpRequest();
    var title = document.getElementById("title").value;
    var description = document.getElementById("description").value;
    var level = document.getElementById("level").value;
    if(title=='')
    {
        alert("Not valid.");
    }
    else
    {
        var parameter = "?title="+title+"&description="+description+"&level="+level+"&phone="+phone;
        newxhttp.open("GET", "/addCourse/"+parameter, true);
        newxhttp.send();
        alert("Successful.");
    }
}