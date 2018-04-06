<?php

function set_cookie($name, $value) {
    if (!isset($_COOKIE[$name]) || ($_COOKIE[$name] != $value)) {
        $_COOKIE[$name] = $value;
    }
    setcookie($name, $value, strtotime('+1 week'), '/');
}
set_cookie('FLAG', 'GCTF{C00K1E_M0N5T3R}');
?>
<!DOCTYPE html>
<html>
<body>
<input type="submit" name="GET FLAG" value="GET FLAG">
<?php
$count=10000000;
for (;;) {
    $count-=1;
    echo '<script type="text/javascript">alert("Press '.$count.' times more for the flag");</script>';
}
?>
</body>
</html>