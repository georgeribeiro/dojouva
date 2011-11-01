<?php 

require_once(dirname(__FILE__) . '/simpletest/autorun.php');
require_once(dirname(__FILE__) . '/roman.php');

class TestRoman extends UnitTestCase {
    
    function testConvertNumber_1() {
        $r = convert(1);
        $this->assertEqual($r, 'I');
    }

    function testConvertNumber_2() {
        $r = convert(2);
        $this->assertEqual($r, 'II');
    }

    function testConvertNumber_5() {
        $r = convert(5);
        $this->assertEqual($r, 'V');
    }

    function testConvertNumber_6() {
        $r = convert(6);
        $this->assertEqual($r, 'VI');
    }

    function testConvertNumber_7() {
        $r = convert(7);
        $this->assertEqual($r, 'VII');
    }

    function testConvertNumber_11() {
        $r = convert(11);
        $this->assertEqual($r, 'XI');
    }

    function testConvertNumber_55() {
        $r = convert(55);
        $this->assertEqual($r, 'LV');
    }

    function testConvertNumber_4() {
        $r = convert(4);
        $this->assertEqual($r, 'IV');
    }

    function testConvertNumber_9() {
        $r = convert(9);
        $this->assertEqual($r, 'IX');
    }

    function testConvertNumber_40() {
        $r = convert(40);
        $this->assertEqual($r, 'XL');
    }

    function testConvertNumber_19() {
        $r = convert(19);
        $this->assertEqual($r, 'XIX');
    }

    function testConvertNumber_42() {
        $r = convert(42);
        $this->assertEqual($r, 'XLII');
    }

    function testConvertNumber_49() {
        $r = convert(49);
        $this->assertEqual($r, 'XLIX');
    }

    function testConvertNumber_70() {
        $r = convert(70);
        $this->assertEqual($r, 'LXX');
    }

    function testConvertNumber_90() {
        $r = convert(90);
        $this->assertEqual($r, 'XC');
    }

    function testConvertNumber_190() {
        $r = convert(190);
        $this->assertEqual($r, 'CXC');
    }
}

?>