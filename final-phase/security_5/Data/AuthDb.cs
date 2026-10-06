using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore;
public class AuthDb(DbContextOptions<AuthDb> options) : IdentityDbContext<IdentityUser>(options) { }
