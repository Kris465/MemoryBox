<?php

class Category {
    protected $filters = [];

    public function __construct() {
    }

    public function getFilters() {
        return $this->filters;
    }
}

class MonitorCategory extends Category {
    public function __construct() {
        parent::__construct(); 

        $this->filters[] = 'Diagonal';
        $this->filters[] = 'Frequency';
    }
}

$monitorCategory = new MonitorCategory();
print_r($monitorCategory->getFilters());
?>