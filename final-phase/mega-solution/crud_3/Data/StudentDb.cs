using Microsoft.EntityFrameworkCore;
public class StudentDb(DbContextOptions<StudentDb> options) : DbContext(options)
{
    public DbSet<Student> Students => Set<Student>();
}
