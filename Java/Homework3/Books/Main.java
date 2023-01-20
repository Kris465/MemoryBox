package Homework3.Books;

import java.util.ArrayList;
import java.util.List;

// 3. Сведения о книге состоят из названия, фамилии автора, цены, года издания и количества страниц. 
// Найти названия книг, в которых простое количество страниц, фамилия автора содержит «А» и год издания не позднее 2010 г.

public class Main {
    public static void main(String[] args) {
        Books book1 = new Books("Магия слов", "Казаков", 500.0, 2021, 102);
        Books book2 = new Books("Рыжик на обочине", "Тайлер", 998.0, 2022, 467);
        Books book3 = new Books("Главная улица", "Льюис", 446.0, 2022, 439);
        Books book4 = new Books("Кентавр", "Апдайк", 410.0, 2022, 192);
        List<Books> listbooks = new ArrayList<>();
        listbooks.add(book1);
        listbooks.add(book2);
        listbooks.add(book3);
        listbooks.add(book4);

        for (int i = 0; i < listbooks.size(); i++) {
            Books book = listbooks.get(i);
            int k = 3;
            int page = book.getPages();
            String bookName = "Не подходит.";
            
            if ((book.getPages() <= 2) && (book.getYear() > 2010) && (book.getAuthor().contains("а"))) {
                bookName = book.getTitle();
            }

            if ((book.getPages() > 2) && (book.getYear() > 2010) && (book.getAuthor().contains("а"))) {
                while (k < page) {
                    if (page % k != 0) {
                        bookName = book.getTitle();
                    } else {
                        break;
                    }
                    k += 2;
                }
            }

            System.out.println(bookName);
        }
    }
}
