<?php     

function convert($number) {
    $numbers = array(
            100 => 'C',
            90 => 'XC',
            50 => 'L',
            40 => 'XL',
            10 => 'X',
            9 => 'IX',
            5 => 'V',
            4 => 'IV',
            1 => 'I'
        );
    $result = "";
    while ($number > 0) {
        foreach ($numbers as $key => $value) {
            if ($number >= $key) {
                $result = $result . $value;
                $number = $number - $key;
                break;
            }
        }
    }

    return $result;
}

?>