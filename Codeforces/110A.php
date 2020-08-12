<?php 
$var = readline();
$count = 0;
for ($i=0; $i<strlen($var); $i++)
    if($var[$i] == '7' || $var[$i] == '4') 
        $count++;    
echo ($count == 4 || $count==7)?"YES":"NO";
?>