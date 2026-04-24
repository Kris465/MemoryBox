document.getElementById('chisloButton').addEventListener('click', function() {
    const chislo = document.getElementById('chisloInput').value;
    const chisloResult = document.getElementById('chisloResult');

    const isPalindrome = chislo == chislo.split('').reverse().join('');
    chisloResult.textContent = isPalindrome ? 'число является палиндромом' : 'число не является палиндромом';

});