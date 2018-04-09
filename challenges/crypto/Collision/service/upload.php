<?php
    //check for form post request
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        //check for whether files are uploaded
        if (empty($_FILES['file1']['name']) or empty($_FILES['file2']['name'])) {
            echo "Error! You never give enough files!";
        } else {
            //calculate SHA1 checksums of uploaded files
            $sha1_file1 = sha1_file($_FILES["file1"]["tmp_name"]);
            $sha1_file2 = sha1_file($_FILES["file2"]["tmp_name"]);

            //compare SHA1 checksums to check for collision
            if ($sha1_file1 === $sha1_file2) {

                //calculate SHA256 checksums of uploaded files
                $sha256_file1 = hash_file("SHA256", $_FILES["file1"]["tmp_name"]);
                $sha256_file2 = hash_file("SHA256", $_FILES["file2"]["tmp_name"]);

                //check whether file has been used
                $fp = fopen("collision.txt", "a+");
                $fsize = filesize("collision.txt");
                $ftext = fread( $fp, $fsize);

                //chech whether files have been accepted before
                if ((strpos($ftext, $sha256_file1) !== false) and (strpos($ftext, $sha256_file2) !== false)) {
                    echo "You cannot use repeated files! >:( <br>";
                    fclose($fp);
                } else {
                    //add strings
                    $data = $sha256_file1 . PHP_EOL;
                    fwrite($fp, $data);
                    $data = $sha256_file2 . PHP_EOL;
                    fwrite($fp, $sha256_file2);
                    //close
                    fclose($fp);
                    //reveal flag
                    echo "GCTF{c0llisi0n_av0id4nc3_f0r_n00b5}";
                }

            } else {
                echo "These 2 files don't have matching SHA1 checksums!";
            }
        }
    }
?>