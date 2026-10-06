using Microsoft.AspNetCore.Mvc;
[ApiController, Route("api/students")]
public class StudentsController(IStudentService students) : ControllerBase
{
    [HttpGet] public IActionResult Index() => Ok("Student Management System is running.");
    [HttpGet("{id:int}")] public IActionResult ById(int id) => Ok($"Student ID: {id}");
    [HttpGet("{id:int}/details")]
    public IActionResult Details(int id)
    {
        var student = students.Find(id);
        return student is null ? NotFound(new { message = "Student not found" }) : Ok(student);
    }
    [HttpGet("{id:int}/name")]
    public IActionResult Name(int id)
    {
        var student = students.Find(id);
        return student is null ? NotFound(new { message = "Student not found" }) : Ok(student.Name);
    }
}
