public record StudentInfo(int Id, string Name, string Course);
public interface IStudentService { StudentInfo? Find(int id); }
public class StudentService : IStudentService
{
    public StudentInfo? Find(int id) => id switch
    {
        101 => new(101, "Rahul Sharma", "BCA"),
        102 => new(102, "Priya Patil", "BCA"),
        103 => new(103, "Amit Joshi", "BCA"),
        _ => null
    };
}
