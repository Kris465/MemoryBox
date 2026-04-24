<?php

class Category {
    protected $filters = [];

    public function __construct() {
    }

    public function getFilters() {
        return $this->filters;
    }
}

class PhoneCategory extends Category {
    public function __construct() {
        parent::__construct(); 

        $this->filters[] = 'Ram';
        $this->filters[] = 'CountSim';
        $this->filters[] = 'Hdd';
        $this->filters[] = 'OS';
    }
}

$phoneCategory = new PhoneCategory();
print_r($phoneCategory->getFilters());
?>