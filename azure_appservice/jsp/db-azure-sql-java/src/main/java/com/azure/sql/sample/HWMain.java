// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.

package com.azure.sql.sample;
//import org.apache.logging.log4j.Level;
//import org.apache.logging.log4j.LogManager;
//import org.apache.logging.log4j.Logger;

import java.sql.*;

public class HWMain {

    private static String dbconnString="";
    /**
     * Run a Hello Azure SQL console application.
     *
     * @param args command line args.
     */
    // <Main>
    //  private static final Logger LOGGER = LogManager.getLogger(HWMain.class);

    public HWMain(){
        HWMain.dbconnString= System.getenv("SQLAZURECONNSTR_trafficcountconnstr");
        
    }
    public static void main(String[] args) {

        HWMain hw = new HWMain();

        String returnme = "";
        try {
            // To Do Figure out why the setLevel doesn't compile
            //LOGGER.setLevel(Level.DEBUG);
    //        LOGGER.info("This is an informational message.");
    //        LOGGER.debug("This is a debug message.");
    //        LOGGER.error("This is an error message.");
            returnme += "debug: count =" + hw.getAndIncrementCounter();
            returnme += "Demo complete, please hold while resources are released";
        } catch (Exception e) {
            e.printStackTrace();
            System.err.println(String.format("Azure SQL getStarted failed with %s", e));
        } finally {
            returnme += "Closing the client";
            // p.close();
        }
        System.out.println(returnme);
        System.exit(0);
    }

    public String getAndIncrementCounter() {
    //    LOGGER.info("This is an informational message.");
    //    LOGGER.debug("This is a debug message.");
    //    LOGGER.error("This is an error message.");
        
        String returnme="";
        
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
        } catch (ClassNotFoundException e) {
            returnme += "class.forName failed. ";
            e.printStackTrace();
            returnme += e.toString();

        }
        Connection conn = null;

        try{
            conn = DriverManager.getConnection(HWMain.dbconnString);

            Statement stmt = conn.createStatement();
            
            //////////////////////////////////
            //
            // get the count value from the db
            //
            String sql = "SELECT * FROM [dbo].[trafficcounttbl] where [dbo].[trafficcounttbl].[id] = 'trafficcount'";
            ResultSet rs = stmt.executeQuery(sql);
            int thecount = 0;
            while (rs.next()) {
                thecount = rs.getInt("count");
                returnme += "<p>trafficcount value from database:"+thecount;
            }
            thecount++;
            String sqlUpdate = "UPDATE trafficcounttbl SET count = " + thecount + " WHERE id = 'trafficcount'";
            stmt.executeUpdate(sqlUpdate);
            //
            //
            //////////////////////////////////////

        } catch (Exception e) {
            returnme += "<p>fail<p>";
            e.printStackTrace();
            returnme += e.toString();

        } finally {
            // Close the connection to the database
            try {
                conn.close();
                //returnme += "<p>Closed connection<p>";
            } catch (SQLException e) {
                e.printStackTrace();
                returnme += e.toString();
                returnme += "<p>Failed to close connection<p>";
            }
        }
        //return "" + count;
    
        
        return returnme;
    }

    
    public String resetDatabaseTable() {
        //    LOGGER.info("This is an informational message.");
        //    LOGGER.debug("This is a debug message.");
        //    LOGGER.error("This is an error message.");
            String returnme="";
            
            try {
                Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            } catch (ClassNotFoundException e) {
                returnme += "class.forName failed. ";
                e.printStackTrace();
                returnme += e.toString();
            }
    
            Connection conn = null;
    
            try{
                conn = DriverManager.getConnection(HWMain.dbconnString);
            
                //////////////////////////////////
                //
                // get the table from the metadata 
                //
                DatabaseMetaData md = conn.getMetaData();
                ResultSet mdre = md.getTables(null,null,"traffic%",null);
                while(mdre.next()){
                    returnme += "<p>Table:"+mdre.getString(3);
                }
                //
                //
                /////////////////////////////////
    
                //////////////////////////
                //
                // drop the table
                //
                String dropsql = "DROP TABLE trafficcouttbl";
    
                try (Statement dropstmt = conn.createStatement()) {
                    dropstmt.execute(dropsql);
                    returnme += "<p>Table dropped successfully...";
                } catch (SQLException e) {
                    e.printStackTrace();
                    returnme += e.toString();
                }
                //
                //
                ///////////////////////
    
                //////////////////////////
                //
                // create the table
                //
                String createsql = "CREATE TABLE trafficcouttbl ("
                + "count INT,"
                + "id VARCHAR(25)"
                + ")";
    
                try (Statement createstmt = conn.createStatement()) {
                    createstmt.execute(createsql);
                    returnme += "<p>Table created successfully...";
    
                    createsql = "INSERT INTO trafficcouttbl (count, id) VALUES (10, 'trafficcount')";
                    createstmt.executeUpdate(createsql);
                    returnme += "<p> Values inserted successfully...";
                } catch (SQLException e) {
                    e.printStackTrace();
                    returnme += e.toString();
                }
                //
                //////////////////////////////
    
                //////////////////////////////
                //
                // get column names and all rows from the table
                DatabaseMetaData mdtrafficcounttbl = conn.getMetaData();
                ResultSet rset = mdtrafficcounttbl.getColumns(null, null, "trafficcouttbl", null);
                returnme += "<p>Column names:";
                int colindex =1;
                while (rset.next()) {
                    returnme += "<p>" + rset.getString(colindex);
                    colindex++;
                }
                
                returnme += "Row values:";
                Statement allrowsstmt = conn.createStatement();
                ResultSet allrowsrs = allrowsstmt.executeQuery("SELECT * FROM trafficcouttbl");
                while (allrowsrs.next()) {
                    returnme += "<p>" + allrowsrs.getString(1) + "\t" + allrowsrs.getString(2) ;
                }
                //
                //            
                /////////////////////////////
    
            } catch (Exception e) {
                returnme += "<p>fail 5";
                e.printStackTrace();
                returnme += e.toString();
    
            } finally {
                // Close the connection to the database
                try {
                    conn.close();
                    //returnme += "<p>Closed connection<p>";
                } catch (SQLException e) {
                    e.printStackTrace();
                    returnme += e.toString();
    
                    returnme += "<p>Failed to close connection<p>";
                }
            }
            return returnme;
        }
}
