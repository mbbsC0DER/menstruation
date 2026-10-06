using Microsoft.AspNetCore.Mvc;
public class StudentController : Controller
{
    private static readonly Student[] students = [
        new() { Id = 1, Name = "Amit", Email = "amit@example.com", Course = "BCA", Marks = 85 },
        new() { Id = 2, Name = "Priya", Email = "priya@example.com", Course = "BSc IT", Marks = 90 }
    ];
    public IActionResult Index() => View(students);
    public IActionResult Details(int id)
    {
        var student = students.FirstOrDefault(s => s.Id == id);
        return student is null ? NotFound() : View(student);
    }
}
