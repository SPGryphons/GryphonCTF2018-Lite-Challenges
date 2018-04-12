<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Team Search</title>
    </head>
    <style>
        html {
            font-family: arial, sans-serif;
        }
        
        table {
            border-collapse: collapse;
        }
        
        td, th {
            border : 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }
        
        tr:nth-child(even) {
            background-color: #dddddd;
        }
    </style>
    <body>
        <h1>Team Search</h1>
        <form action="" method="POST">
            Team Name:  <input type="text" name="teamname"><br><br>
            <input type="submit">
        </form>
        <?php
            if($_POST) {
                $teamname = $_POST['teamname'];
                class MyDB extends SQLite3 {
                    function __construct() {
                        $this->open('teams.db');
                    }
                }
                $db = new MyDB();
                if(!$db) {
                    echo $db->lastErrorMsg();
                } else {
                    $sql = "select * from teams where teamname = '" . $teamname . "';";
                    //echo $sql;

                    $ret = $db->query($sql);
                    echo "<br>";
                    echo "<h2>Results</h2>";
                    echo "<table><tr><th>Team Name</th><th>Class</th></tr>";
                    while($row = $ret->fetchArray(SQLITE3_ASSOC) ) {
                        echo "<tr><td>". $row['teamname'] . "</td>";
                        echo "<td>" . $row['class'] . "</td></tr>";
                    }
                    echo "</table><br>";
                //echo "Operation done successfully\n";
                $db->close();
                }
            }
        ?>
    </body>
</html>
