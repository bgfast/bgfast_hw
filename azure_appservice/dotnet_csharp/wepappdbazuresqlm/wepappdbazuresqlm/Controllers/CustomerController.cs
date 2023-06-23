using Microsoft.AspNetCore.Mvc;
using System.Data;
using System.Text.Json;
using System.Text;
using System.Data.SqlClient;
using Microsoft.Extensions.Options;
using wepappdbazuresqlm.Configuration;

namespace wepappdbazuresqlm.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class CustomerController : ControllerBase
    {

        private readonly ILogger<CustomerController> _logger;
        private readonly IOptions<ConnectionStrings> _options;

        public CustomerController(ILogger<CustomerController> logger, IOptions<ConnectionStrings> options)
        {
            _logger = logger;
            _options = options;
        }

        [HttpGet(Name = "GetCustomers")]
        public IActionResult Get()
        {
            try
            {
               

                using (SqlConnection connection = new SqlConnection(_options.Value.SqlConnectionString))
                {
                    connection.Open();
                    StringBuilder sb = new StringBuilder();
                    sb.Append("SELECT * FROM [SalesLT].[Customer];");
                    String sql = sb.ToString();

                    using (SqlCommand command = new SqlCommand(sql, connection))
                    {
                        using (SqlDataReader reader = command.ExecuteReader())
                        {
                            var list=new List<Customer>();
                            while (reader.Read())
                            {
                                var result = (IDataRecord)reader;
                                Console.WriteLine(JsonSerializer.Serialize(result));
                                list.Add(new Customer()
                                {
                                    FirstName = result["FirstName"].ToString(),
                                    LastName = result["LastName"].ToString(),
                                    CustomerID = (int)result["CustomerID"]
                                });
                                //while (reader.Read()) 
                                //{ 
                                //    reader.Read();
                                //}
                                //returnme += reader.;
                            }
                            if (list.Any())
                            {
                                return new OkObjectResult(JsonSerializer.Serialize(list));
                            }
                            else {
                                return new NotFoundObjectResult(new{ });
                            }
                            
                        }
                    }
                }
            }
            catch (SqlException e)
            {
                Console.WriteLine(e.ToString());
            }
            return Ok();
        }
    }
}