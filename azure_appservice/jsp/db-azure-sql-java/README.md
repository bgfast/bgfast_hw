---
page_type: sample
languages:
- java
products:
- azure
description: "Azure SQL sample command line and jsp page"
---

# Developing a Java app using Azure SQL 


## Getting Started

### Prerequisites

* Before you can run this sample, you must have the following prerequisites:

   * An active Azure account. If you don't have one, you can sign up for a [free account](https://azure.microsoft.com/free/). 

   * Maven

### Quickstart

* First clone this repository using

```bash
git clone 
```

* From a command prompt or shell, run the following command to compile and resolve dependencies.

```bash
cd 
mvn clean package
```

* From a command prompt or shell, run the following command to run the application.

```bash
mvn exec:java -Dexec.mainClass="com.azure.sql.sample.HWMain"                                                    
```

## About the code

The code included in this sample is intended to get you quickly started with a Java application that connects to Azure SQL DB with the Microsoft JDBC driver

## More information

- [Java SDK JavaDoc for SQL ](TO BE UPDATED)

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
