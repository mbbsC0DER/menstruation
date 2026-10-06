using Microsoft.AspNetCore.Mvc;
[ApiController, Route("api/students")]
public class StudentsController(StudentStore store) : ControllerBase
{
    [HttpGet] public IActionResult All() => Ok(store.All());
    [HttpGet("{id:int}")]
    public IActionResult ById(int id)
    {
        var student = store.Find(id);
        return student is null ? NotFound() : Ok(student);
    }
    [HttpPost]
    public IActionResult Create(Student input)
    {
        var student = store.Add(input);
        return CreatedAtAction(nameof(ById), new { id = student.Id }, student);
    }
    [HttpPut("{id:int}")]
    public IActionResult Update(int id, Student input) => store.Update(id, input) ? NoContent() : NotFound();
    [HttpDelete("{id:int}")]
    public IActionResult Delete(int id) => store.Delete(id) ? NoContent() : NotFound();
}
