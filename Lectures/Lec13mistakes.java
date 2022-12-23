package Lectures;

import java.io.*; // import java.io.Files не захотелось импортироваться почему-то

public class Lec13mistakes {
    public static void main(String[] args) {       
        try {
        String pathProject = System.getProperty("user.dir");
        String pathFile = pathProject.concat("/file.txt");
        File file = new File(pathFile);
        if (file.createNewFile()) {
            System.out.println("file.created");
        }
        else {
            System.out.println("file.existed");
        }
    } catch (Exception e) {
     System.out.println("catch");
    } finally {
 System.out.println("finally");
    }
}}


// try {
//     Код, в котором может появиться ошибка
//   } catch (Exception e) {
//     Обработка, если ошибка случилась
//   }
//   finally {
//     Код, который выполнится в любом случае
//   }


// Работа с ошибками при работе с файлами.
// String line = "empty";
// try {
//    File file = new File(pathFile);
//    if (file.createNewFile()) {
//        System.out.println("file.created"); }
//    else {
//        BufferedReader bufReader =
//        new BufferedReader(new FileReader(file));
//        System.out.println("file.existed");
//        line = bufReader.readLine();
//        bufReader.close(); }
// } catch (Exception e) {
//    //e.printStackTrace();
// } finally {
//    System.out.println(line);
// }

  
