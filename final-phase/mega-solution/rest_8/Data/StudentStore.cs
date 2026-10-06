public class StudentStore
{
    private readonly object gate = new();
    private readonly List<Student> students = [new Student {
        Id = 1, Name = "Amit", Email = "amit@example.com", Course = "BCA", Marks = 80
    }];
    private int nextId = 2;
    private static Student Copy(Student s) => new() { Id = s.Id, Name = s.Name, Email = s.Email, Course = s.Course, Marks = s.Marks };
    public Student[] All() { lock (gate) return students.Select(Copy).ToArray(); }
    public Student? Find(int id) { lock (gate) { var s = students.Find(s => s.Id == id); return s is null ? null : Copy(s); } }
    public Student Add(Student input)
    {
        lock (gate) { var student = Copy(input); student.Id = nextId++; students.Add(student); return Copy(student); }
    }
    public bool Update(int id, Student input)
    {
        lock (gate) {
            var s = students.Find(s => s.Id == id);
            if (s is null) return false;
            s.Name = input.Name; s.Email = input.Email; s.Course = input.Course; s.Marks = input.Marks;
            return true;
        }
    }
    public bool Delete(int id) { lock (gate) return students.RemoveAll(s => s.Id == id) > 0; }
}
