using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
public class StudentsController(StudentDb db) : Controller
{
    public async Task<IActionResult> Index() => View(await db.Students.OrderBy(s => s.Id).ToListAsync());
    public IActionResult Create() => View("Edit", new Student());
    [HttpPost, ValidateAntiForgeryToken]
    public async Task<IActionResult> Create([Bind("Name,Email,Course,Marks")] Student student)
    {
        if (!ModelState.IsValid) return View("Edit", student);
        db.Students.Add(student);
        await db.SaveChangesAsync();
        return RedirectToAction(nameof(Index));
    }
    public async Task<IActionResult> Edit(int id)
    {
        var student = await db.Students.FindAsync(id);
        return student is null ? NotFound() : View(student);
    }
    [HttpPost, ValidateAntiForgeryToken]
    public async Task<IActionResult> Edit(int id, [Bind("Id,Name,Email,Course,Marks")] Student input)
    {
        if (id != input.Id) return BadRequest();
        var student = await db.Students.FindAsync(id);
        if (student is null) return NotFound();
        if (!ModelState.IsValid) return View(input);
        student.Name = input.Name; student.Email = input.Email;
        student.Course = input.Course; student.Marks = input.Marks;
        await db.SaveChangesAsync();
        return RedirectToAction(nameof(Index));
    }
    public async Task<IActionResult> Details(int id)
    {
        var student = await db.Students.FindAsync(id);
        return student is null ? NotFound() : View(student);
    }
    [HttpPost, ValidateAntiForgeryToken]
    public async Task<IActionResult> Delete(int id)
    {
        var student = await db.Students.FindAsync(id);
        if (student is null) return NotFound();
        db.Students.Remove(student);
        await db.SaveChangesAsync();
        return RedirectToAction(nameof(Index));
    }
}
