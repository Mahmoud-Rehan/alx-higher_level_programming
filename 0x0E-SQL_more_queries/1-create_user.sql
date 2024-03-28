-- Creates the MySQL server user
CREATE USER IF NOT EXIST "user_0d_2"@"localhost" IDENTIFIED BY "user_0d_2_pwd";
GRANT SELECT ON hbtn_0d_2.* TO "user_0d_2"@"localhost";
