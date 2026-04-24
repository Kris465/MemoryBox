/* Модификаторы доступа:
public - доступен из любого места
protected - доступен только в классе и его дечерних классах
private - доступен только в самом классе */
<?php
class BankAccount {
    private $balance;

    public function __construct($initialBlance)
    {
        $this->balance = $initialBlance;
    }

    public function deposit($amount) {
        $this->balance += $amount;
    }

    public function getBalance() {
        return $this->balance;
    }
}
?>