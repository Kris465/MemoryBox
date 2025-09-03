<?php
class StringUtils {
    /**
     * @param string 
     * @param string 
     * @return int 
     */
    public static function countChar(string $str, string $char): int {
        $count = 0;
        for ($i = 0; $i < strlen($str); $i++) {
            if ($str[$i] === $char) {
                $count++;
            }
        }
        return $count;
    }

    /**
     * @param string 
     * @param string 
     * @param string 
     * @return string 
     */
    public static function replaceChar(string $str, string $oldChar, string $newChar): string {
        $result = '';
        for ($i = 0; $i < strlen($str); $i++) {
            $result .= ($str[$i] === $oldChar) ? $newChar : $str[$i];
        }
        return $result;
    }

    /**
     * @param string 
     * @return string
     */
    public static function reverse(string $str): string {
        $result = '';
        for ($i = strlen($str) - 1; $i >= 0; $i--) {
            $result .= $str[$i];
        }
        return $result;
    }

    /**
     * @param string 
     * @return array 
     */
    public static function splitToWords(string $str): array {
        return explode(' ', $str);
    }

    /**
     * @param string
     * @return string
     * @throws 
     */
    public static function detectAlphabet(string $str): string {
        if (empty($str)) {
            throw new Exception("Пустая строка");
        }

        $hasCyrillic = false;
        $hasLatin = false;

        for ($i = 0; $i < strlen($str); $i++) {
            $char = $str[$i];
            if (preg_match('/[\p{Cyrillic}]/u', $char)) {
                $hasCyrillic = true;
            } 
            elseif (preg_match('/[a-zA-Z]/', $char)) {
                $hasLatin = true;
            } else {
                throw new Exception("Строка содержит не-буквенные символы или символы из других алфавитов");
            }

            if ($hasCyrillic && $hasLatin) {
                throw new Exception("Слово содержит символы из разных алфавитов");
            }
        }
        return $hasCyrillic ? 'Cyrillic' : 'Latin';
    }
}
