document.getElementById('palindromeButton').addEventListener('click', function() {
    const number = document.getElementById('palindromeInput').value;
    const palindromeResult = document.getElementById('palindromeResult');
    
    const isPalindrome = number === number.split('').reverse().join('');
    palindromeResult.textContent = isPalindrome ? 'Число является палиндромом.' : 'Число не является палиндромом.';
});
